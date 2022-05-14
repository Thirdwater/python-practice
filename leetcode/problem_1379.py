"""A solution to leetcode problem 1379
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        original_stack = [original]
        clone_stack = [cloned]
        while original_stack:
            original_head = original_stack.pop(-1)
            clone_head = clone_stack.pop(-1)
            if original_head is target:  # reference equality
                return clone_head
            if original_head.left:
                original_stack.append(original_head.left)
                clone_stack.append(clone_head.left)
            if original_head.right:
                original_stack.append(original_head.right)
                clone_stack.append(clone_head.right)
