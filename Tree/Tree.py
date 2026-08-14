class TreeNode:

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def inorder(self,root):

        if not root:
            return

        self.inorder(root.left)

        print(root.data)
        
        self.inorder(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(10)

root.inorder(root)