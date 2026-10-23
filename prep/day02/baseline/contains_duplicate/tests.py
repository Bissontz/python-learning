"""Simple tests for contains_duplicate. Run from repo root:
pytest prep/day02/baseline/contains_duplicate/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("contains_duplicate_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
contains_duplicate = _mod.contains_duplicate


def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_all_unique():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_many_duplicates():
    assert contains_duplicate([1, 1, 1, 3, 3]) is True


def test_single_element():
    assert contains_duplicate([42]) is False


def test_negatives():
    assert contains_duplicate([-1, 0, -1]) is True
