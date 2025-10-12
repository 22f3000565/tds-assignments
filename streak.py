def longest_positive_streak(nums: list[int]) -> int:
    """
    Returns the length of the longest consecutive run of strictly positive integers.
    Returns 0 for empty lists.
    Non-positive values break streaks.
    """
    if not nums:
        return 0

    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 0

    if current_streak > max_streak:
        max_streak = current_streak

    return max_streak
