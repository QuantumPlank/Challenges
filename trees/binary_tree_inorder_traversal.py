"""
Difficulty:
    Easy

Statement:
    You are given the root of a binary tree, return the inorder traversal of its nodes' values.

    n: number of nodes in the tree

Constraints:    
    0 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100


Expected time and space complexity:
    Time: O(n)
    Space: O(1)

Examples:
    Example 1:
        Input: root = [1,2,3,null,4,5,null]
        Output: [2,4,1,5,3]
    Example 2:
        Input: root = []
        Output: []

"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        pass

    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = []
        result = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = []
        result = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

