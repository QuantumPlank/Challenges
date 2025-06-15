"""
Difficulty:
    Medium

Statement:
    Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
    A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
    You must write an algorithm that runs in O(n) time.
    n: length of nums array

Constraints:    
    0 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9


Expected time and space complexity:
    Time: O(n)
    Space: O(n)

Examples:
    Example 1:
        Input: nums = [2,20,4,10,3,4,5]
        Output: 4

    Example 2:
        Input: nums = [0,3,2,5,4,6,1,1]
        Output: 7

"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def sorting(self, nums: List[int]) -> int:
        """
        Time: O(n * log n)
        Space: O(n)
        """
        if nums == []:
            return 0
        sorted_nums = sorted(nums)
        longest_sequence = 1
        streak = 1
        for idx in range(len(sorted_nums) - 1):
            if sorted_nums[idx] == sorted_nums[idx + 1]:
                continue
            if sorted_nums[idx] + 1 == sorted_nums[idx + 1]:
                streak += 1
            else:
                streak = 1
            if streak > longest_sequence:
                longest_sequence = streak
        return longest_sequence

    def hashset(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        if nums == []:
            return 0
        nums_set = set(nums)
        
        longest_sequence = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1
                seeker = num + 1
                while seeker in nums_set:
                    streak += 1
                    seeker += 1
                longest_sequence = max(longest_sequence, streak)
        return longest_sequence

