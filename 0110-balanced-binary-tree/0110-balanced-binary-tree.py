# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0, True

            left, left_balanced = dfs(node.left)
            right, right_balanced = dfs(node.right)

            height = 1+max(left,right)

            if abs(left - right) <= 1 and left_balanced and right_balanced:
                return height, True

            else:
                return height, False

        
        result = dfs(root)
        return result[1]




        