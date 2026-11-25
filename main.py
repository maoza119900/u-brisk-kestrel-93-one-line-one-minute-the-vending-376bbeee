#!/usr/bin/env python3
"""Write the vending-machine pickup line to the output file.

Deterministic: a single fixed string, no clock, randomness, network
or file input. The output path honours $MAKEFUN_OUTPUT_DIR and
defaults to /output/entry.txt, the path the competition gate reads.
"""

import os

# The entry is exactly 117 characters: inside the gate's 1-200 range,
# one line, no trailing newline, so the file holds the line and nothing else.
LINE = "Hey, beautiful \u2014 I only take exact change, but for you I\u2019d jam my own slot. Press B7 and let me drop something sweet."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
