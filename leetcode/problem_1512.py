"""A solution to leetcode problem 1512
https://leetcode.com/problems/number-of-good-pairs/
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Note that for n of the same integer, there are nChoose2 such pairs.
        # nChoose2 = n!/(2!(n - 2)!) = n(n-1)/2
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        num_pairs = 0
        for count in num_count.values():
            num_pairs += count * (count - 1) // 2
        return num_pairs
