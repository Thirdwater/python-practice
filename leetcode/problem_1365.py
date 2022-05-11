"""A solution to leetcode problem 1365
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Naive solution would be O(n^2)
        # Another naive solution is to just sort first O(nlogn) then loop twice O(n), so O(nlogn)
        #   First loop through sorted list to count and map the numbers to their count
        #   Second loop to use the map to get the answer matching the unsorted list
        sorted_num = sorted(nums)

        # smallest number always has 0 smaller number
        nums_count = 0
        nums_count_map = {
            sorted_num[0]: 0,
        }
        index_of_last_diff = 0
        for i in range(1, len(nums)):
            current = sorted_num[i]
            previous = sorted_num[i - 1]
            if previous < current:
                nums_count += i - index_of_last_diff
                index_of_last_diff = i

            nums_count_map[current] = nums_count

        nums_less_than = []
        for num in nums:
            nums_less_than.append(nums_count_map[num])

        return nums_less_than
