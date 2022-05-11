"""A solution to leetcode problem 1281
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = abs(n)
        digits_sum = 0
        digits_product = 1
        while digits > 0:
            digit = digits % 10
            digits_sum += digit
            digits_product *= digit

            digits //= 10
        # Note the solution is looking for (product - sum) in particular.
        return digits_product - digits_sum
