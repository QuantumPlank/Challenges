"""
Difficulty:
    Easy

Statement:
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    n: length of array nums

Constraints:
    None

Expected time and space complexity:
    Time: O(n)
    Space: O(n)

Examples:
    Example 1:
        Input: nums = [1, 2, 3, 3]
        Output: true
    Example 2:
        Input: nums = [1, 2, 3, 4]
        Output: false
"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, nums: List[int]) -> bool:
        """
        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def sorting(self, nums: List[int]) -> bool:
        """
        Time: O(n * log n)
        Space: O(1) or O(n) depending on sorting algorithm
        """
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def hashSet(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def hashSetLength(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        return len(set(nums)) < len(nums)
