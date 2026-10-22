# Easy — Pair indices that sum to target

**Pattern:** arrays + hash map  
**Timebox:** ~10–12 minutes (part of the 20–25 min Day 1 baseline)

## Problem

You are given a list of integers `nums` and an integer `target`.

Return the **indices** of two distinct elements that add up to `target`.

- Exactly one valid pair is guaranteed.
- You may not use the same element twice.
- Order of the two indices does not matter for correctness (tests accept either order).

## Examples

```
nums = [2, 7, 11, 15], target = 9  →  [0, 1]   # 2 + 7
nums = [3, 2, 4],       target = 6  →  [1, 2]   # 2 + 4
nums = [3, 3],          target = 6  →  [0, 1]
```

## Constraints (interview-scale)

- `2 <= len(nums) <= 10_000`
- Values fit in a normal Python `int`

## Deliverable

Implement `two_sum(nums: list[int], target: int) -> list[int]` in `solution.py`.

Think aloud: clarify → example → approach → code → quick mental test.
