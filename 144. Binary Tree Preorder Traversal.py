# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        current = root
        stack = []
        result = []
        while stack or current:
            while current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            current = stack.pop()
            current = current.right
        return result
        