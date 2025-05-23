"""
Difficulty:
    Medium

Statement:
    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
    Each product is guaranteed to fit in a 32-bit integer.
    Follow-up: Could you solve it in O(n) time without using the division operation?

    n: length of the nums array

Constraints:    
    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20


Expected time and space complexity:
    Time: O(x)
    Space: O(y)

Examples:
    Example 1:
        Input: nums = [1,2,4,6]
        Output: [48,24,12,8]

    Example 2:
        Input: nums = [-1,0,1,2,3]
        Output: [0,-6,0,0,0]

"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, nums: List[int]) -> List[int]:
        """
        Time: O(n^2)
        Space: O(n)
        """
        result = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                total *= nums[j]
            result.append(total)

        return result
    
    def division(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        prod, zeros = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1
        
        if zeros > 1:
            return [0] * len(nums)

        result = []
        for idx, num in enumerate(nums):
            if zeros == 1:
                if num == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(prod // num)
        return result

    def preffixandsuffix(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i] 
        return res