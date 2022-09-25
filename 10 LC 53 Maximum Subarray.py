"""
Maximum Subarray
Grind75 #10
LC # 53 Medium

Solution:
time complexity O(n) - iterate through entire list once
space complexity = O(1) - only additional space used for two integer sums
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # iterate through list, with cumulative sums starting as first item
        # update the running sum on one hand
        # update maxSum if exceeded by running sum on the other
        # return the maxSum once complete
        # more concise version of solution below
        curSum = maxSum = nums
        for num in nums[1:]:
            curSum = max(curSum, 0) + num
            maxSum = max(maxSum, curSum)
            
        return maxSum
    
"""
This solution is good, but can be done even more efficiently in Python


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        maxSum = nums[0]
        carry = nums[0]
        r = 1
        
        while r < len(nums):
            # if carry sum is negative or 0
            # update max sum if greater
            # update new carry to current num at index r
            # update l index to current r index
            if carry <= 0:
                carry = nums[r]
            # if carry is positive
            # add nums[r] to carry if also positive
            # update maxSum if current carry > prev maxSum
            else:
                carry += nums[r]
            # if carry > maxSum after any updates, update maxSum
            if carry > maxSum:
                maxSum = carry
            # always increment pointer to move through list
            r += 1
            
        return maxSum
"""