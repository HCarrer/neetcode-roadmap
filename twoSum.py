# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashTable:
                returnArr = [hashTable[diff], i]
            hashTable[n] = i
        
        return [returnArr[0], returnArr[1]] if returnArr[0] < returnArr[1] else [returnArr[1], returnArr[0]]