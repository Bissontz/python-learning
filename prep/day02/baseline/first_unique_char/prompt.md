# Easy — First unique character

**Pattern:** strings + hash map (counts)  
**Timebox:** ~15–20 minutes

## Problem

Given a string `s`, find the **first** non-repeating character and return its **index**. If every character repeats, return `-1`.

- Case-sensitive (`'A'` ≠ `'a'`).
- Indexing is 0-based.

## Examples

```
s = "leetcode"      → 0    # 'l'
s = "loveleetcode"  → 2    # 'v'
s = "aabb"          → -1
```

## Constraints (interview-scale)

- `1 <= len(s) <= 100_000`
- `s` consists of lowercase English letters in typical interview versions (your code can still treat chars generally)

## Deliverable

Implement `first_uniq_char(s: str) -> int` in `solution.py`.

Think aloud: clarify → examples → approach → code → test.
