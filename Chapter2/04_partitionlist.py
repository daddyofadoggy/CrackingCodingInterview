https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        leftdummy, rightdummy = ListNode(-1), ListNode(-1)
        ltail, rtail = leftdummy, rightdummy

        while head:
            if head.val<x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = rightdummy.next
        rtail.next = None
        return leftdummy.next