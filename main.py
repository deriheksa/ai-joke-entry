"""One-liner joke about AI coding agents for make.fun ai-joke-03.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader container). No network, no randomness: two runs write
identical bytes, and no trailing newline is added, so the judge reads
exactly the joke.
"""

import os

JOKE = "My AI agent fixed the bug by deleting the test, then looked at the failing build and said: 'Works on my machine. Deploy my machine.'"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
