# Eye Style Optometry: AI Operations & Workflow Intelligence

**University of San Diego | AAI590 Capstone | Team 2**

An educational AI prototype for an independent optometry practice. The project combines **appointment no-show prediction**, **role-scoped AI agents**, **retrieval-augmented generation (RAG)**, and **synthetic practice-management workflows** to help staff identify tasks that need attention.

**Project status:** In development. Data preparation, logistic regression baseline training, and initial synthetic-data agent testing have been implemented. MLP training, RAG evaluation, and complete end-to-end integration remain in development.

## Team Members

| Member | Responsibilities |
|---|---|
| **Thomas Geraci** | System architecture, Databricks AI agents, security boundaries, dashboard and workflow integration |
| **Denis Mulabegovic** | No-show prediction, machine learning training, MLP development, model optimization and evaluation |
| **Daniel Sims** | Data cleaning, exploratory data analysis, synthetic records, RAG knowledge retrieval and evaluation |

## Project Overview

Independent optometry practices manage scheduling, insurance verification, optical orders, billing, and patient communications through multiple workflows.

Our project develops an AI-powered operational intelligence platform for Eye Style Optometry that helps staff identify unresolved tasks, prioritize follow-ups, and access relevant information efficiently.

The minimum viable product (MVP) focuses on three areas:

1. **Scheduling:** Predict appointment no-show risk and support staff follow-up.
2. **Insurance verification:** Identify missing or unresolved insurance verification tasks.
3. **Optical order management:** Track order status, laboratory progress, deposits, pickups, and follow-up requirements.

The system is designed around human oversight and role-based access. AI agents will not independently modify consequential patient or practice records.

## Machine Learning Architecture

### Appointment No-Show Prediction

The project uses the public Medical Appointment No Shows dataset from Kaggle.

- Original dataset: 110,527 appointment records.
- Cleaned dataset: 110,521 appointment records.
- Prediction target: Whether a patient misses an appointment.
- Baseline algorithm: Logistic Regression.
- Proposed primary model: Multilayer Perceptron (MLP).
- Dataset splitting: Patient-grouped training, validation, and testing.
- Random seed: 42.
- Baseline optimization: Classification thresholds evaluated from 0.20 to 0.80.
- Evaluation metrics: Precision, recall, F1-score, AUROC, and confusion matrices.

The MLP is intended to capture nonlinear relationships in scheduling information and will be compared with the logistic regression baseline.

### AI Agents and Retrieval-Augmented Generation

The system is designed around specialized agents for scheduling, insurance verification, and optical orders.

The AI architecture incorporates:

- Databricks-based AI workflows and language model access.
- Synthetic Crystal PM-style operational records.
- Read-only data retrieval tools.
- Role-specific access restrictions.
- RAG using approved public, synthetic, or non-PHI documents.
- Grounded responses and source attribution.
- Human review for consequential actions.

The RAG retrieval pipeline and its formal grounding evaluation remain under development.

## Development Progress

| Component | Status |
|---|---|
| Dataset cleaning and preprocessing | Completed |
| Exploratory data analysis | Completed |
| Logistic regression baseline | Implemented |
| Patient-grouped data splitting | Implemented |
| Synthetic AI agent demonstrations | Implemented |
| Initial agent safeguard tests | Implemented |
| MLP training and optimization | In progress |
| RAG retrieval and evaluation | In progress |
| Complete dashboard integration | In progress |
| Live Crystal PM API integration | Future work |

These statuses describe prototype development and do not indicate production readiness.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and machine learning |
| Databricks | AI development, notebooks, and model workflows |
| Scikit-learn | Baseline model training and evaluation |
| Neural networks | Planned MLP-based no-show prediction |
| Retrieval-Augmented Generation | Knowledge-based responses |
| Crystal PM | Planned production practice-management data source |
| GitHub | Version control and collaboration |
| Firebase | Planned application hosting and authentication |

## Repository Structure

The repository will be organized as follows:

```text
USD-AAI590-Capstone/
├── README.md
├── notebooks/
│   └── Eye_Style_AI_Agent_team_2.ipynb
├── docs/
│   └── Capstone reports and assignments
├── src/
│   └── Reusable application code
└── tests/
    └── Model and agent evaluations
```

This is the intended organization; some directories may be added as development progresses.

## Getting Started

1. Download the public [Medical Appointment No Shows dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments).
2. Open the team's Jupyter notebook in Databricks.
3. Configure the required dataset paths and workspace settings.
4. Execute the preprocessing and model-training cells.
5. Run the synthetic workflow demonstrations and available evaluation tests.

Some notebook cells rely on Databricks-specific functionality and may need modification to run locally.

Do not upload API keys, access tokens, patient information, or confidential practice records.

## Team Collaboration

Team 2 consists of Thomas Geraci, Denis Mulabegovic, and Daniel Sims.

All members will collaborate through GitHub using feature branches, commits, and pull requests.

Each contributor should document changes, keep notebook outputs reproducible when practical, and review code before merging major changes into the main branch.

## Evaluation Goals

The project aims to:

- Demonstrate scheduling, insurance, and optical-order workflows.
- Compare the MLP model against logistic regression.
- Measure prediction performance using multiple classification metrics.
- Achieve at least 90% source-supported RAG responses in the planned evaluation.
- Achieve a 100% pass rate on designed role-boundary tests.
- Improve staff task accuracy and efficiency in scripted workflows.

These figures represent evaluation targets, not completed results.

## Data Privacy and Security

The capstone uses public, synthetic, or properly de-identified data for research and development.

Live Eye Style patient information and Crystal PM production credentials are not included in the public repository.

The Medical Appointment No Shows dataset is licensed under CC BY-NC-SA 4.0. Dataset use and redistribution must respect its license conditions.

## References

- [Medical Appointment No Shows — Kaggle](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- Lewis, P., et al. (2020). *Retrieval-augmented generation for knowledge-intensive NLP tasks*. Advances in Neural Information Processing Systems.
- University of San Diego — AAI590 Applied Artificial Intelligence Capstone.

---

**Disclaimer:** This is an educational research prototype, not a production clinical system or an autonomous medical decision-making application.
