"""
Difficulty:
    Easy

Statement:
    Given a string s, return true if it is a palindrome, otherwise return false.
    A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
    
    n : length of the string s

Constraints:    
    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.


Expected time and space complexity:
    Time: O(n)
    Space: O(1)

Examples:
    Example 1:
        Input: s = "Was it a car or a cat I saw?"
        Output: true

    Example 1:
        Input: s = "tab a cat"
        Output: false

"""


class Solution:
    def __init__(self) -> None:
        pass
    
    def reversed(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        cleaned_s = ""
        for c in s:
            if str.isalnum(c):
                cleaned_s += c.lower()
        return cleaned_s == reversed(cleaned_s)


    def twoPointers_NonOptimal(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        cleaned_s = ""
        for c in s:
            if str.isalnum(c):
                cleaned_s += c.lower()
        s = cleaned_s
        for idx in range(len(s) // 2):
            if s[idx] != s[-idx-1]:
                return False
        return True

    def twoPointer_Optimal(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """
        frontIdx = 0
        backIdx = len(s) - 1
        while frontIdx < backIdx:
            while frontIdx < backIdx and not str.isalnum(s[frontIdx]):
                frontIdx += 1
            while frontIdx < backIdx and not str.isalnum(s[backIdx]):
                backIdx -= 1
            if s[frontIdx].lower() != s[backIdx].lower():
                return False
            frontIdx += 1
            backIdx -= 1
        return True
