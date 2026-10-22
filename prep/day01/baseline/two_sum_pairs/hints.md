# Hints (use only if stuck ≥5 minutes)

1. Brute force nested loops works but is O(n²). Interviewers often want better.
2. While scanning left → right, store `value → index` in a dict.
3. For each `nums[i]`, ask: have I already seen `target - nums[i]`?
4. If yes, return `[seen[complement], i]`. If no, record `nums[i]` and continue.
