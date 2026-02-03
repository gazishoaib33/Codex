"""Math-related coding problems."""

from typing import Iterable


def sum_of_multiples(limit: int, multiples: Iterable[int] = (3, 5)) -> int:
    """Return the sum of all numbers below `limit` divisible by any of `multiples`.

    Example: sum_of_multiples(10) -> 23 (3 + 5 + 6 + 9)
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")
    unique_multiples = {m for m in multiples if m != 0}
    if not unique_multiples:
        return 0
    total = 0
    for number in range(limit):
        if any(number % m == 0 for m in unique_multiples):
            total += number
    return total
