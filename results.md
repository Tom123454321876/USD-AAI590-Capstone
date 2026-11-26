# Historical Week 6 results (not rerun after split)

Source: original `Eye_Style_AI_Agent_team_2 (15).ipynb` saved outputs and Week 6 report. These values describe the earlier notebook run; they are not a new verification of this repository.

- Cleaned appointments: 110,521. Patient-grouped train/validation/test: 77,565 / 16,534 / 16,422.
- MLP recall 77.05%; F1 43.68%; ROC-AUC 72.02% (held-out test). The public data is not from Eye Style. The saved inference cell originally referenced a different historical MLflow run than the test cell; this split changes inference to read the freshly verified run. Do not equate prior synthetic predictions with the evaluated run without checking them.
- RAG: 15/15 in-corpus grounded answers and 5/5 appropriate abstentions on the fixed 20-question set; EXP-3, 95 words, 25-word overlap, top-k 3. LLM judging and optimization on fixed questions limit generalization.
- Workflow: 9/9 task-correct; 7/9 strict correctness. Median AI execution 6.418 seconds. No paired manual baseline.
- Website interface checks 14/14; internal deployment checks 6/6. Not evidence of actual HTTP/Firebase or clinical deployment.

Re-run in a private development workspace and independently review new model answers before reporting new results.
