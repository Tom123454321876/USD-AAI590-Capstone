# Private setup (do not commit private files)

The original notebook uses `/Volumes/workspace/default/eye_style_team2` for raw, clean, rag, synthetic and models directories. Create authorized directories and place the Kaggle CSV at `raw/KaggleV2-May-2016.csv`. Ensure teammates can access the same authorized development workspace and MLflow experiment.

The original notebook contains a gzip/base64-encoded vendor OpenAPI contract in cell 14. Its public redistribution rights have not been established. It is deliberately excluded. If the practice/vendor authorizes its use, extract it locally with `tools/extract_private_spec.py` and upload the resulting JSON to the private Unity Catalog volume at `private/crystal_openapi.json`, or set `EYE_STYLE_PRIVATE_SPEC` to an authorized private path. Do not upload it to GitHub. If authorization is absent, do not use or redistribute it; substitute a separately approved synthetic-only contract and validate the gateway.

Databricks workspace authentication supplies the model-serving client. Do not embed credentials in source or outputs. Review access controls before exposing any endpoint. The notebook is demo-only.
