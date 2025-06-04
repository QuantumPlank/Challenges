"""
Difficulty:
    Easy

Statement:
    You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
    Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
    Your solution must run in O(log n) time.

    n: length of array nums

Constraints:
    1 <= nums.length <= 10000.
    -10000 < nums[i], target < 10000


Expected time and space complexity:
    Time: O(log n)
    Space: O(1)

Examples:
    Example n:
        Input: x
        Output: y
    Example m:
        Input: x
        Output: y
"""
from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def solution(self, nums: List[int], target: int) -> int:
        """
        Time: O(log n)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
