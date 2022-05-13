"""A solution to leetcode problem 1528
https://leetcode.com/problems/shuffle-string/
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_chars = [None] * len(s)
        for original_index, target_index in enumerate(indices):
            shuffled_chars[target_index] = s[original_index]
        return "".join(shuffled_chars)
