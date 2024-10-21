# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # make a dummy node with value 0
        dummyhead = ListNode(0)
        curr = dummyhead
        # dummyhead and curr are both pointing to same node. We will keep iterating current while keeping dummyhead static to return dummyhead

        carry = 0

        while l1 or l2 or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            summ = a + b + carry
            carry = summ / 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummyhead.next