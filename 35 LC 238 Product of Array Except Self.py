class Solution:
    def productExceptSelf(self, nums):
        
        """
        Optimized Solution
        Time - O(n)
        Space - O(1) excluding return array, per specification
        
        Intuition:
        Essentially, have two pointers (i and -1-i) and traverse the nums array in both directions at once
        Build prefix and suffix products as you go
        Will eventually multiply all nums by both their prefix and suffix products
        This will be correct answer for each num since multiplication is commutative/associative
        """
        
        ans = [1]*len(nums)
        suf = 1
        pre = 1
        
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
            
        return ans
        
        """
        Suffix product solution
        Basically, go up and down the array to build sums
        O(2n) ~ O(n) time
        O(n) space
        """
        """
        
        n = len(nums)
        ans = [1]*n
        suffix_prod = 1
        
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
            
        for i in range(n-1,-1,-1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
            
        return ans
        """


        """
        This will return correct answer eventually, but is NOT O(n) time
        Exceeds time limit of leetcode submission
        """
        """
        res = [1]*len(nums)
        
        for i in range(0, len(nums)):
            lprod = math.prod(nums[0:i]) if i > 0 else 1
            rprod = math.prod(nums[i+1:len(nums)]) if i < len(nums) - 1 else 1
            res[i] = lprod * rprod
            
        return res
        """