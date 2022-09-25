"""
Clone Graph
Grind 75 #31
LC #133 Medium


Time - O(v*e) -- will visit all nodes, and all neighbors even if already visited
Space - O(v)
"""





# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
Same idea as my original solution but done better
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        q = deque([node])
        clones = {node.val: Node(node.val, [])}
        
        while q:
            
            # cur is node from original graph
            # cur_clone is clone of cur that we are working on
            cur = q.popleft()
            cur_clone = clones[cur.val]
            
            for neighbor in cur.neighbors:
                # create a clone for each neighbor that has not already been cloned
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                # for each neighbor, append cloned neighbor to current clone
                cur_clone.neighbors.append(clones[neighbor.val])
        
        return clones[node.val]
        
"""
THIS PASSED FIRST TRY
CAN WE MAKE IT BETTER?

        
        # if n nodes, base case if n = 0
        if not node:
            return None
        

        visited = set()        # tool to keep track of visited nodes using unique node vals
        clones = {}            # dict to keep references to clones made, using unique node vals
        
        # clone the given node, add val to set and clone to dict
        cloneRoot = Node(node.val, node.neighbors)
        
        visited.add(node.val)
        clones[cloneRoot.val] = cloneRoot
        
        
        # generate stack to iterate through neighbors as we progress through graph
        stack = []
        
        # for each neighbor of CLONED root node
        # make deep copy of neighbor nodes
        # add deep copies to dict
        # update neighbor from original to clone
        # append neighbors to stack (since this is root, all are unvisited)
        # iterating through neighbors of CLONED root so that we update neighbors in CLONED graph 
        if len(node.neighbors) > 0:
            for neighbor in cloneRoot.neighbors:
                cloneTemp = Node(neighbor.val, neighbor.neighbors)
                clones[neighbor.val] = cloneTemp
                neighbor = cloneTemp
                stack.append(cloneTemp)
                
        
        # run through neighbors
        while len(stack) > 0:
            
            # get node from top of stack
            cur = stack.pop()
            
            # if we have already visited this node, do not repeat process
            if cur.val in visited:
                continue
                
            # otherwise, add node val to visited set
            
            else:
                visited.add(cur.val)
                for neighbor in cur.neighbors:
                    # if we already have a clone, update neighbors in list with clone
                    # if we haven't already cloned a neighbor, clone update dict
                    if neighbor.val in clones:
                        neighbor = clones[neighbor.val]
                    else:
                        cloneTemp = copy.deepcopy(neighbor)
                        clones[neighbor.val] = cloneTemp
                        neighbor = cloneTemp
                    # if we haven't already visited a neighbor, add to stack
                    if neighbor.val not in visited:
                        stack.append(neighbor)
                        
        # return deep copy of root node
        return cloneRoot
"""