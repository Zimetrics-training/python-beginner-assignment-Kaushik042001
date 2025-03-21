"""
Problem: Find the Longest Consecutive Sequence
Given an unsorted array of integers, write a function longest_consecutive(nums)
that returns the length of the longest consecutive elements sequence.

Example: if nums = [100, 4, 200, 1, 3, 2]; The function should return 4,
since the longest consecutive elements sequence is [1, 2, 3, 4].

Look for difference of 1 between two consecutive numbers.
"""


def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Continue the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4

nums = [1, 9, 3, 10, 2, 20]
print(longest_consecutive(nums))  # Output: 3

nums = []
print(longest_consecutive(nums))  # Output: 0
