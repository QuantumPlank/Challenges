"""
Difficulty:
    Medium

Statement:
    Given an array of integers numbers that is sorted in non-decreasing order.
    Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
    There will always be exactly one valid solution.
    Your solution must use O(1)O(1) additional space.

Constraints:    
    2 <= numbers.length <= 1000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000


Expected time and space complexity:
    Time: O(x)
    Space: O(y)

Examples:
    Example 1:
        Input: numbers = [1,2,3,4], target = 3
        Output: [1,2]
"""
from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
    def binarySearch(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n * log n)
        Space: O(1)
        """
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            searched = target - numbers[i]
            while left <= right:
                middle = left + (right - left) // 2
                if numbers[middle] == searched:
                    return [i + 1, middle + 1]
                elif numbers[middle] < searched:
                    left = middle + 1
                else:
                    right = middle - 1
        return []
    
    def hashMap(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        seen = {}
        for i in range(len(numbers)):
            searched = target - numbers[i]
            if seen.get(searched, 0):
                return [seen[searched], i + 1]
            seen[numbers[i]] = i + 1
        return []

    def twoPointers(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left
            else:
                return[left + 1, right + 1]
        return []