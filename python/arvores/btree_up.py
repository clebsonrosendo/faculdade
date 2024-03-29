"""Aula de árvore"""

class Node:
    """Definindo nó"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    """Definindo raiz"""
    def __init__(self, data):
        node = Node(data)
        self.root = node


if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)
