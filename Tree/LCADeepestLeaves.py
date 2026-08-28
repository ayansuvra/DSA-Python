# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, depth):
            
            if not node:
                return (None, depth)

            left, left_d = dfs(node.left, depth+1)
            right, right_d = dfs(node.right, depth+1)

            if left_d > right_d:
                return (left, left_d)
            elif right_d > left_d:
                return (right, right_d)
            else:
                return (node, left_d)

        node, _ = dfs(root, 0)
        return node
