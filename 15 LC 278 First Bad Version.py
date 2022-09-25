"""
First Bad Version
Grind 75 #15
LC #232 Easy

Solution:
time complexity = O(logn) - cut BST in half until find answer
space complexity = O(1)

Binary Search Solution
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # base case
        if n == 1: return 1
        
        # binary search
        l = 0
        r = n
        m = n // 2
        
        # if version m is bad, check if prev version is also bad
        # if so, continue binary search
        # if not, first bad version has been found at m
        # if version m is good, check if next version is also good
        # if so, continue binary search
        # if not, first bad version has been found at m+1
        while l <= r:
            m = l + (r - l + 1) // 2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                else:
                    r = m - 1
            else:
                if isBadVersion(m+1):
                    return m+1
                else:
                    l = m + 1
                    
        return m
        