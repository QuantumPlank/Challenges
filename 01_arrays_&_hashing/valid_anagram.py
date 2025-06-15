"""
Difficulty:
    Easy

Statement:
    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    n: length of string s
    m: length of string t

Constraints:
    s and t consist of lowercase English letters.

Expected time and space complexity:
    Time: O(n+m)
    Space: O(1)

Examples:
    Example 1:
        Input: s = "racecar", t = "carrace"
        Output: true
    Example 2:
        Input: s = "jar", t = "jam"
        Output: false
"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def sorting(self, s: str, t: str) -> bool:
        """
        Time: O(n * log n + m * log m)
        Space: O(1) or O(n + m) depending on sorting algorithm
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def hashMap(self, s: str, t: str) -> bool:
        """
        Time: O(n + m)
        Space: O(1)
        """
        if len(s) != len(t):
            return False

        s_count: dict[str, int] = dict()
        t_count: dict[str, int] = dict()

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count
