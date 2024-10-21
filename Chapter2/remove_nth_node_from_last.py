#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        dummy.next = head
        runner = dummy
        follower = dummy
        # prev = None
        count = 0
        while runner.next:
            if count >= (n):
                follower = follower.next
            count = count + 1
            runner = runner.next
        # print(follower.val)
        follower.next = follower.next.next
        return dummy.next

