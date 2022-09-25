"""
Merge Two Sorted Lists
Grind 75 #3
LeetCode #21 Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order

Solution:
time complexity = O(n) => based on number of nodes in the lists to be merged
space complexity = O(1) => we only create a single new node and point at existing nodes from there
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create new empty list node to begin building new sorted list
        # create dummy pointer to same node so we retain pointer to this beginning point
        head = dummy = ListNode()
        
        # check lowest val between current list1 and list2 nodes
        # assign next node in merged list to node with lower val and move along
        # if vals are equal, default to list1 (could do same with list2)
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            
        # when one list is exhausted, only add nodes from other list in order
        # do this until both lists are exhausted
        while list1 or list2:
            if list1 and not list2:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
            
        # return node pointed to by our dummy head pointer
        # root of merged list is actually blank, so we want to start at next node
        # this next node is the first we've added to the merged list
        return dummy.next