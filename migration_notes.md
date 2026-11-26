# Migration notes

Source cells are one-based (including Markdown). See `config/stages.json` for exact ownership and provenance.

Original notebook SHA-256: `c6a7566bd59f89d99f141a61836a50d9e0aca96065c77abc0445019d4f012939`.

Omitted cells: 1, 2, 3, 4, 6, 7, 8, 10, 11, 26, 27, 28, 38, 51, 55, 60, 64, 73, 74, 80, 91, 92. These include introductory status/plan/handoff text, redundant dataset preview, package-install/restart cells (replaced by driver setup), and the skipped obsolete RAG template. The complete original notebook should be retained privately, not committed publicly.

Changes: reorder data cleaning before model training; preserve model split and preprocessing; extract framework and synthetic loader; externalize private OpenAPI contract; clear notebook outputs; replace historical MLflow metrics and inference pointer with verified-run metadata; make evaluation model label dynamic; gate historical human ratings. The original code still has shared globals and workspace paths. This is an incremental modularization, not a fully independent production package.

Static validation checks parse every executable extracted cell (excluding driver Databricks magic), validate notebook format, check source coverage and stage manifest. Runtime verification requires authorized Databricks access and original dataset. Some source Markdown describes historical notebook layout, not new file locations.
