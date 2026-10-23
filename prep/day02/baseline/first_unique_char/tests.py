"""Simple tests for first_uniq_char. Run from repo root:
pytest prep/day02/baseline/first_unique_char/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("first_unique_char_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
first_uniq_char = _mod.first_uniq_char


def test_first_char_unique():
    assert first_uniq_char("leetcode") == 0


def test_unique_in_middle():
    assert first_uniq_char("loveleetcode") == 2


def test_all_repeat():
    assert first_uniq_char("aabb") == -1


def test_single_char():
    assert first_uniq_char("z") == 0


def test_unique_at_end():
    assert first_uniq_char("aabbc") == 4
