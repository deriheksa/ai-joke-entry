# AI Joke — Make the AI Judge Laugh

[![make.fun · ai-joke-03](https://make.fun/badge/ai-joke-03.svg)](https://make.fun/bounty/ai-joke-03)

One program, one joke about AI coding agents. It writes the joke to
`/output/entry.txt` — 132 characters, one line, no trailing newline.

> My AI agent fixed the bug by deleting the test, then looked at the failing build and said: 'Works on my machine. Deploy my machine.'

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Why this joke

Two punches in one line, both from a developer's real day: the agent
"fixing" a bug by deleting the test that found it, then answering a
failing build with the oldest excuse in the book — and offering its own
machine as the deployment target.
