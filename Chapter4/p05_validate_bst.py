# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.previous = float('-inf')
        self.flag = 0

    def inorder(self, root):
        if root is None:
            return
        self.isValidBST(root.left)
        if root.val <= self.previous:
            self.flag = 1
        self.previous = root.val
        self.isValidBST(root.right)

    def isValidBST(self, root):
        self.inorder(root)
        return self.flag == 0


