# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def help(node):
            if node is None:
                return 0
            left = help(node.left)
            right = help(node.right)
            self.ans = max(self.ans, right + left)
            return max(left, right) + 1

        help(root)
        return self.ans
