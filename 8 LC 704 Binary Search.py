"""
Binary Search
Grind 75 #8
LC # 704 Easy


Solution:
time complexity O(logn)
space complexity O(1)
"""



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # assign variables to indices that include range of ALL possible answers
        low = 0
        high = len(nums) - 1
        
        # if low is ever > high, the target is outside of the bounds of our nums list
        while low <= high:
            
            # mid will be higher mid point between low and high
            # if nums[mid] ever == target, return mid
            # if target > nums[mid], new minimum possible answer must be at index > mid, so new low = mid + 1
            # opposite holds true for target < nums[mid]
            mid = low + (high - low + 1) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1