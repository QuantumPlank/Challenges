"""
Difficulty:
    Easy

Statement:
    You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
    You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
    Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

    n: Length of the array prices

Constraints:    
    1 <= prices.length <= 100
    0 <= prices[i] <= 100

Expected time and space complexity:
    Time: O(x)
    Space: O(y)

Examples:
    Example 1:
        Input: prices = [10,1,5,6,7,1]
        Output: 6
    Example 2:
        Input: prices = [10,8,7,5,2]
        Output: 0

"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def bruteForce(self, prices: List[int]) -> int:
        """
        Time: O(n^2)
        Space: O(1)
        """
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
    
    def twoPointers(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
            else:
                left = right
            right += 1
        return profit

    def slidingWindow(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        profit = 0
        minimal = prices[0]
        for i in range(len(prices)):
            minimal = min(minimal, prices[i])
            profit = max(profit, prices[i] - minimal)
        return profit
