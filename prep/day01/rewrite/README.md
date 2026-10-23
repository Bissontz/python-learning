# Rewrite exercise — clean up `messy.py`

## Task

`messy.py` is a realistic “works on my machine” script: vague names, nested conditionals, bare `except`, manual bubble sort, mixed severity encodings, and file I/O without structure.

**Your job:** rewrite it into **`clean.py`** in this same folder.

## Expectations for `clean.py`

- Clear function boundaries (e.g. load → normalize → aggregate → report)
- Readable names; no single-letter soup outside tiny loops
- Basic error handling (`FileNotFoundError`, bad JSON shape) with useful messages
- Same observable behavior on `sample_events.json`:
  - Count usable rows (must have `id`)
  - Print location counts (highest first)
  - Print high-severity snippets (`id|actor|summary-or-desc`)
  - Write `summary_out.txt` with `count=` and `high=`
- Severity variants (`HIGH` / `high` / `3` / etc.) still normalize to `high` / `medium` / `low`
- Empty / missing location → `UNSPECIFIED`

## How to run

```bash
# baseline behavior (optional reference)
python prep/day01/rewrite/messy.py

# your rewrite
python prep/day01/rewrite/clean.py
```

Do **not** copy `messy.py` and rename variables only — restructure it.
