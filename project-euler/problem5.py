"""A solution to project euler problem 5
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232,792,560
"""

def evenly_divisible_up_to(term, divisor):
    for i in range(divisor, 1, -1):
        if term % i != 0:
            return False
    return True


if __name__ == '__main__':
    candidate = 20
    while not evenly_divisible_up_to(candidate, 20):
        candidate += 20
    print(candidate)
