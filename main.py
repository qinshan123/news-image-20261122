#!/usr/bin/env python3
"""make.fun news-image-20261122 entry program.

Writes the finished poster to /output/entry.png. The poster itself is a
pre-rendered asset (assets/entry.png) built by build_poster.py from the
day's verified headlines; this program simply emits it, byte for byte,
so two runs always produce identical output. Standard library only,
no network.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "assets", "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
