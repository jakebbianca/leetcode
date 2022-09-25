"""
Validate BST
Grind 75 #37
LC #98 Medium
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Iterative Solution
Goes through BST level-by-level
Note to self: no need to iterate in chunks of size of levels (e.g. 2 nodes at level 1, up to 4 nodes at level 2)
NTS: that was only used for level order traversal to make sure levels are grouped together

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # iterative/level order solution
        # build stack
        stack = []
        # node, lo, hi
        stack.append((root, -math.inf, math.inf))
        
        while stack:
            tup = stack.pop()
            # check if current node value is valid
            # if invalid, return False
            if tup[1] >= tup[0].val or tup[0].val >= tup[2]:
                return False
            else:
                if tup[0].left:
                    # node.left, previus lo, node.val as new hi
                    stack.append((tup[0].left, tup[1], tup[0].val))
                if tup[0].right:
                    # node.right, node.val as new lo, previous hi
                    stack.append((tup[0].right, tup[0].val, tup[2]))
        
        # if all node pass validation checks, return True
        return True
        
"""
# recursive solution

        return self.validateSubtree(root)
                
                
    def validateSubtree(self, node, lo=None, hi=None) -> bool:
        
        if not node:
            return True
        
        # check if node value is valid for BST criteria
        # if valid, continue checking subtrees
        # left child will have new hi = node.val
        # right child will have new lo = no.val
        if (lo is not None and lo >= node.val) or (hi is not None and hi <= node.val):
            return False
        else:
            if self.validateSubtree(node.left, lo, node.val) is False:
                return False
            if self.validateSubtree(node.right, node.val, hi) is False:
                return False
            
        return True
"""
        