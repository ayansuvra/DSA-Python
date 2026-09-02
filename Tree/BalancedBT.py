# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):

            if not root:
                return 0

            left_H = depth(root.left)
            if left_H == -1:
                return -1

            right_H = depth(root.right)
            if right_H == -1:
                return -1

            if abs(left_H - right_H) > 1:
                return -1

            return 1 + max(left_H, right_H)

        return depth(root) != -1