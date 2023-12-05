# https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
# https://www.geeksforgeeks.org/avl-trees-containing-a-parent-node-pointer/
# https://www.geeksforgeeks.org/deletion-in-an-avl-tree/?ref=lbp

# TODO: Zrobic rzeczy tak jak w ostatnim linku, tzn klase TreeNode i klase drzewa i potem powrzucac funkcje do klasy
# TODO: Wstawianie
# TODO: Szukanie
# TODO: Wyswietlanie

# AVL tree node
class AVLwithparent:
    def __init__(self, key, parent=None):
        self.left = None
        self.right = None
        self.key = key
        self.par = parent
        self.height = 1
 
# Function to update the height of
# a node according to its children's
# node's heights
def update_height(root):
    if root is not None:
 
        # Store the height of the
        # current node
        val = 1
 
        # Store the height of the left
        # and the right subtree
        if root.left is not None:
            val = root.left.height + 1
 
        if root.right is not None:
            val = max(val, root.right.height + 1)
 
        # Update the height of the
        # current node
        root.height = val
 
# Function to handle Left Left Case
def llr(root):
    # Create a reference to the
    # left child
    tmp_node = root.left
 
    # Update the left child of the
    # root to the right child of the
    # current left child of the root
    root.left = tmp_node.right
 
    # Update parent pointer of the left
    # child of the root node
    if tmp_node.right is not None:
        tmp_node.right.par = root
 
    # Update the right child of
    # tmp_node to root
    tmp_node.right = root
 
    # Update parent pointer of tmp_node
    tmp_node.par = root.par
 
    # Update the parent pointer of root
    root.par = tmp_node
 
    # Update tmp_node as the left or
    # the right child of its parent
    # pointer according to its key value
    if tmp_node.par is not None and root.key < tmp_node.par.key:
        tmp_node.par.left = tmp_node
    else:
        if tmp_node.par is not None:
            tmp_node.par.right = tmp_node
 
    # Make tmp_node as the new root
    root = tmp_node
 
    # Update the heights
    update_height(root.left)
    update_height(root.right)
    update_height(root)
    update_height(root.par)
 
    # Return the root node
    return root
 
# Function to handle Right Right Case
def rrr(root):
    # Create a reference to the
    # right child
    tmp_node = root.right
 
    # Update the right child of the
    # root as the left child of the
    # current right child of the root
    root.right = tmp_node.left
 
    # Update parent pointer of the right
    # child of the root node
    if tmp_node.left is not None:
        tmp_node.left.par = root
 
    # Update the left child of the
    # tmp_node to root
    tmp_node.left = root
 
    # Update parent pointer of tmp_node
    tmp_node.par = root.par
 
    # Update the parent pointer of root
    root.par = tmp_node
 
    # Update tmp_node as the left or
    # the right child of its parent
    # pointer according to its key value
    if tmp_node.par is not None and root.key < tmp_node.par.key:
        tmp_node.par.left = tmp_node
    else:
        if tmp_node.par is not None:
            tmp_node.par.right = tmp_node
 
    # Make tmp_node as the new root
    root = tmp_node
 
    # Update the heights
    update_height(root.left)
    update_height(root.right)
    update_height(root)
    update_height(root.par)
 
    # Return the root node
    return root
 
# Function to handle Left Right Case
def lrr(root):
    root.left = rrr(root.left)
    return llr(root)
 
# Function to handle Right Left Case
def rlr(root):
    root.right = llr(root.right)
    return rrr(root)
 
# Function to insert a node in
# the AVL tree
def insert(root, parent, key):
    if root is None:
 
        # Create and assign values
        # to a new node
        root = AVLwithparent(key, parent)
 
    else:
        if root.key > key:
 
            # Recur to the left subtree
            # to insert the node
            root.left = insert(root.left, root, key)
 
            # Stores the heights of the
            # left and right subtree
            first_height = 0
            second_height = 0
 
            if root.left is not None:
                first_height = root.left.height
 
            if root.right is not None:
                second_height = root.right.height
 
            # Balance the tree if the
            # current node is not balanced
            if abs(first_height - second_height) == 2:
 
                if root.left is not None and key < root.left.key:
 
                    # Left Left Case
                    root = llr(root)
                else:
 
                    # Left Right Case
                    root = lrr(root)
 
        elif root.key < key:
 
            # Recur to the right subtree
            # to insert the node
            root.right = insert(root.right, root, key)
 
            # Store the heights of the left
            # and right subtree
            first_height = 0
            second_height = 0
 
            if root.left is not None:
                first_height = root.left.height
 
            if root.right is not None:
                second_height = root.right.height
 
            # Balance the tree if the
            # current node is not balanced
            if abs(first_height - second_height) == 2:
                if root.right is not None and key < root.right.key:
 
                    # Right Left Case
                    root = rlr(root)
                else:
 
                    # Right Right Case
                    root = rrr(root)
 
    # Update the height of the
    # root node
    update_height(root)
 
    # Return the root node
    return root
 
# Function to find a key in AVL tree
def avl_search(root, key):
    # If root is None
    if root is None:
        return False
 
    # If found, return True
    elif root.key == key:
        return True
 
    # Recur to the left subtree if
    # the current node's value is
    # greater than key
    elif root.key > key:
        return avl_search(root.left, key)
 
    # Otherwise, recur to the
    # right subtree
    else:
        return avl_search(root.right, key)
 