#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None

        follower, runner = head, head.next.next

        while runner and runner.next:
            runner = runner.next.next
            follower = follower.next

        # When 'runner' reaches the end, remove the next node of 'follower' and return 'head'.
        follower.next = follower.next.next

        return head

