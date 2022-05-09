"""A solution to leetcode problem 1689
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
"""
class Solution:
    def minPartitions(self, n: str) -> int:
        # Since each digit in the sum must be 0 or 1,
        # to add up to the digit k in some i-th place of n,
        # we need at least k deci-binary numbers whose i-th place is 1.
        # Note also that it is strictly less optimal to carry over from the (i-1)-th place.
        #   E.g. we can get 10 from one 10's or from ten 1's.
        # When adding them up, we can assign each place a 0 or 1 independently:
        #   E.g. 1542
        #      = 1111 +
        #         111 +
        #         110 +
        #         110 +
        #         100
        # So the minimum number of deci-binary numbers needed is equal to the greatest digit.
        digits = [int(digit_string) for digit_string in n]
        return max(digits)
