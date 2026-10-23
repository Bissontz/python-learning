"""Day 1 baseline — pair indices that sum to target.

Implement two_sum. Do not paste a finished solution here until you solve it.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two distinct elements that add up to target."""
    # raise NotImplementedError("Implement two_sum")

    if nums is None or target is None or len(nums) < 2 or len(nums) > 10000:
        return []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []