"""A solution to leetcode problem 2011
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        operation_to_value_map = {
            '++X': 1,
            'X++': 1,
            '--X': -1,
            'X--': -1,
        }
        for operation in operations:
            sum += operation_to_value_map[operation]
        return sum
