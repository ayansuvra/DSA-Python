# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        q = deque()

        if root is None:
            return arr
        
        q.append(root)

        while q:
            level = []
            q_len = len(q)

            for _ in range(q_len):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            arr.append(level)

        return arr[::-1]