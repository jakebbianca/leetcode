"""
Invert Binary Tree
Grind 75 #6
LC #226 Easy

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

            4                    4                                  
          /   \                /   \                          
        2       7   BECOMES   7      2                                        
      /  \     / \          /  \    /  \                                                      
     1    3   6   9        3    1  6    9                                                 


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

Solution:
time complexity = O(n) => need to iterate through each node
space complexity = O(1) => only additional variable required is a single temp node
"""