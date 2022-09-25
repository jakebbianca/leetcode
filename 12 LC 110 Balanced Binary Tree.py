"""
Balanced Binary Tree
Grind 75 #12
LC #110 Easy

Solution:
time complexity = O(n) - cut BST in half until find answer
space complexity = O(1)

Below uses a depth-first search (DFS), as we can keep track of maximum depth/height at each node
We return up the tree recursively
If at any point the tree is unbalanced, we will return -1 and send that signal back up
-1 returning up the tree at any point will signal imbalance
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        def check_depth(node):
            if node is None:
                return 0

            left_depth = check_depth(node.left)
            # Left side already unbalanced
            if left_depth == -1:
                return -1
            right_depth = check_depth(node.right)
            # Right side already unbalanced
            if right_depth == -1:
                return -1

            # Left and right subtrees differ more than 1 -> unbalanced
            if abs(left_depth - right_depth) > 1:
                return -1

            # If balanced, return the depth of current node
            # Add 1 depth to the current node itself
            return 1 + max(left_depth, right_depth)

        return check_depth(root) != -1