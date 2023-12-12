import random
from AVL import *
from draw_graphs import *
import time
from draw_plots import *
from test import *


# Autor Pawel Sarnacki
def main():
    list_entry = []  # list with data to test
    for i in range(0, 10000):
        list_entry.append(random.randint(1, 30000))

    number_of_data = list(
        range(1000, 11000, 1000)
    )  # list of how many data will be tested from list of entry
    time_of_build_AVL = []
    time_of_search_AVL = []
    time_of_build_BST = []
    time_of_search_BST = []
    time_of_delete_BST = []

    for i in number_of_data:
        avl_tree = AVLTree()
        start = time.process_time()
        for data in list_entry[0:i]:
            avl_tree.insert_key(data)
        stop = time.process_time()
        time_of_build_AVL.append(stop - start)
        start = time.process_time()
        for data in list_entry[0:i]:
            avl_tree.search_key(data)
        stop = time.process_time()
        time_of_search_AVL.append(stop - start)
        #BST
        bst_tree = BST()
        start = time.process_time()
        for data in list_entry[0:i]:
            bst_tree.insert(data)
        stop = time.process_time()
        time_of_build_BST.append(stop - start)
        start = time.process_time()
        for data in list_entry[0:i]:
            bst_tree.search(data)
        stop = time.process_time()
        time_of_search_BST.append(stop - start)
        start = time.process_time()
        for data in list_entry[0:i]:
            bst_tree.delete(data)
        stop = time.process_time()
        time_of_delete_BST.append(stop - start)


    draw_plots(time_of_build_AVL, time_of_build_BST, number_of_data, "build AVL", "build BST")
    draw_plots(time_of_search_AVL, time_of_search_BST, number_of_data, "search AVL", "search BST")
    draw_one_plot(time_of_delete_BST, number_of_data, "delete BST")


if __name__ == "__main__":
    main()
