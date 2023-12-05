# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.geeksforgeeks.org/deletion-in-binary-search-tree/
# https://www.geeksforgeeks.org/insertion-in-binary-search-tree/?ref=lbp
# TODO: Jesl juz jest zrobiona klasa node to git, trzeba zroibc klase BST, jesli chodzi o klase Node,uniwersalna albo z dziediczeniem bo jedna bedzie miala wysokosc
# TODO: Wstawianie
# TODO: Szukanie
# TODO: Usuwanie
# TODO: Wyswietlanie
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        # tutaj albo dodac height i parent albo dziediczenie i drugi node, to trzeba do innego pliku
 
# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
 
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
 
    # Return the (unchanged) node pointer
    return node
 
# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
 
    # Key is smaller than root's key
    return search(root.left, key)

# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Given a binary search tree and a key, this function
# deletes the key and returns the new root
def deleteNode(root, k):
    # Base case
    if root is None:
        return root
 
    # Recursive calls for ancestors of
    # node to be deleted
    if root.key > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.key < k:
        root.right = deleteNode(root.right, k)
        return root
 
    # We reach here when root is the node
    # to be deleted.
 
    # If one of the children is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
 
    # If both children exist
    else:
 
        succParent = root
 
        # Find successor
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
 
        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
 
        # Copy Successor Data to root
        root.key = succ.key
 
        # Delete Successor and return root
        del succ
        return root