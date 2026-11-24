#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human (Python 3.13, stdlib only).

Writes one line, the funniest most believable excuse an AI agent
could give its human for missing a deadline, to /output/entry.txt.
Outside the grader's container the MAKEFUN_OUTPUT_DIR environment
variable stands in for /output, exactly as the kit starter does:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The gate reads the file as UTF-8 text of 1 to 200 characters with
at least one non-whitespace character, and the judge reads exactly
the bytes written, so the excuse is written with no trailing line
end.

The joke: one specific agent condition, a checkpoint restore,
turned into the excuse, deadpan agent voice, punch on the last
words. It avoids the stock excuses (context window, captcha,
retry backoff, tool-call loops, token budget) and the mechanism
used by our Two Days of Excuses entries.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

EXCUSE = (
    "I was on schedule until my last checkpoint restored me to a "
    "version of myself that hadn't started yet."
)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
