"""
Difficulty:
    Medium

Statement:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
    The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
    
    n: length of the array nums
    m: number of triplets in array nums

Constraints:
    3 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5


Expected time and space complexity:
    Time: O(n^2)
    Space: O(1)

Examples:
    Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

    Example 2:
        Input: nums = [0,1,1]
        Output: []

    Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]

"""
from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^3)
        Space: O(m)
        """
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple([nums[i], nums[j], nums[k]]))
        result = [list(i) for i in result]
        return result

    def hashMap(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^2)
        Space: O(n)
        """
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res

    def twoPointers(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^2)
        Space: O(1)
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result