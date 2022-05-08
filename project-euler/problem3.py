"""A solution to project euler problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer: 6,857
"""
from typing import Optional

from utils.prime import prime_factors


def naive_solution(n:int) -> Optional[int]:
    factors = prime_factors(n)
    if factors:
        return factors[-1]
    return None


if __name__ == '__main__':
    print(naive_solution(600851475143))
