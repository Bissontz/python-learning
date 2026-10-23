# Easy — Array intersection

**Pattern:** hash set  
**Timebox:** ~15–20 minutes

## Problem

Given two integer lists `nums1` and `nums2`, return a list of their **unique** intersection — each value that appears in **both**, at most once in the result.

- Order of the result does **not** matter (tests compare as sets).
- Values may repeat inside either input; still emit each shared value once.

## Examples

```
nums1 = [1, 2, 2, 1], nums2 = [2, 2]     → [2]
nums1 = [4, 9, 5],    nums2 = [9, 4, 9, 8, 4]  → [4, 9]  # any order
nums1 = [1, 2],       nums2 = [3, 4]     → []
```

## Constraints (interview-scale)

- `0 <= len(nums1), len(nums2) <= 1000` (interview Easy scale)
- Values fit in a normal Python `int`

## Deliverable

Implement `intersection(nums1: list[int], nums2: list[int]) -> list[int]` in `solution.py`.

Think aloud: clarify → examples → approach → code → test.
