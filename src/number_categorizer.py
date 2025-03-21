"""
Problem:
Task: Write a program that processes a list of integers and categorizes them into the following groups:

1. Positive: Numbers greater than 0.
2. Negative: Numbers less than 0.
3. Zero: Numbers equal to 0.
4. Even: Numbers divisible by 2.
5. Odd: Numbers not divisible by 2.
6. Prime: Numbers greater than 1 and divisible only by 1 and themselves.
7. Perfect: Numbers that are equal to the sum of their divisors (excluding themselves).

For each number in the list, create a category that consists of a combination of these conditions.
The format should be a list of strings where each string is a combination of categories,
separated by commas (e.g., "positive, even", "negative, odd", "prime", "zero, even" etc.).

Write a function categorize_numbers(nums: List[int]) -> List[str] that implements this transformation.

Additionally, create helper functions:
1. is_prime(num: int) -> bool: returns True if the number is prime.
2. is_perfect(num: int) -> bool: returns True if the number is perfect.
"""

from typing import List


def is_prime(num: int) -> bool:
    """Returns True if num is a prime number."""
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_perfect(num: int) -> bool:
    """Returns True if num is a perfect number."""
    if num <= 0:
        return False
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_divisors == num


def categorize_numbers(nums: List[int]) -> List[str]:
    result = []

    for num in nums:
        categories = []

        # Check zero
        if num == 0:
            categories.append("zero")
            categories.append("even")
        else:
            # Check positive/negative
            if num > 0:
                categories.append("positive")
            else:
                categories.append("negative")

            # Check even/odd
            if num % 2 == 0:
                categories.append("even")
            else:
                categories.append("odd")

            # Check prime
            if is_prime(num):
                categories.append("prime")

            # Check perfect
            if is_perfect(num):
                categories.append("perfect")

        # Join categories into a string and append to the result list
        result.append(", ".join(categories))

    return result


# Test the function
# nums = [1, 2, 3, 4, 5, 6, 7, -1, 0]
# print(categorize_numbers(nums))
