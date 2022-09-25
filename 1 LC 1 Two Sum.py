
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
"""
# hash map solution
# time complexity: O(n)
# space complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 2: return [0,1]
        return self.twoSumHashMethod(nums, target)

    def twoSumHashMethod(self, nums, target):
        Hashmap = {}
        for index, value in enumerate(nums):
            key = target - value
            if key in Hashmap:
                return [Hashmap[key], index]
            else:
                Hashmap[value] = index

ans = Solution()
print(ans.twoSum(nums=[2,7,11,15], target=9))

