"""
Difficulty:
    Medium

Statement:
    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
    Please implement encode and decode

    m: sum of lengths of all the strings
    n: number of strings

Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.


Expected time and space complexity:
    Time: O(m)
    Space: O(m+n)

Examples:
    Example 1:
        Input: ["neet","code","love","you"]
        Output:["neet","code","love","you"]
    Example 2:
        Input: ["we","say",":","yes"]
        Output: ["we","say",":","yes"]
"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def brute(self):
        """
        Time: O(m)
        Space: O(m+n)
        """
        def encode(strs: List[str]) -> str:
            if not strs:
                return ""
            sizes, res = [], ""
            for s in strs:
                sizes.append(sizes)
            for sz in sizes:
                res += str(sz)
                res += ','
            res += '#'
            for s in strs:
                res += s
            return res

        def decode(s: str) -> List[str]:
            if not s:
                return []
            sizes, res, i = [], [], 0
            while s[i] != '#':
                cur = ""
                while s[i] != ',':
                    cur += s[i]
                    i += 1
                sizes.append(int(cur))
                i += 1
            i += 1
            for sz in sizes:
                res.append(s[i:i + sz])
                i += sz
            return res

    def optimal(self):
        """
        Time: O(m)
        Space: O(m+n)
        """
        def encode(strs: List[str]) -> str:
            res = ""
            for s in strs:
                res += str(len(s)) + "#" + s
            return res

        def decode(s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                curr = ""
                while s[i] != "#":
                    curr += s[i]
                    i += 1
                i += 1
                sz = int(curr)
                word = s[i:i+sz]
                res.append(word)
                i += sz
            return res
