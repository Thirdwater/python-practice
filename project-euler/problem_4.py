"""A solution to project euler problem 4
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906,609
"""

from math import inf


def is_palindrome(n: int) -> bool:
    n_forward = str(abs(n))
    n_backward = n_forward[::-1]
    return n_forward == n_backward


def terms_generator():
    for term_1 in reversed(range(100, 999)):
        for term_2 in reversed(range(100, term_1)):
            yield term_1, term_2


if __name__ == '__main__':
    max_so_far = -inf
    for term_1, term_2 in terms_generator():
        product = term_1 * term_2
        if term_1 == term_2 and product < max_so_far:
            break
        if is_palindrome(product) and product > max_so_far:
            max_so_far = product
    print(max_so_far)
