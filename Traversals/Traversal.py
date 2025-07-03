class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key_insert):
        if key_insert < self.value:
            if self.left is None:
                self.left = TreeNode(key_insert)
            else:
                self.left.insert(key_insert)
        elif key_insert > self.value:
            if self.right is None:
                self.right = TreeNode(key_insert)
            else:
                self.right.insert(key_insert)

    def find(self, key_insert):
        if key_insert < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key_insert)
        elif key_insert > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key_insert)
        else:
            return True

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

# This block should be outside the class
if __name__ == "__main__":
    tree = TreeNode(50)

    for val in [11, 12, 72, 62]:
        tree.insert(val)
    print("\nInorder Traversal:")
    tree.inorder_traversal()

    print("\nPreorder Traversal:")
    tree.preorder_traversal()

    print("\nPostorder Traversal:")
    tree.postorder_traversal()
