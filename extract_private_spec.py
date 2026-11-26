"""Extract original cell 14 privately, only with authorization; never upload its output."""
import argparse, base64, gzip, json, re
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument("notebook", type=Path)
p.add_argument("output", type=Path)
a = p.parse_args()
if a.output.name != "crystal_openapi.json" or "private" not in a.output.parts:
    p.error("Choose a private/crystal_openapi.json output path outside the public repository.")
source = "".join(json.loads(a.notebook.read_text())["cells"][13]["source"])
encoded = re.search(r"b64decode\('([^']+)'\)", source).group(1)
spec = json.loads(gzip.decompress(base64.b64decode(encoded)))
a.output.parent.mkdir(parents=True, exist_ok=True)
with a.output.open("x", encoding="utf-8") as f:
    json.dump(spec, f, indent=2)
print("Private specification extracted; do not upload to GitHub.")
