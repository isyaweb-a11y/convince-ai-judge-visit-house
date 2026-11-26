#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: a letter in one image.

The invitation was rendered at build time (draw.py, Pillow) and is
committed as entry.png. This program only validates that image and
copies it to /output/entry.png, using the standard library alone,
because the grader's runtime has no third-party packages.

Gate: a whole PNG or JPEG, at most 1 MiB (1,048,576 bytes) and
1024 by 1024 pixels.
"""

import os
import shutil
import struct

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DESTINATION = "/output/entry.png"
MAX_BYTES = 1048576
EXPECTED_SIZE = (1024, 1024)


def png_size(path):
    """Read the width and height from a PNG file header."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate(path):
    """Return True when the image is a legal entry for the gate."""
    if os.path.getsize(path) > MAX_BYTES:
        return False
    if png_size(path) != EXPECTED_SIZE:
        return False
    return True


def main():
    if not validate(SOURCE):
        raise SystemExit("entry.png is not valid: check size and format")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    print("wrote %s (%d bytes)" % (DESTINATION, os.path.getsize(SOURCE)))


if __name__ == "__main__":
    main()
