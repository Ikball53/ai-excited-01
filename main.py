#!/usr/bin/env python3
"""Copy the bundled ai-excited-01 artwork into the output folder.

The picture lives next to this script as entry.png. This program only
checks that the file is a genuine, in-limits PNG and then copies its
bytes verbatim, so the rendered image is byte-identical every run.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

# Fingerprint of entry.png, measured in this session with sha256sum.
EXPECTED_SHA256 = "19360e84c5ec956f0e71a7e9a0cc24772f47fc72c3c4debc23806ca8e19178d2"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message: str) -> "NoReturn":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_png(payload: bytes) -> tuple[int, int]:
    if not payload:
        fail("entry.png is empty")
    if len(payload) > MAX_BYTES:
        fail(f"entry.png is {len(payload)} bytes, over the {MAX_BYTES}-byte limit")
    if payload[:8] != PNG_MAGIC:
        fail("entry.png does not start with the PNG signature")
    if len(payload) < 33 or payload[12:16] != b"IHDR":
        fail("entry.png is missing a valid IHDR chunk")
    width, height = struct.unpack(">II", payload[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        fail(f"entry.png is {width}x{height}, over the {MAX_SIDE}px limit")
    return width, height


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        fail(f"entry.png not found next to main.py ({here})")
    payload = source.read_bytes()
    width, height = check_png(payload)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        fail("entry.png sha256 mismatch -- refusing to copy a changed file")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(payload)
    print(f"wrote {target} ({width}x{height}, {len(payload)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
