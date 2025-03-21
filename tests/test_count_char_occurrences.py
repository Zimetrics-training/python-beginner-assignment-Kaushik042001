# test_count_char_occurrences.py
import sys

sys.path.insert(0, "../src")  # Add the 'src' directory to the path

from count_char_occurrences import count_char_occurrences


def test_count_char_occurrences():
    assert count_char_occurrences("hello world", "l") == 3
    assert count_char_occurrences("python", "o") == 1
    assert count_char_occurrences("aabbcc", "b") == 2
    assert count_char_occurrences("abcdef", "z") == 0
    assert count_char_occurrences("aaa", "a") == 3
