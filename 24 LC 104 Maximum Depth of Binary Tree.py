"""
Maximum Depth of Binary Tree
Grind 75 #24
LC #104
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Iterative Deque (Double-Ended Queue) Solution
Time = O(n)
Space = O(2^(depth-1))
"""
import collections
from typing import Optional


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # double-ended queue
        # iterative, non-recursive solution
        deque = collections.deque()
        depth = 0
        if root:
            deque.append(root)
        while deque:
            size = len(deque)
            for _ in range(0, size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            depth += 1
        return depth

"""
DFS Solution
Time = O(n)
The Space Complexity is also O(N). In the worst case, we are dealing with a skewed tree. 
Therefore the recursion stack will be of size O(N) because we never unravel it until we hit our base case
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            return 1 + max(left, right)
        
        
        return dfs(root)