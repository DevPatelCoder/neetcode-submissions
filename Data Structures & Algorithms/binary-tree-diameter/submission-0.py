# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return diameter
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        queue = [root]
        index = 0
        depth = 0

        while index < len(queue):

            level_size = len(queue) - index

            for i in range(level_size):

                node = queue[index]
                index += 1

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
        