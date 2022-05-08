"""A solution to leetcode problem 1480
https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = []
        for i, num in enumerate(nums):
            if i == 0:
                running_sums.append(num)
            else:
                previous_sum = running_sums[-1]
                running_sums.append(previous_sum + num)
        return running_sums
