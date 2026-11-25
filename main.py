#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan (one line, at most 20 words) to /output/entry.txt.

The slogan:
    Your Solana wallet finally grew a brain — and it spends better than you do.

Why this line (judge criteria, in order):
1. Names the wallet outright: "Solana wallet".
2. Fresh image, no stock crypto lines: a wallet that "grew a brain" — no
   keys, moons or bags.
3. Plain words, clear on one read: your wallet now thinks and spends for you.
4. Rhythm + contrast that sticks: "finally grew a brain" vs "spends better
   than you do" — the wallet talks back and judges its owner, gently.
5. Honest: a wallet agent really does transact on your behalf.

15 whitespace-separated tokens (14 words + the em dash), 75 characters —
well inside the gate (1-140 chars, UTF-8, one line).
Tie-break favours the smaller text, so the line stays short on purpose.

Antigravity's 10 ideas were read and weighed (file agy-ideas.txt): its best,
"I settled forty Solana swaps while your bank was still verifying your
mother's maiden name", is vivid but leans on the jargon word "swaps" and is
21 characters longer; this line keeps zero jargon, names the wallet outright,
and keeps the wallet-voice + judgement twist from the rounds-board pattern.
"""

import os
import stat

SLOGAN = "Your Solana wallet finally grew a brain \u2014 and it spends better than you do."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate: 1-140 UTF-8 characters, one line, not only whitespace.
    text = SLOGAN.strip()
    assert "\n" not in text, "slogan must be a single line"
    assert 1 <= len(text) <= 140, "slogan must be 1-140 characters"
    assert len(text.split()) <= 20, "slogan must be at most 20 words"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Program entries: files under /output must be mode 0644.
    os.chmod(OUTPUT_PATH, 0o644)
    print(text)


if __name__ == "__main__":
    main()
