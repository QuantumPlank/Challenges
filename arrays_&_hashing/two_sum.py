"""
Difficulty:
    Easy

Statement:
    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
    You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
    Return the answer with the smaller index first.

    n: length of array nums

Constraints:
    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000

Expected time and space complexity:
    Time: O(n)
    Space: O(n)

Examples:
    Example 1:
        Input: nums = [3,4,5,6], target = 7
        Output: [0,1]

    Example 2:
        Input: nums = [4,5,6], target = 10
        Output: [0,2]

    Example 3:
        Input: nums = [5,5], target = 10
        Output: [0,1]
"""


class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(n^2)
        Space: O(n)
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def sorting(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(n * log n)
        Space: O(1) or O(n + m) depending on sorting algorithm
        """
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort(key=lambda x: x[0])

        i = 0
        j = len(nums) - 1

        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            if curr < target:
                i += 1
            else:
                j -= 1
        return []

    def hashMap(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O()
        Space: O()
        """
        prevMap: dict[int, int] = dict()
        for i, num in enumerate(nums):
            prevMap[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [i, prevMap[diff]]
        return []
