# Hints (use only if stuck ≥5 minutes)

1. Use a stack (list). Push opening brackets.
2. On a closing bracket, the top of the stack must be the matching opener — else invalid.
3. Keep a small map: `')' → '('`, `']' → '['`, `'}' → '{'`.
4. At the end, the stack must be empty (no leftover opens).
