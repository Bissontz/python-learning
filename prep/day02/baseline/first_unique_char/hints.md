# Hints (use only if stuck ≥5 minutes)

1. Two passes: first count frequencies, then scan left → right for the first char with count 1.
2. `collections.Counter(s)` is fine in interviews if you explain it.
3. One pass with “index + seen twice” bookkeeping is possible but the two-pass version is clearer to narrate.
4. Empty string / all repeats → `-1`.
