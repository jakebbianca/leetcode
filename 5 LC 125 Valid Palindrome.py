"""
Valid Palindrome
Grind 75 #5
LC #125 Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. 
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        # restructure string s
        # remove non-alphanumeric characters
        # make all alphabetical characters lowercase
        s = ''.join(ch for ch in s if ch.isalnum()).lower()
        
        # check if character at index i is same as at index (-i-1)
        # only need to check up to midway point
        # can exclude median character if len(s) is odd
        for i in range(0, len(s)//2):
            if s[i] != s[-i-1]: return False

        # if all comparisons pass, characters form a palindrome
        return True