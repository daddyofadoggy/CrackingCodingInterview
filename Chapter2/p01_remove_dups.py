#https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter


class Solution(object):
    def remove_element(self, head, value):
        current_node = head
        if current_node.val == value:
            head = head.next
            return
        while current_node.next.val != value:
            current_node = current_node.next
        current_node.next = current_node.next.next

    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cnt = Counter()
        ## check duplicate elements
        dummy = ListNode(-1, head)
        currentnode = head
        current = dummy.next
        prev = dummy
        while currentnode:
            cnt[currentnode.val] += 1
            currentnode = currentnode.next
        while current:
            if cnt[current.val] > 1:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy.next



