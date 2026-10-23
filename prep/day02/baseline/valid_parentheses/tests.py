"""Simple tests for is_valid. Run from repo root:
pytest prep/day02/baseline/valid_parentheses/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("valid_parentheses_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
is_valid = _mod.is_valid


def test_simple_pair():
    assert is_valid("()") is True


def test_all_types():
    assert is_valid("()[]{}") is True


def test_wrong_type():
    assert is_valid("(]") is False


def test_wrong_order():
    assert is_valid("([)]") is False


def test_nested():
    assert is_valid("{[]}") is True


def test_unbalanced_open():
    assert is_valid("(((") is False


def test_unbalanced_close():
    assert is_valid(")") is False
