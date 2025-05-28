"""
Difficulty:
    Medium

Statement:
    You are given an integer array heights where heights[i] represents the height of the ith bar
    You may choose any two bars to form a container. Return the maximum amount of water a container can store.

    n: length of the array heights

Constraints:
    2 <= height.length <= 1000
    0 <= height[i] <= 1000


Expected time and space complexity:
    Time: O(n)
    Space: O(1)

Examples:
    Example 1:
        Input: height = [1,7,2,5,4,7,3,6]
        Output: 36

    Example 2:
        Input: height = [2,2,2]
        Output: 4
"""
from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                container = min(heights[i], heights[j]) * (j - i)
                result = max(result, container)
        return result

    def twoPointers(self, heights: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        result = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            capacity = min(heights[left], heights[right]) * (right - left)
            result = max(result, capacity)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
