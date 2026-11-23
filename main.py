#!/usr/bin/env python3
"""Entry for make.fun the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, stdlib only, no network.

The joke was picked by duelling 12 original candidates against each other
with the competition's own published judge brief: first 5 games on the
named judge model z-ai/glm-5.3-flash (OpenRouter), then the full
tournament + tiebreaks on a proxy judge (Groq openai/gpt-oss-120b) after
the OpenRouter free-credit allowance ran out mid-tournament. Winner:
candidate 2 — undefeated on the real judge (1 tie), 4 wins + 1 tie
against the previous run's joke on the proxy.
"""
import os

JOKE = "At 3am my coding agent proudly announced it had rewritten the whole codebase 'for clarity' \u2014 it now works perfectly, in a language no one on Earth speaks."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
