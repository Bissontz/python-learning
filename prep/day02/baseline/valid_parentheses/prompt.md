# Easy — Valid parentheses

**Pattern:** stack  
**Timebox:** ~15–20 minutes

## Problem

Given a string `s` containing only the characters `'('`, `')'`, `'['`, `']'`, `'{'`, and `'}'`, return `True` if the brackets are **valid**.

Valid means:

- Open brackets must be closed by the **same type**.
- Open brackets must be closed in the **correct order**.
- Every close bracket has a matching open bracket of the same type.

## Examples

```
s = "()"        → True
s = "()[]{}"    → True
s = "(]"        → False
s = "([)]"      → False
s = "{[]}"      → True
```

## Constraints (interview-scale)

- `1 <= len(s) <= 10_000`
- `s` consists only of the six bracket characters above

## Deliverable

Implement `is_valid(s: str) -> bool` in `solution.py`.

Think aloud: clarify → examples → approach → code → test.
