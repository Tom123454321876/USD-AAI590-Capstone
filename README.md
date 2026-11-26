# Eye Style Optometry — AI Operations & Workflow Intelligence

University of San Diego | AAI590 Capstone | Team 2

Educational prototype integrating appointment no-show prediction, retrieval-augmented generation (RAG), role-scoped agents and synthetic optometry workflows. No live Crystal PM or production patient data is required for the demo. Authentication and HTTP deployment remain pending; the notebook interfaces are not a production API.

## Team responsibilities

| Team member | Workstream | Folders |
|---|---|---|
| Thomas Geraci | Agent architecture, security, integration and system tests | `agents/`, `integration/`, `evaluation/`, `src/agents/` |
| Denis Mulabegovic | Logistic regression, MLP, tuning, evaluation and inference | `machine_learning/` |
| Daniel Sims | Data preparation, EDA, synthetic fixtures and RAG | `data_pipeline/`, `rag/`, `src/data/` |

## Reproduction

1. Clone the repository into a Databricks Git folder.
2. Obtain the public [Medical Appointment No Shows dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments). Use the authorized private shared volume described in `docs/private_setup.md`.
3. Install dependencies and run `run_pipeline.ipynb` stage by stage. See `docs/execution_order.md` for prerequisites and manual reviews.
4. Compare new metrics against `docs/results.md`; do not assume historical scores are reproduced automatically.

The extracted notebooks are linked stages, not independently runnable notebooks. The runner maintains a single shared namespace because original functions depend on prior cells. The code has been statically validated, not rerun on Databricks. The split includes limited corrective refactoring; a full independent module conversion remains future work.

## Public repository safety

No raw dataset, saved predictions, model binaries, original notebook outputs, credentials or embedded vendor API specification are included. The API specification must be supplied privately only with authorization. Review the synthetic RAG corpus and all source code for publication rights before committing. Do not publish private data or secrets. The original notebook is retained privately by the team.
