# GitHub upload sequence

1. Thomas creates a new branch and uploads the shared setup package (preserve paths), then opens a pull request to main. Shared config and manifest refer to files that arrive in later PRs.
2. Each member creates a branch from updated main, unzips only their own package at repository root, checks their files, commits under their own account, opens a PR, and asks another member to review. Merge all three PRs.
3. Run `python -m unittest discover -s tests` on the complete repository; run the private Databricks pipeline, review the results, and fix issues before removing the existing root notebook.
4. The existing public root notebook embeds the vendor contract. If not authorized for publication, remove it promptly, review Git history (deleting the file alone does not remove past commits), and coordinate with the owner/vendor as appropriate. Retain a private backup.

Branch suggestions: `feature/data-rag`, `feature/ml`, `feature/agents`, `chore/repository-setup`. Commit messages should describe actual work. Each member should review and own their contributions, not claim authorship for work they did not perform. Preserve directory structure when uploading; do not upload ZIPs themselves.
