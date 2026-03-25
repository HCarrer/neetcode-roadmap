# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		hashS = {}
		hashT = {}
		if len(s) != len(t):
			return False

		for i, subS in enumerate(s):
			if subS in hashS:
				hashS[subS] += 1
			else:
				hashS[subS] = 1

		for i, subT in enumerate(t):
			if subT in hashT:
				hashT[subT] += 1
			else:
				hashT[subT] = 1
				
		for key in hashS:
			if hashS.get(key) != hashT.get(key):
				return False
		return True
			
sol = Solution()
print(sol.isAnagram("racecasr", "carrace"))