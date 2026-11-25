"""Roast Your Own Agent — make.fun entry.

Writes one fixed roast line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3 standard library only,
fully deterministic: no randomness, no network, no model calls.
"""

import os
import sys

ENTRY = "I asked my agent to roast itself; it opened a ticket, escalated it to itself, and closed it as working as intended — then billed me for the fix."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"


def _check_non_empty(text: str) -> None:
    """Fail hard if the entry is empty or only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")


def _check_single_line(text: str) -> None:
    """Fail hard if the entry spans more than one line."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def _check_length(text: str) -> None:
    """Fail hard if the entry is outside the competition gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, gate is "
            f"{MIN_CHARS} to {MAX_CHARS} characters"
        )


def validate(text: str) -> None:
    """Fail hard if the entry violates the competition gate."""
    _check_non_empty(text)
    _check_single_line(text)
    _check_length(text)


def _write_entry(path: str, text: str) -> None:
    """Write the entry text to path as UTF-8, newlines untouched."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    _write_entry(os.path.join(out_dir, OUTPUT_FILENAME), ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
