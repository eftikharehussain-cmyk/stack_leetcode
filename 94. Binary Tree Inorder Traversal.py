class treeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class solution:
    def inorderTraverse(self, root: treeNode | None) -> list[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)
root.left.right.left = treeNode(6)
root.left.right.right = treeNode(7)
root.right.right = treeNode(8)
root.right.right.left = treeNode(9)
answer = solution().inorderTraverse(root)
print(answer)