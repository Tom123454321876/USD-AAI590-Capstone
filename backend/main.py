"""Demo-only HTTP bridge. Upstream must implement the documented serving contract."""
import json
import os
from urllib.parse import urlparse

import firebase_admin
from firebase_admin import auth
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024
firebase_admin.initialize_app(options={'projectId': os.getenv('FIREBASE_PROJECT_ID', 'eye-style-optometry---ai')})
ROLES = {'owner': 'Owner', 'receptionist': 'Front Desk', 'front desk': 'Front Desk', 'optician': 'Optician'}
WORKFLOWS = {'Owner': {'Scheduling', 'Insurance Verification', 'Optical Orders', 'RAG'}, 'Front Desk': {'Scheduling', 'Insurance Verification', 'Optical Orders', 'RAG'}, 'Optician': {'Optical Orders', 'RAG'}}


def failure(message, status):
    return jsonify(success=False, error=message), status


@app.after_request
def cors(response):
    origin = request.headers.get('Origin')
    if origin and origin in os.getenv('ALLOWED_ORIGINS', '').split(','):
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Vary'] = 'Origin'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.get('/health')
def health():
    return jsonify(status='ok', mode='demo', upstream_configured=bool(os.getenv('DATABRICKS_SERVING_URL') and os.getenv('DATABRICKS_TOKEN')))


def identity():
    header = request.headers.get('Authorization', '')
    if not header.startswith('Bearer '):
        return None, None, failure('Firebase ID token required.', 401)
    try:
        claims = auth.verify_id_token(header[7:])
    except Exception:
        return None, None, failure('Invalid Firebase ID token.', 401)
    # Only custom claims set by a trusted Firebase administrator are accepted.
    raw_role = claims.get('role')
    role = ROLES.get(raw_role.strip().lower()) if isinstance(raw_role, str) else None
    if not role or not claims.get('uid'):
        return None, None, failure('Authorized staff role required.', 403)
    return role, claims['uid'], None


def call_upstream(payload):
    url = os.getenv('DATABRICKS_SERVING_URL', '')
    token = os.getenv('DATABRICKS_TOKEN', '')
    parsed = urlparse(url)
    if not token or parsed.scheme != 'https' or not parsed.hostname or not parsed.path.endswith('/invocations') or parsed.username or parsed.password:
        return failure('Databricks serving endpoint not configured.', 503)
    try:
        response = requests.post(url, headers={'Authorization': 'Bearer '+token}, json={'dataframe_records': [payload]}, timeout=(10, 120), allow_redirects=False)
        if response.status_code != 200:
            return failure('Databricks request failed.', 502)
        result = response.json()['predictions']
        if not isinstance(result, list) or len(result) != 1:
            raise ValueError('Invalid prediction envelope')
        result = result[0]
        if isinstance(result, str):
            result = json.loads(result)
        if not isinstance(result, dict) or result.get('success') is not True or result.get('mode') != 'demo' or result.get('role') != payload['authenticated_role']:
            raise ValueError('Invalid response contract')
        if payload['action'] == 'chat' and (result.get('workflow') != payload['workflow'] or not isinstance(result.get('answer'), str) or not result['answer'].strip() or result.get('requires_staff_review') is not True):
            raise ValueError('Invalid chat response')
        if payload['action'] == 'dashboard':
            records = result.get('records')
            if not isinstance(records, list) or any(not isinstance(r, dict) or r.get('workflow_type') not in WORKFLOWS[payload['authenticated_role']] - {'RAG'} for r in records):
                raise ValueError('Invalid dashboard response')
        if payload['action'] == 'capabilities' and (result.get('read_only') is not True or result.get('live_crystal_connected') is not False):
            raise ValueError('Invalid capabilities response')
        return jsonify(result)
    except (requests.RequestException, ValueError, KeyError, TypeError):
        return failure('Invalid or unavailable Databricks response.', 502)


@app.post('/chat')
def chat():
    role, uid, error = identity()
    if error: return error
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or set(body) != {'question', 'workflow'}:
        return failure('Provide only question and workflow.', 400)
    question, workflow = body['question'], body['workflow']
    if not isinstance(question, str) or not question.strip() or len(question.strip()) > 4000:
        return failure('Question must contain 1–4000 characters.', 400)
    if not isinstance(workflow, str) or workflow not in WORKFLOWS[role]:
        return failure('Workflow access denied.', 403)
    return call_upstream({'action':'chat', 'question':question.strip(), 'workflow':workflow, 'authenticated_role':role, 'authenticated_subject':uid})


def read_action(action):
    role, uid, error = identity()
    if error: return error
    return call_upstream({'action':action, 'question':'', 'workflow':'', 'authenticated_role':role, 'authenticated_subject':uid})


@app.get('/dashboard')
def dashboard(): return read_action('dashboard')


@app.get('/capabilities')
def capabilities(): return read_action('capabilities')
