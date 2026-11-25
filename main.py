"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to entry.txt.
Python 3.13, standard library only; no network, no files read.
"""

import os
import sys

JOKE = "My bed filed for custody of me on Monday morning. The court ruled I only visit my job."

MAX_CHARS = 200


def resolve_output_dir():
    """The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output."""
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(var, "").strip()
        if value:
            return value
    return "/output"


def validate(text):
    """Gate: 1-200 UTF-8 characters, not whitespace-only, one line."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not encodable, though str always is
    return text


def main():
    joke = validate(JOKE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke + "\n")
    print(f"wrote {len(joke)} chars to {path}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
