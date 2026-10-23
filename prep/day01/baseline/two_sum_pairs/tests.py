"""Simple tests for two_sum. Run from repo root:
pytest prep/day01/baseline/two_sum_pairs/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("two_sum_pairs_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
two_sum = _mod.two_sum


def _normalize(pair: list[int]) -> tuple[int, int]:
    assert len(pair) == 2
    a, b = pair
    return (a, b) if a < b else (b, a)


def test_classic_example():
    assert _normalize(two_sum([2, 7, 11, 15], 9)) == (0, 1)


def test_middle_pair():
    assert _normalize(two_sum([3, 2, 4], 6)) == (1, 2)


def test_duplicates():
    assert _normalize(two_sum([3, 3], 6)) == (0, 1)


def test_negatives():
    assert _normalize(two_sum([-1, -2, -3, -4, -5], -8)) == (2, 4)
