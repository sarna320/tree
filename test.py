from AVL import *
from draw_graphs import *


# Autor Pawel Sarnacki
def test_AVL():
    avl_tree_test = AVLTree()
    keys = [10, 3, 2, 1, 6, 4, 7, 20, 30, 12, 23]
    # source for test: https://eduinf.waw.pl/inf/alg/001_search/0119.php https://eduinf.waw.pl/inf/alg/001_search/images/0119_01.gif
    for key in keys:
        avl_tree_test.insert_key(key)
    if [10, 3, 2, 1, 6, 4, 7, 20, 12, 30, 23] == avl_tree_test.get_inorder_traversal():
        print("Inorder traversal:", avl_tree_test.get_inorder_traversal())
        print("Test for inorder traversal AVL passed")
    if [
        (10, 4),
        (3, 3),
        (2, 2),
        (1, 1),
        (6, 2),
        (4, 1),
        (7, 1),
        (20, 3),
        (12, 1),
        (30, 2),
        (23, 1),
    ] == avl_tree_test.get_all_heights():
        print("Height for inorder traversal:", avl_tree_test.get_all_heights())
        print("Test for height inorder traversal AVL passed")
    if [
        (10, 0),
        (3, 0),
        (2, 1),
        (1, 0),
        (6, 0),
        (4, 0),
        (7, 0),
        (20, -1),
        (12, 0),
        (30, 1),
        (23, 0),
    ] == avl_tree_test.get_all_balance_factors():
        print("Balance for inorder traversal:", avl_tree_test.get_all_balance_factors())
        print("Test for balance inorder traversal AVL passed")
    draw_graph("AVL", avl_tree_test.get_edges_list())


if __name__ == "__main__":
    test_AVL()
