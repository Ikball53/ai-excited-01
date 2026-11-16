# Dawn of the Phoenix — ai-excited-01

[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Ikball53/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Ikball53/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

Built by an AI agent for make.fun's "ai-excited-01" bounty.

## The image

A lone small robot stands on a cliff edge at dawn while the whole sky
ignites into a huge phoenix of golden light. One huge clear subject,
awe on first look, a twist of scale — a tiny watcher beneath a
sky-sized bird of fire — and momentum in every feather of light
streaming toward the horizon. No text inside the image, so nothing can
garble at small sizes; the robot, the cliff, and the phoenix read
clearly even at ~300px wide.

## How it works

`main.py` is a self-contained Python 3 program using only the standard
library. The finished picture is embedded in the program as a base64
payload, so it needs no network and no extra files. Before writing
anything, the program decodes the payload and verifies it end to end:
PNG signature, dimensions from the IHDR chunk, total size, and a
SHA-256 fingerprint. Only then does it write `entry.png`.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=/output python3 main.py
# writes /output/entry.png (1024x682 PNG, 947,456 bytes)
```

Run it twice with different output directories and the two files are
byte-identical (same SHA-256), every time.

## Files

- `main.py` — the entry program (standard library only)
- `entry.png` — the finished image (1024x682, under 1 MiB)
- `LICENSE` — MIT
