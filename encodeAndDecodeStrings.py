# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: dummy_input = ["Hello","World"]

# Output: ["Hello","World"]

# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);

from typing import List

DELIMITER = ">"

class Solution:
    # ["Hello","Magical","Wonderful","World"] -> "5>Hello7>Magical>9Wonderful5>World"
    def encode(self, strs: List[str]) -> str:        
        res = ""
        for s in strs:
            res += str(len(s)) + DELIMITER + s
        return res
    
    # "5>Hello7>Magical>9Wonderful5>World" -> ["Hello","Magical","Wonderful","World"]
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        index = 0
        while index < len(s):
            lengthStringIndex = index
            while s[lengthStringIndex] != DELIMITER:
                lengthStringIndex += 1
            length = int(s[index:lengthStringIndex])
            index = lengthStringIndex + 1
            lengthStringIndex = index + length
            word = str(s[index:lengthStringIndex])
            res.append(word)
            index = lengthStringIndex
                
        return res
                

sol = Solution()
encoded = sol.encode(["we","say",":","yes","!@#$%^&*()"])
print(sol.decode(encoded))