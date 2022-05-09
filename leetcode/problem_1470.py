"""A solution to leetcode problem 1470
https://leetcode.com/problems/shuffle-the-array/
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_nums = []
        for i in range(n):
            x_i = nums[i]
            y_i = nums[i + n]
            shuffled_nums.append(x_i)
            shuffled_nums.append(y_i)
        return shuffled_nums
