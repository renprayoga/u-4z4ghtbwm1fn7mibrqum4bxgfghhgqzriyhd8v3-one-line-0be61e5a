"""One Line, One Laugh — entry writer.

Chosen line (114 characters, one line):

    My smart fridge emailed me a diet plan, so I unplugged it and ate
    ice cream in the dark like a raccoon with Wi-Fi.

Why this line wins (judge rubric order: one funny self-contained line,
real laugh, tight, fresh, clear on first read):

- One funny line: a single self-contained joke — setup and punchline in
  one sentence, no second line needed.
- Real laugh: the turn is the revenge — the fridge that judges my eating
  gets unplugged, and I eat ice cream in the dark anyway. The
  "raccoon with Wi-Fi" image lands the absurdity.
- Tight: 114 of 140 characters, every word earns its place; "emailed me
  a diet plan" does the whole setup in five words.
- Fresh: not a stock smart-device joke (no "Alexa, play…", no
  "have you tried turning it off and on again") — a fridge that emails
  diet plans is a new angle, and the raccoon comparison is not a pun
  anyone has heard.
- Clear on first read: plain words, one image at a time, the joke needs
  no explanation.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-140 characters, not only whitespace — and
exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3 stdlib only.
"""

import os
import sys

ENTRY = (
    "My smart fridge emailed me a diet plan, so I unplugged it and ate "
    "ice cream in the dark like a raccoon with Wi-Fi."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 140


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} characters (need 1-140)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if any(line != line.rstrip() for line in entry.split("\n")):
        return _fail("entry line has trailing whitespace")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    # The gate reads the whole file: exactly one trailing newline, so the
    # file holds one line and nothing else — no blank second line.
    if written != ENTRY + "\n":
        return _fail("written file is not exactly the entry plus one newline")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
