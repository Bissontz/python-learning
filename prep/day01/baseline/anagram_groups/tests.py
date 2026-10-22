"""Simple tests for is_anagram. Run from repo root:
pytest prep/day01/baseline/anagram_groups/ -q
"""

import importlib.util
from pathlib import Path

_SOLUTION = Path(__file__).resolve().parent / "solution.py"
_spec = importlib.util.spec_from_file_location("anagram_groups_solution", _SOLUTION)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
is_anagram = _mod.is_anagram


def test_classic():
    assert is_anagram("listen", "silent") is True


def test_with_spaces():
    assert is_anagram("rail safety", "fairy tales") is True


def test_true_permutation():
    assert is_anagram("apple", "papel") is True


def test_false_different_counts():
    assert is_anagram("apple", "apply") is False


def test_different_lengths():
    assert is_anagram("a", "ab") is False


def test_empty():
    assert is_anagram("", "") is True


def test_case_sensitive():
    assert is_anagram("aA", "Aa") is True
    assert is_anagram("ab", "Ab") is False
