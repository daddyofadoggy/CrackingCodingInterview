# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        string1 = []
        string2 = []
        def getStringfromTree(node, strr):
            if node is None:
                strr.append('X')
                return
            strr.append(" "+str(node.val)+" ")
            getStringfromTree(node.left, strr)
            getStringfromTree(node.right, strr)
        getStringfromTree(root, string1)
        getStringfromTree(subRoot, string2)
        string = "".join(string1)
        substring= "".join(string2)
        return string.find(substring)!=-1

