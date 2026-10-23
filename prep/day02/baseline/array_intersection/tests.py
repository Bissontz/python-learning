"""Simple tests for intersection. Run from repo root:
pytest prep/day02/baseline/array_intersection/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("array_intersection_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
intersection = _mod.intersection


def test_with_duplicates():
    assert set(intersection([1, 2, 2, 1], [2, 2])) == {2}


def test_multiple_shared():
    assert set(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == {4, 9}


def test_empty_intersection():
    assert set(intersection([1, 2], [3, 4])) == set()


def test_one_empty():
    assert set(intersection([], [1, 2])) == set()


def test_identical():
    assert set(intersection([7, 7, 7], [7])) == {7}
