"""A solution to leetcode problem 1431
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_threshold = max(candies)
        can_reach_max = []
        for kid_candies in candies:
            can_reach_max.append(kid_candies + extraCandies >= candy_threshold)
        return can_reach_max
