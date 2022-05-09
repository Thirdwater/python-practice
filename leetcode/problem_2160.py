"""A solution to leetcode problem 2160
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
"""
class Solution:
    def minimumSum(self, num: int) -> int:
        # Note we get the minimum sum when we take the 2 smallest digits as the tenth digits,
        # and the 2 largest digits as the unit digits.
        # But to prove this, consider:
        #   1. For any digits 0 <= a <= b <= 9,
        #        a + b <= 10a + b (equal if a = 0)
        #      Similarly, for 0 <= a <= b <= c <= 9,
        #        a + b + c <= 10a + b + c <= 100a + 10b + c
        #      I.e. it is cheaper (or equal) to add the digits rather than combining them into a number.
        #   2. For any digits 0 <= a <= b <= c <= d <= 9,
        #        (10a + c) + (10b + d) =  10a + 10b + c + d
        #                              <= (100a + 10b + c) + d
        #      I.e. it is cheaper (or equal) to add 2 2-digit numbers rather than 1 1-digit and 1 3-digit.
        #      Also the pairing of 2 smallest digits with 2 largest digits doesn't matter.
        digits = [int(digit_string) for digit_string in str(num)]
        sorted_digits = sorted(digits)
        num_1 = (10 * sorted_digits[0]) + sorted_digits[2]
        num_2 = (10 * sorted_digits[1]) + sorted_digits[3]
        return num_1 + num_2
