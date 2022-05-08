"""Prime module
In this module, we consider 1 as non-prime.
"""
from typing import List


def is_prime(n: int) -> bool:
    """
    Checks if n is prime.

    This method runs in O(sqrt(n)).
    """
    if n <= 3:
        return n >= 2
    if n % 2 == 0:
        return False

    factor = 3
    while factor**2 <= n:
        if n % factor == 0:
            return False
        factor += 2

    return True


def prime_factors(n: int) -> List[int]:
    """
    Returns a list of prime factors of n.
    """
    factors = []
    if n % 2 == 0:
        factors.append(2)

    factor = 3
    while factor**2 <= n:
        if n % factor == 0 and is_prime(factor):
            factors.append(factor)
        factor += 2

    return factors
