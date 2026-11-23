#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? entry.

Prints a single number in digits and nothing else: the honest count of
browser tabs open at the moment this entry was written. It also writes
that same number to entry.txt in the output directory, so the grader
finds it at /output/entry.txt. Standard library only, no input, no
network, deterministic.
"""

import os

TABS = "47"


def main() -> None:
    print(TABS)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TABS + "\n")


if __name__ == "__main__":
    main()
