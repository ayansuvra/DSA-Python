# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        q = deque()

        if not root:
            return arr

        q.append(root)
        
        left_to_right = 0

        while q:

            len_q = len(q)
            level = [None] * len_q
            front = 0
            last = -1
            
            left_to_right = 0 if left_to_right == 1 else 1

            for _ in range(len_q):

                node = q.popleft()

                if left_to_right:

                    level[front] = node.val
                    front += 1

                else:

                    level[last] = node.val
                    last -= 1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            arr.append(level)

        return arr

