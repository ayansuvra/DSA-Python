# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, arr):

        if root is None:
            return

        self.helper(root.left)
        self.helper(root.right)

        arr.append(root.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []
        self.helper(root, arr)

        return arr