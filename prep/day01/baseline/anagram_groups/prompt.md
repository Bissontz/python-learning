# Easy — Are these anagrams?

**Pattern:** strings + hash map (or sorting)  
**Timebox:** ~10–12 minutes (part of the 20–25 min Day 1 baseline)

## Problem

Two strings are **anagrams** if they use the same characters with the same frequencies (order may differ).

Write `is_anagram(s: str, t: str) -> bool` that returns `True` iff `s` and `t` are anagrams of each other.

- Compare case-sensitively ( `'A'` ≠ `'a'` ).
- Only the given characters matter — no need to strip punctuation unless it appears in the inputs.
- Empty string is an anagram of empty string.

## Examples

```
s = "listen", t = "silent"   → True
s = "rail safety", t = "fairy tales"  → True   # includes the space once each
s = "apple", t = "papel"     → True
s = "apple", t = "apply"     → False
s = "a", t = "ab"            → False
```

## Constraints

- `0 <= len(s), len(t) <= 100_000` in theory — prefer an O(n) counting approach over sorting if you can.

## Deliverable

Implement `is_anagram` in `solution.py`. Think aloud before coding.
