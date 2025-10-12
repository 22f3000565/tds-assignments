import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 3, -1, 4, 5, 6, 7, 0, 8]) == 4

def test_streaks_with_zeros():
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_streaks_with_negatives():
    assert longest_positive_streak([-1, -2, 1, 2, -3, 3, 4, 5]) == 3

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5
