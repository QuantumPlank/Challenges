"""
Difficulty:
    Easy

Statement:
    Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

    Implement the following methods:
        - constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
        - int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Constraints:    
    1 <= k <= 1000
    0 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -1000 <= val <= 1000
    There will always be at least k integers in the stream when you search for the kth integer.

Expected time and space complexity:
    Time: O(x)
    Space: O(y)

Examples:
    Example 1:
        Input: ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
        Output: [null, 3, 3, 3, 5, 6]
"""
from typing import List
import heapq

class Sorting:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.largests_integers = nums.copy()

    def add(self, val: int) -> int:
        self.largests_integers.append(val)
        self.largests_integers.sort()
        return self.largests_integers[-self.k]

        

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums.copy()
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
        
