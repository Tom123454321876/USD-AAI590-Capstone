# Daniel: Lightweight handoff loader for Thomas's gateway and website integration

import os
import json

SYNTHETIC_DATA_DIR = "/Volumes/workspace/default/eye_style_team2/synthetic"

def load_synthetic_mvp_data():
    files = [
        "patients", "appointments", "scheduling_booking_features",
        "scheduled_no_show_scores", "insurance_verifications",
        "frame_orders", "contact_lens_orders", "synthetic_data_manifest"
    ]
    bundle = {}
    for name in files:
        path = f"{SYNTHETIC_DATA_DIR}/{name}.json"
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                bundle[name] = json.load(f)
    return bundle
