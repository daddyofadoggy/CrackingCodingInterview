# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/editorial/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def constructbst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            n = TreeNode(nums[mid])
            n.left = constructbst(left, mid - 1)
            n.right = constructbst(mid + 1, right)
            return n

        return constructbst(0, len(nums) - 1)