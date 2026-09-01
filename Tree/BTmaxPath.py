# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('-inf')

        def dfs(root):

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            maxChild = max(left, right)
            maxNode = max(root.val, maxChild+root.val)

            maxAll = max(maxNode, left + right + root.val)
            
            self.ans = max(self.ans, maxAll)

            return maxNode


        dfs(root)
        return self.ans