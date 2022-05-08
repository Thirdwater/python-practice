"""A solution to leetcode problem 2114
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        num_words = [len(sentence.split(" ")) for sentence in sentences]
        return max(num_words)
