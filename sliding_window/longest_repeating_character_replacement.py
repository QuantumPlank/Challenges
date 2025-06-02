"""
Difficulty:
    Medium

Statement:
    You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
    n: length of string s


Constraints:    
    1 <= s.length <= 1000
    0 <= k <= s.length

Expected time and space complexity:
    Time: O(n)
    Space: O(m)

Examples:
    Example 1:
        Input: s = "XYYX", k = 2
        Output: 4
    Example 2:
        Input: s = "AAABABB", k = 1
        Output: 5

"""


class Solution:
    def __init__(self) -> None:
        pass

    def slidingWindow(self, s: str, k: int) -> int:
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

    def slidingWindow(self, s: str, k: int) -> int:
        """
        Time: O(n)
        Space: O(m)
        """
        left = 0
        result = 0
        right = 0
        while right < len(s):
            run_k = k
            character = s[left]
            right = left + 1
            run_result = 1
            incidence = -1
            while run_k >= 0 and right < len(s):
                if s[right] == character:
                    run_result += 1
                else:
                    run_k -= 1
                    if incidence == -1:
                        incidence = right
            result = max(result, run_result)
        return result