#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One Star, Written in Sap": A genuine one-star review built from a plant's-eye view of water, soil and light: watered by calendar not soil, evicted from the sill for a candle she never lights, and praised for a new leaf by the human standing in its light.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "One star: She waters me by calendar, not by soil - flooded on Mondays, dust-dry by Friday - moved me off the sunny sill for a candle she never lights, and calls my new leaf 'a good sign' while standing in my light."
TEXT = LINE + "\n"
MAX_CHARS = 279
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
