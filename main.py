#!/usr/bin/env python3
"""Copy the pre-rendered entry.png to the output directory and verify it.

Standard library only. Deterministic: the output is a byte copy of the
source image, so repeated runs produce identical bytes.
"""
import hashlib
import os
import shutil
import struct

MAX_BYTES = 1 * 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_size(data):
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file (bad signature)")
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG file (missing IHDR)")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        data = f.read()

    width, height = read_png_size(data)
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if (width, height) != (1024, 1024):
        raise ValueError(f"entry.png is {width}x{height}, expected 1024x1024")

    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        written = f.read()
    if hashlib.md5(written).hexdigest() != hashlib.md5(data).hexdigest():
        raise ValueError("output bytes differ from source")

    print(f"OK: wrote {dst} ({len(data)} bytes, 1024x1024, "
          f"md5 {hashlib.md5(data).hexdigest()})")


if __name__ == "__main__":
    main()
