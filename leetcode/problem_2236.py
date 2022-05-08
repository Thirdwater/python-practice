"""A solution to leetcode problem 2236
https://leetcode.com/problems/root-equals-sum-of-children/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Since root can be None, we want this safety check.
        if root is None:
            return False

        # Type-wise, we should also check existence of left and right nodes.
        # But prompt-wise, we are fine since we are guaranteed a complete tree.
        children_sum = root.left.val + root.right.val
        return root.val == children_sum
