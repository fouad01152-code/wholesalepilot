from pathlib import Path
import base64
import io
import lzma
import shutil
import tarfile

root = Path(__file__).resolve().parent
parts = sorted((root / ".source-package").glob("part-*"))
if not parts:
    raise SystemExit("No .source-package parts found")

encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
raw = lzma.decompress(base64.b64decode(encoded))
with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as tf:
    tf.extractall(root, filter="data")

print("Materialized WholesalePilot source into", root)
