"""
Middle of the Linked List 
Grind 75 #23
LC #876

Solution 
time complexity = O(n) -- really closer to O(n/2), but grows exactly proportionally to n
space complexity = O(1) constant space

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # need to find middle node in linked list
        # if two middle nodes (i.e. even number of nodes), return second middle node
        # need some way to store locations of passed nodes as we traverse and count all nodes
        # we are NOT given the count of nodes
        
        # we will use a runner node to progress through 2 nodes at a time
        # this will allow us to find middle node in half the time
        runner = head
        
        # while the runner node has a next node, always progress the head/walker node
        # if the runner also has a next.next node, move the runner forward two nodes
        # when either the while or if condition breaks, we have found the middle node
        # break loop if needed and return head once complete
        while runner and runner.next:
            head = head.next
            runner = runner.next.next
        
        return head
               
        
        """
        # brute force
        # store head node in new variable
        # traverse full list
        # with stored variable, traverse again to halfway point
        # time complexity = O(nlogn)? O(1.5n)?
        # space complexity = O(1) -- constant space
        # similar alternative using stack, would require more space
        
        # with constraints, always at least one node in linked list
        # counter will represent number of times we need to move to next node to find middle
        dummy = head
        counter = 0
        head = head.next
        
        while head:
            counter += 1
            head = head.next
            
        if counter % 2 == 0:
            counter = counter // 2
        else:
            counter = (counter // 2) + 1
        
        for i in range(0, counter):
            dummy = dummy.next
            
        return dummy
        """
            
            
     