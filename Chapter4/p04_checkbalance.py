# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root):
        if root is None:
            return -1
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh)>1:
            return -99
        else:
            return 1+max(lh, rh)
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.height(root) != -99