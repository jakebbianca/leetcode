from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # create a de-queue and fill with all coordinates of zeroes in input matrix
        # if we find a non-zero number, change matrix to -1 to mark as unrecorded
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        
        # iterate through each set of coordinates in the queue
        # compare against adjacent cells, update adjacent cells if possible
        # if cell is updated, add cell coordinates to queue
        # this is how we will find and update cells more than one cell distance from a zero
        while q:
            x, y = q.popleft()
            for row, col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x2, y2 = x+row, y+col
                if 0 <= x2 < len(mat) and 0 <= y2 < len(mat[0]) and mat[x2][y2] == -1:
                    mat[x2][y2] = mat[x][y] + 1
                    q.append((x2, y2))
        
        return mat

ans = Solution()

ans.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])