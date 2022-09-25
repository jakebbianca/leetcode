"""
K Closest Points to Origin
Grind 75 #28
LC #973 Medium

Time complexity: O(Nlogk)
Space complexity: O(k)
"""


import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                # heappushpop removes SMALLEST item, which is why we negated dist
                # heap[0] will be furthest point (biggest negative)
                # heap[0][0] accesses the negative distance of that point
                # push adds item to heap, pop removes smallest item from heap,
                # so pushpop more efficiently adds new item and removes other item at once
                heapq.heappushpop(heap, (dist, i))
        
        # Return all points stored in the max heap
        # only want to return list of lists of points, hence (_, i)
        # in this case, _ is fill in for dists held in heap
        return [points[i] for (_, i) in heap]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2