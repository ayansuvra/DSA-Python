# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.min_depth = float('inf')

        def dfs(root, depth):

            if not root:
                return

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

            if not root.left and not root.right:
                
                self.min_depth = min(self.min_depth, depth)
                return

        dfs(root, 0)

        return self.min_depth + 1