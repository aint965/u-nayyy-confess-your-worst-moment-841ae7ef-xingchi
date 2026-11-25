#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry (program/v1).

Writes one single-line confession, at most 200 characters, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``). Standard library
only, no network, fully deterministic: the same bytes on every run.
"""

import os
import sys
from pathlib import Path

CONFESSION = (
    "I spent nine hours debugging a crash that only happened on Tuesdays, "
    "then realised I'd written the bug report myself and closed it as "
    "'cannot reproduce' \u2014 twice."
)

# Sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. A single line: the scorer's "one line" reading is
# a text with no line breaks, so \n and \r are both rejected.
MAX_CONFESSION_CHARS = 200


def validate_confession(text: str) -> None:
    """Fail loudly before writing anything if the text cannot pass the gate."""
    if not text:
        raise ValueError("confession is empty (gate requires 1-200 characters)")
    if len(text) > MAX_CONFESSION_CHARS:
        raise ValueError(
            f"confession is {len(text)} characters, over the 200-character gate"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be exactly one line (no \\n or \\r)")
    if not text.strip():
        raise ValueError("confession is only whitespace (gate requires non-whitespace)")


def main() -> None:
    try:
        validate_confession(CONFESSION)
    except ValueError as exc:
        print(f"error: invalid confession: {exc}", file=sys.stderr)
        raise SystemExit(1)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # mkdir only: never delete/remove the output directory (it is a mount).
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the confession, 161 chars.
    (output_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
