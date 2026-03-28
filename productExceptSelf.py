# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        
        # pref
        for i in range(n):
            if i == 0:
                continue
            pref[i] = pref[i-1] * nums[i-1]
        
        # suf
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            suf[i] = suf[i+1] * nums[i+1]
            
        res = [0] * n
        for i in range(0, n):
            res[i] = pref[i] * suf[i]
                
        return res

sol = Solution()
print("final =", sol.productExceptSelf([4,5,1,8,2]))