"""
Contains Duplicate
Grind 75 #25
LC #217 Easy
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        """
        Set Solution
        Time O(n)
        Space O(n)
        Potential to use less space than hash, but only as we approach n
        """
        
        return len(nums) > len(set(nums))
        
        
        
        """
        Hashmap solution
        Time O(n)
        Space O(n)
        Potential to use less space/time than set, but only if we find
        duplicate and terminate early
        """
        hashed = {}
        for i in nums:
            if i in hashed:
                return True
            else:
                dic[i] = 1
        
        return False
