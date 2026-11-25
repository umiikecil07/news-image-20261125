"""The World Today — 25 November 2026: one-page news front page.

Draws the front page with Pillow and writes it to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when set). The drawing is a pure
function of stories.py, so two runs produce byte-identical output.

If Pillow is unavailable at runtime, falls back to copying the shipped
entry.png that this program produced during development.
"""

import hashlib
import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    try:
        from frontpage import build_page

        page = build_page()
    except ImportError:
        shipped = os.path.join(_HERE, "entry.png")
        if os.path.exists(shipped):
            shutil.copyfile(shipped, out_path)
            print("Pillow unavailable; copied shipped entry.png")
            return 0
        raise
    page.save(out_path, format="PNG")
    digest = hashlib.sha256(open(out_path, "rb").read()).hexdigest()
    print("Wrote %s (%d bytes, sha256 %s)"
          % (out_path, os.path.getsize(out_path), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
