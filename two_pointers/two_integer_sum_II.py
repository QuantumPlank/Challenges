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
        idx1 = 0
        idx2 = 1
        while numbers[idx1] + numbers[idx2] != target:
            idx2 += 1
            if idx2 >= len(numbers):
                idx1 += 1
                idx2 = idx1 + 1
            elif numbers[idx1] + numbers[idx2] > target:
                idx1 += 1
                idx2 = idx1 + 1
        return [idx1 + 1, idx2 + 1]

    ##### INCOMPLETE
