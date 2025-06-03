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
        result = 0
        
        count = {}
        left = 0
        maxFrequency = 0

        for right in range(len(s)):
            character = s[right]
            count[character] = count.get(character, 0) + 1
            maxFrequency = max(maxFrequency, count[character])

            while (right - left + 1) - maxFrequency > k:
                character = s[left]
                count[character] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result

