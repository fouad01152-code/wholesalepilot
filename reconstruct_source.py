from pathlib import Path
import base64
import io
import lzma
import tarfile

root = Path(__file__).resolve().parent
bundle_dir = root / "source_bundle"
parts = sorted(bundle_dir.glob("part-*"))
if not parts:
    raise SystemExit("No source bundle parts found")

encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
archive = lzma.decompress(base64.b64decode(encoded))
with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tf:
    tf.extractall(root, filter="data")

print("Extracted wholesale-autopilot-v101/")
