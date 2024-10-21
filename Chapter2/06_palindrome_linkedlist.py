# https://leetcode.com/problems/palindrome-linked-list/editorial/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.slowrunner = head
        def recur_palindrome(currentnode=head):
            if currentnode is not None:
                if not recur_palindrome(currentnode.next):
                    return False
                if currentnode.val != self.slowrunner.val:
                    return False
                self.slowrunner = self.slowrunner.next
            return True
        return recur_palindrome()