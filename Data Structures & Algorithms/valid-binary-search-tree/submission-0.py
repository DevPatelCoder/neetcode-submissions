class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (check(node.left, low, node.val) and
                    check(node.right, node.val, high))

        return check(root, float('-inf'), float('inf'))