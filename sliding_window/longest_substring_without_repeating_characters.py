"""
Difficulty:
    Medium

Statement:
    Given a string s, find the length of the longest substring without duplicate characters.
    A substring is a contiguous sequence of characters within a string.
    
    n: length of the string s
    m: unique characters in the string

Constraints:    
    0 <= s.length <= 1000
    s may consist of printable ASCII characters.

Expected time and space complexity:
    Time: O(n)
    Space: O(m)

Examples:
    Example 1:
        Input: s = "zxyzxyz"
        Output: 3
    Example 2:
        Input: s = "xxxx"
        Output: 1

"""


class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, s: str) -> int:
        """
        Time: O(n*m)
        Space: O(m)
        """
        result = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            result = max(result, len(charSet))
        return result

    def slidingWindow(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(m)
        """
        charMap = {}
        left = 0
        result = 0
        for right in range(len(s)):
            character = s[right]
            if character in charMap:
                left = max(charMap[character]+1, left)
            charMap[character] = right
            result = max(result, right - left + 1)
        return result



