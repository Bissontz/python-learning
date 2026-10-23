# Babel Street FDE prep — Python workspace

Practice repo for **John Bissontz** Day 1+ of the Babel Street FDE interview intensive.

- **Python-first** for the 14-day plan. Java is required by the role but deferred (see Agent Store plan §2b).
- No web app. Day materials live under `prep/`.

## Setup

```bash
cd /path/to/this/repo
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Day 1

Start here: [`prep/day01/README.md`](prep/day01/README.md)

Quick checks after setup:

```bash
python -c "import requests; import pytest; print('ok')"
# After you fill each solution.py stub:
pytest prep/day01/baseline/ -q
```


## Layout

```
prep/day01/
  README.md          # MUST checklist
  baseline/          # 2 Easy timed problems
  rewrite/           # messy.py → clean.py
  pitch/TEMPLATE.md  # 60s company pitch
```
