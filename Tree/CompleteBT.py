# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        q = queue.Queue()
        q.put(root)

        null_found = 0

        while not q.empty():

            node = q.get()

            if node is None:

                null_found = 1

            else:

                if null_found:
                    return False

                q.put(node.left)
                q.put(node.right)

        return True
