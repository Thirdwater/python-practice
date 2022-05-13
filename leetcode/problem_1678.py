"""A solution to leetcode problem 1678
https://leetcode.com/problems/goal-parser-interpretation/
"""
class Solution:
    def interpret(self, command: str) -> str:
        interpretation = command.replace("(al)", "al")
        interpretation = interpretation.replace("()", "o")
        return interpretation
