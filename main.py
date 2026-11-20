"""把仓库中的 entry.png 逐字节复制到评测器指定的输出目录（$MAKEFUN_OUTPUT_DIR）。"""

import os
import shutil
import sys
from pathlib import Path

OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> int:
    src = Path(__file__).resolve().parent / OUTPUT_NAME
    if not src.is_file():
        print(f"error: source file not found: {src}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    dst = out_dir / OUTPUT_NAME
    try:
        shutil.copyfile(src, dst)
    except OSError as exc:
        print(f"error: cannot copy {src} -> {dst}: {exc}", file=sys.stderr)
        return 1

    if dst.read_bytes() != src.read_bytes():
        print(f"error: copy verification failed: {dst} differs from {src}", file=sys.stderr)
        return 1

    print(f"copied {src} -> {dst} ({src.stat().st_size} bytes, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
