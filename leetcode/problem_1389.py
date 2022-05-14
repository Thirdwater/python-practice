"""A solution to leetcode problem 1389
https://leetcode.com/problems/create-target-array-in-the-given-order/
"""
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target_num = nums[i]
            target_index = index[i]
            target.insert(target_index, target_num)
        return target
