"""
Difficulty:
    Medium

Statement:
    Given an integer array nums and an integer k, return the k most frequent elements within the array.
    The test cases are generated such that the answer is always unique.
    You may return the output in any order.

    n: length of array nums

Constraints:
    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.


Expected time and space complexity:
    Time: O(n)
    Space: O(n)

Examples:
    Example 1:
        Input: nums = [1,2,2,3,3,3], k = 2
        Output: [2,3]
    Example 2:
        Input: nums = [7,7], k = 1
        Output: [7]
"""

from collections import defaultdict
from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def sorting(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n * log n)
        Space: O(n)
        """
        nums_frequency = {}
        for num in nums:
            nums_frequency[num] = nums_frequency.get(num, 0) + 1
        nums_frequency_list = [ item for item in nums_frequency.items() ]
        nums_frequency_list.sort(key = lambda x: x[1])
        result = []
        while(len(result) < k):
            result.append(nums_frequency_list.pop()[0])
        return result

    def minheap(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n * log k)
        Space: O(n + k)
        """
        nums_frequency = {}
        for num in nums:
            nums_frequency[num] = nums_frequency.get(num, 0) + 1
        import heapq
        heap = []
        for num in nums_frequency.keys():
            heapq.heappush(heap, (nums_frequency[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while(len(result) < k):
            result.append(heapq.heappop(heap)[1])
        return result

    def bucketsort(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        nums_frequency = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            nums_frequency[num] = nums_frequency.get(num, 0) + 1

        for num, count in nums_frequency.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if (len(result) == k):
                    return result
        return result
