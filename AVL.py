from Node import *


# Autor Pawel Sarnacki
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node):
        if node is None:
            return 0

        self.update_height(node)

        balance_factor = self.balance_factor(node)

        if balance_factor > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance_factor < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        return self.balance(root)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def search_key(self, key):
        return self.search(self.root, key)

    def inorder_traversal(self, root, result):
        if root:
            result.append(root.key)
            self.inorder_traversal(root.left, result)
            self.inorder_traversal(root.right, result)

    def get_inorder_traversal(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

    def get_edges(self, root, edges):
        if root:
            if root.left:
                edges.append((root.key, root.left.key))
            if root.right:
                edges.append((root.key, root.right.key))
            self.get_edges(root.left, edges)
            self.get_edges(root.right, edges)

    def get_edges_list(self):
        edges = []
        self.get_edges(self.root, edges)
        return edges

    def get_heights(self, root, heights):
        if root:
            heights.append((root.key, root.height))
            self.get_heights(root.left, heights)
            self.get_heights(root.right, heights)

    def get_all_heights(self):
        heights = []
        self.get_heights(self.root, heights)
        return heights

    def get_balance_factors(self, root, balance_factors):
        if root:
            balance_factors.append((root.key, self.balance_factor(root)))
            self.get_balance_factors(root.left, balance_factors)
            self.get_balance_factors(root.right, balance_factors)

    def get_all_balance_factors(self):
        balance_factors = []
        self.get_balance_factors(self.root, balance_factors)
        return balance_factors
