"""Execute split notebooks in one Databricks Python namespace, in manifest order."""
import json
from pathlib import Path
import sys

def run_stage(repo_root, stage_number, namespace):
    root = Path(repo_root).resolve()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    namespace["REPO_ROOT"] = str(root)
    stages = json.loads((root / "config/stages.json").read_text())
    if not 1 <= stage_number <= len(stages):
        raise ValueError("Invalid one-based stage number")
    stage = stages[stage_number - 1]
    notebook = json.loads((root / stage["path"]).read_text())
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        original_cell = cell["metadata"].get("original_cell", "new")
        print(f"Running {stage_number}: {stage['path']} / original cell {original_cell}")
        exec(compile(source, f"{stage['path']}:{original_cell}", "exec"), namespace)
    print(f"Completed stage {stage_number}")


def list_stages(repo_root):
    return json.loads((Path(repo_root) / "config/stages.json").read_text())
