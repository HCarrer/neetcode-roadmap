# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

from typing import List


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		freq = [[] for i in range(len(nums) + 1)]
		count = {}
		for num in nums:
			if num in count:
				count[num] += 1
			else:
				count[num] = 1
		
		for index, c in count.items():
			freq[c].append(index)
   
		res = []
		for i in range(len(freq) - 1, 0, -1):
			for n in freq[i]:
				res.append(n)
				if len(res) == k:
					return res
	
	
sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
print(sol.topKFrequent([1,1,1,2,2,100, 100], 2))