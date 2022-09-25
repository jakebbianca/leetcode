"""
Valid Parentheses
Grind75 #2
LeetCode #20 Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

class Solution(object):
    def isValid(self, s):
        
        # if number of characters is odd, always return False
        if len(s) %2 != 0:
            return False
        
        # define sets for characters and matches we will check for
        # initialize the stack
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []
        
        # if we find an open bracket, add it to the stack
        # if we don't and thus find a closing bracket...
        # ...and stack is empty (no match)...
        # ...or stack.pop() returns a different opening bracket (no match)...
        # ... return false
        # otherwise, continue until finished iterating through the string
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open, bracket) not in  matches:
                    return False
        
        # if any unclosed open brackets remain in stack, return false
        # if stack empty and all pairs closed in order, return True
        return len(stack) == 0