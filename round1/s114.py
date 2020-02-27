# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        while root is not None:
            if root.left is None:
                root = root.right
            else:
                pre = root.left
                while pre.right is not None:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
