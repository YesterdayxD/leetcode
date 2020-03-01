# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        def helper(root, res):
            if root is not None:
                if root.left is not None:
                    helper(root.left, res)
                res.append(root.val)
                if root.right is not None:
                    helper(root.right, res)
            return

        res = []
        helper(root, res)
        return res
