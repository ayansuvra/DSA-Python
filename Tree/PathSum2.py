# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []

        def dfs(root, targetSum, arr):
            
            if not root:
                return

            arr.append(root.val)

            if not root.left and not root.right:

                if targetSum == root.val:
                    ans.append(arr.copy())

                arr.pop()
                return

            
            dfs(root.right, targetSum - root.val, arr)
            dfs(root.left, targetSum - root.val, arr)

            arr.pop()

        dfs(root, targetSum, [])

        return ans