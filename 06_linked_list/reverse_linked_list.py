"""
Difficulty:
    Easy

Statement:
    Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

    n: size of the list

Constraints:
    0 <= The length of the list <= 1000.
    -1000 <= Node.val <= 1000


Expected time and space complexity:
    Time: O(n)
    Space: O(1)

Examples:
    Example 1:
        Input: head = [0,1,2,3]
        Output: [3,2,1,0]
    Example 2:
        Input: head = []
        Output: []

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def __init__(self) -> None:
        pass

    def linkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        current = head
        previous = None
        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        return previous
