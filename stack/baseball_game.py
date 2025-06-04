"""
Difficulty:
    Easy

Statement:
    You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

    Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

        An integer x: Record a new score of x.

        '+': Record a new score that is the sum of the previous two scores.

        'D': Record a new score that is the double of the previous score.

        'C': Invalidate the previous score, removing it from the record.

    Return the sum of all the scores on the record after applying all the operations.

    Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

    n: length of the list operations

Constraints:    
    1 <= operations.length <= 1000
    operations[i] is "C", "D", +, or a string representing an integer in the range [(-30,000), (30,000)].
    For operation "+", there will always be at least two previous scores on the record.
    For operations "C" and "D", there will always be at least one previous score on the record.

Expected time and space complexity:
    Time: O(x)
    Space: O(y)

Examples:
    Example 1:
        Input: ops = ["1","2","+","C","5","D"]
        Output: 18
    Example 2:
        Input: ops = ["5","D","+","C"]
        Output: 15
"""

from typing import List

class Solution:
    def __init__(self) -> None:
        pass

    def stack(self, operations: List[str]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(record[-1] + record[-2])
            elif operations[i] == 'D':
                record.append(record[-1] * 2)
            elif operations[i] =='C':
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
