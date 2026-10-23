# Hints (use only if stuck ≥5 minutes)

1. Brute force nested comparisons works but is O(n²).
2. Sort then scan adjacent pairs — O(n log n).
3. Interview favorite: put values in a `set` while scanning; if you see a value already in the set, return `True`.
4. Compare `len(nums)` to `len(set(nums))` — same idea, one liner (still say the set idea out loud).
