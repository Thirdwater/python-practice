"""A solution to leetcode problem 771
https://leetcode.com/problems/jewels-and-stones/
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_types = list(jewels)
        jewel_count = 0
        for stone in stones:
            if stone in jewel_types:
                jewel_count += 1
        return jewel_count
