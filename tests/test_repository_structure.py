import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class StructureTests(unittest.TestCase):
    def test_manifest_notebooks(self):
        stages = json.loads((ROOT / "config/stages.json").read_text())
        seen = set()
        for stage in stages:
            data = json.loads((ROOT / stage["path"]).read_text())
            for cell in data["cells"]:
                original = cell.get("metadata", {}).get("original_cell")
                if original is not None:
                    self.assertNotIn(original, seen)
                    seen.add(original)
                if cell["cell_type"] == "code":
                    self.assertEqual(cell["outputs"], [])
                    compile("".join(cell["source"]), stage["path"], "exec")
        self.assertEqual(len(seen), sum(len(s["original_cells"]) for s in stages))
    def test_private_contract_not_included(self):
        self.assertFalse(any(ROOT.rglob("crystal_openapi.json")))
if __name__ == "__main__":
    unittest.main()
