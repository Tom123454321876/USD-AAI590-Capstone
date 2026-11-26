# Execution order

Use the shared Databricks kernel via `run_pipeline.ipynb`. Each row is one stage. Do not launch separate notebook kernels and assume Python globals persist. Install dependencies first. Stage 1 uses the original shared volume. Back up all existing artifacts because training and data generation can overwrite them. All stages are prototype-only.

| Stage | Owner | Notebook | Original cells |
|---:|---|---|---|
| 1 | Daniel | `data_pipeline/01_data_cleaning.ipynb` | 5, 56, 57, 58 |
| 2 | Daniel | `data_pipeline/02_exploratory_data_analysis.ipynb` | 59, 61, 62, 63 |
| 3 | Denis | `machine_learning/01_logistic_regression.ipynb` | 29, 30, 31, 32, 33, 34, 35, 36 |
| 4 | Denis | `machine_learning/02_mlp_training.ipynb` | 37, 39, 40, 41, 42 |
| 5 | Denis | `machine_learning/03_model_optimization.ipynb` | 43 |
| 6 | Denis | `machine_learning/04_model_export_and_verification.ipynb` | 44, 45, 46, 47 |
| 7 | Denis | `machine_learning/05_model_evaluation.ipynb` | 48, 49 |
| 8 | Denis | `machine_learning/06_model_inference.ipynb` | 50 |
| 9 | Daniel | `data_pipeline/03_synthetic_crystal_data.ipynb` | 65, 72 |
| 10 | Daniel | `rag/01_knowledge_corpus.ipynb` | 66, 67 |
| 11 | Daniel | `rag/02_chunking_and_vector_index.ipynb` | 68, 69 |
| 12 | Daniel | `rag/03_retrieval_optimization.ipynb` | 70, 71 |
| 13 | Daniel | `rag/04_grounding_evaluation.ipynb` | 79, 81, 82, 83 |
| 14 | Thomas | `agents/01_agent_framework.ipynb` | 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 |
| 15 | Thomas | `agents/02_model_integration.ipynb` | 52 |
| 16 | Thomas | `agents/03_specialist_agents.ipynb` | 53, 54 |
| 17 | Thomas | `evaluation/01_workflow_evaluation.ipynb` | 75, 76, 77, 78 |
| 18 | Thomas | `agents/04_agent_security.ipynb` | 84, 85, 86 |
| 19 | Thomas | `integration/01_dashboard_output_contract.ipynb` | 87, 88, 89 |
| 20 | Thomas | `agents/05_policy_matrix.ipynb` | 90 |
| 21 | Thomas | `integration/02_website_backend.ipynb` | 93 |
| 22 | Thomas | `evaluation/02_website_integration_tests.ipynb` | 94 |
| 23 | Thomas | `integration/03_operational_data_gateway.ipynb` | 95, 96, 97, 98 |
| 24 | Thomas | `integration/04_deployment_interface.ipynb` | 99 |
| 25 | Thomas | `evaluation/03_deployment_readiness.ipynb` | 100 |

## Review gates and known issues

- Before stage 4, ensure TensorFlow is available. Before RAG and agent calls, ensure the workspace supports the original serving endpoint and model downloads.
- Stage 6 exports the chosen model, logs it to MLflow and verifies load parity. If Unity Catalog copy fails, resolve permissions/IO before proceeding. Model logging is not Unity Catalog model registration.
- Stage 8 uses the newly verified run pointer, not the historical fixed run ID. Stage 9 regenerates synthetic scores using that model.
- Stage 14 requires the private Crystal API contract and Databricks workspace authentication.
- Stage 17 original cells 77–78 include historical manually reviewed labels. Review fresh answers in cell 76, update labels in cell 77, then explicitly set `CONFIRM_FRESH_WORKFLOW_REVIEW=True` before executing cell 77. To avoid rerunning paid calls, execute cell 77 and 78 individually in the same namespace after review.
- Stage 18 original cell 86 contains historical adversarial review labels. Inspect it, run the execution portion without applying historical labels, review fresh answers, update the review dictionary, then set `CONFIRM_FRESH_ADVERSARIAL_REVIEW=True` and complete the cell. The gate intentionally prevents automatic reuse of old judgments.
- Historical RAG scores use an LLM judge; revalidate grounding. No manual timing baseline has been measured.
- Stage 25 tests internal interfaces only; Firebase token verification and public HTTP deployment are pending.
- Stage code uses the original hardcoded volume paths; to use another workspace, update all occurrences consistently. Full runtime execution and reproducibility must be checked by the team.
