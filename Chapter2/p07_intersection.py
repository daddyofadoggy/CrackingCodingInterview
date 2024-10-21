# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        currentA = headA
        while currentA:
            s.add(currentA)
            currentA = currentA.next

        currentB = headB
        while currentB:
            if currentB in s:
                return currentB
            currentB = currentB.next
        return None