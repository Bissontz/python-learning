# Hints (use only if stuck ≥5 minutes)

1. Put one list into a `set`, scan the other, collect hits into a result set (avoids duplicate outputs).
2. Or: `list(set(nums1) & set(nums2))` — say “set intersection” out loud so it doesn’t look like a trick.
3. Sorting + two pointers also works if the interviewer wants O(1) extra space beyond the output.
4. Remember: unique in the **output**, even if inputs have duplicates.
