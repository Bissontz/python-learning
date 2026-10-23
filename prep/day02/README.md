# Day 2 — Data structures & interview patterns

Match the plan **MUST** list. Same think-aloud protocol as Day 1 — use it on **every** problem.

## Protocol (every problem)

**clarify → examples → approach → code → test**

Say each step out loud before the next. Do not jump straight to typing.

## MUST checklist

1. **4 Easy baselines** — Solve all four under `baseline/` (write code in each folder’s `solution.py`). Timebox ≈15–20 min each. Do **not** peek at `hints.md` until stuck ≥5 min. After each: `pytest prep/day02/baseline/<folder>/ -q`.
2. **Pattern journal** — One line per problem (what pattern + when you’d reach for it). Log in Agent Store `prep-progress.md` or a local note — keep it short.
3. **Pitch rehearsal** — Say your Day 1 Babel Street 60s pitch out loud **once** (no rewrite required unless something was wrong).

## How to run

From repo root (venv active, deps installed — see Day 1 setup if needed):

```bash
pytest prep/day02/ -q
```

Or one problem at a time:

```bash
pytest prep/day02/baseline/contains_duplicate/ -q
```

## NICE (if energy remains)

- 2 more Easy (arrays / hash maps)
- NeetCode array / hash map videos
- Rewrite a big-O cheat sheet from memory

## Success criteria

- [ ] ≥3/4 Easy solved in ≤20 min each with verbal approach first
- [ ] Can recite clarify → examples → approach → code → test without prompting
- [ ] One-line pattern note for each of the four
- [ ] Pitch said aloud once

## Suggested order for John

1. Skim this README + recall the protocol  
2. `contains_duplicate` → `valid_parentheses` → `first_unique_char` → `array_intersection`  
3. Pattern journal (4 lines)  
4. Pitch once out loud  
5. Mark Day 2 in Agent Store progress tracker  
