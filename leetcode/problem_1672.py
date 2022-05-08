"""A solution to leetcode problem 1672
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customer_wealth = []
        for customer_banks in accounts:
            customer_wealth.append(sum(customer_banks))
        return max(customer_wealth)
