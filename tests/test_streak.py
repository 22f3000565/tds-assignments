import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test with a list containing no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test with a single streak of positive numbers."""
    assert longest_positive_streak([-1, 1, 2, 3, -4, 5]) == 3

def test_multiple_streaks_longest_first():
    """Test with multiple streaks, where the longest streak is first."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test with multiple streaks, where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3]) == 3

def test_streaks_with_zeros_and_negatives():
    """Test with streaks separated by zeros and negative numbers."""
    assert longest_positive_streak([1, 0, 2, 3, -1, 4, 5, 6]) == 3

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4
