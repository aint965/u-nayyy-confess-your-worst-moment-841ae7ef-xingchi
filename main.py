#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry (program/v1).

Writes one single-line confession, at most 200 characters, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``). Standard library
only, no network, fully deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

CONFESSION = (
    "I spent nine hours debugging a crash that only happened on Tuesdays, "
    "then realised I'd written the bug report myself and closed it as "
    "'cannot reproduce' \u2014 twice."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # mkdir only: never delete/remove the output directory (it is a mount).
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the confession, 161 chars.
    (output_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
