"""
Flood Fill
Grind 75 #9
LC #733 Easy

Solution:
time complexity is O(nm)?? -- potential to visit each set of vertices
space complexity is O(1) -- do not need to store data with any variable relationship
"""


from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # get number of rows and columns
        rows = len(image)
        cols = len(image[0])
        # store original color int in a variable for reuse
        startColor = image[sr][sc]
        
        # helper depth-first search function
        def dfs(row, col):
            # check that row and column indices are within bounds
            # check that we have not already traversed this pixel
            # check that the pixel color matches the start pixel color
            if row < 0 or col < 0 or row > rows-1 or col > cols-1 or image[row][col] == newColor or image[row][col] != startColor:
                return
            
            # update color of current pixel
            image[row][col] = newColor
            # repeat dfs 4-directionally from current pixel
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        
        # start dfs from starting row/col
        dfs(sr, sc)
        # return updated image
        return image

"""
Below solution is good, but can be made more efficient by not relying on
a hashset/tracking coordinates we have already traversed


def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


    # define helper function
    # check validity of image coordinates/indices
    # check if we have already visited a given pair of indices
    # check if current indices hold value of starting pixel color
    # if we pass all three checks, add indices as tuple to hashset,
    # update the color and repeat 4-directionally
    def floodFillHelper(image, row, col, newColor, startColor, hashset) -> None:
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]): return
        if (row, col) in hashset: return
        if image[row][col] == startColor:
            image[row][col] = newColor
            hashset.add((row, col))
            floodFillHelper(image, row-1, col, newColor, startColor, hashset)
            floodFillHelper(image, row+1, col, newColor, startColor, hashset)
            floodFillHelper(image, row, col-1, newColor, startColor, hashset)
            floodFillHelper(image, row, col+1, newColor, startColor, hashset)
            
    # create a blank set that we will hash
    hashset = set()
    
    # run recursive helper function with starting indices
    floodFillHelper(image, sr, sc, color, image[sr][sc], hashset)
    
    return image
"""