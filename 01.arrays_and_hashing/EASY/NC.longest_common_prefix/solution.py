from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            character = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != character:
                    return strs[0][:i]
        return strs[0]