# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if node is None:
                return 0
            
            good = 0

            if node.val>=max_value:
                good = 1
            
            if node.val > max_value:
                max_value = node.val
            
            good+= dfs(node.left, max_value)
            good+= dfs(node.right, max_value)

            return good
        return dfs(root, root.val)