"""
Valid Anagram
Grind 75 #7
LC # 242 Easy
Multiple Solutions available
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # anagrams must have the same number of characters
        if len(s) != len(t): return False
        
        # more explicit version of counter solution
        # may save a bit of time over counter
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True
        
        
        """
        # This is probably the most 'pythonic' way to solve this problem
        # Time and space complexity are great and code is very simple/abstracted/readable
        
        # Counter is a subclass of dict
        # operation below creates a dict for each string
        # these dicts will have each character found as key
        # matching values will be count of occurrences
        # if they are equal for two strings, you have confirmed anagrams
        return Counter(s) == Counter(t)
        """

        """
        # This xor attempt does NOT work
        # This attempt relies on commutative/associative properties of xor
        # Fails if the two strings have even numbers of the same letters, regardless of anagram status
        # Example: if s = "aa" and t = "bb", xor will be 0 based on below
        
        # perform xor check for all 
        xor = 0
        for i in range(0, len(s)):
            xor = xor ^ ord(s[i]) ^ ord(t[i])
            
        if xor == 0:
            return True
        else:
            return False
        """