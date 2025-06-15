"""
Difficulty:
    Medium

Statement:
    Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    n: length of array strs
    m: length of the longest string

Constraints:
    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.

Expected time and space complexity:
    Time: O(n * m)
    Space: O(n)

Examples:
    Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    Example 2:
        Input: strs = ["x"]
        Output: [["x"]]

    Example 3:
        Input: strs = [""]
        Output: [[""]]


"""


from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, strs: list[str]) -> list[list[str]]:
        """
        Time: O(n^2 * m)
        Space: O(n * m)
        """
        groups = []

        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            s_count: dict[str, int] = dict()
            t_count: dict[str, int] = dict()

            for i in range(len(s)):
                s_count[s[i]] = s_count.get(s[i], 0) + 1
                t_count[t[i]] = t_count.get(t[i], 0) + 1

            return s_count == t_count

        for string in strs:
            for group in groups:
                if isAnagram(string, group[0]):
                    group.append(string)
                    break
            else:
                groups.append([string])
        return groups

    def sorted(self, strs: list[str]) -> list[list[str]]:
        """
        Time: O(n * m * log m)
        Space: O(n)
        """
        from collections import defaultdict
        groups: dict[str, list[str]] = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string))
            groups[sorted_string].append(string)

        return list(groups.values())

    def hashTable(self, strs: list[str]) -> list[list[str]]:
        """
        Time: O(n * m)
        Space: O(n * m)
        """
        res = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())
