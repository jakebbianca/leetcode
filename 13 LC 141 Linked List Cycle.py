"""
Linked List Cycle
Grind 75 #13
LC #141 Easy

Solution:
time complexity at worst ~O(2n) ~ O(n)
space complexity O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        if not head: return False

        # traverse the list with two separate nodes at a time
        # one goes twice as fast as the other
        # if there is a cycle, the runner will eventually catch the walker
        # if that ever happens, return True
        # if not, there's no cycle, confirmed once runner no longer exists
        walker = head
        runner = head

        while runner.next and runner.next.next:
            runner = runner.next.next
            walker = walker.next
            if walker == runner:
                return True

        return False
        