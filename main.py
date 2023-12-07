import random
from AVL import *
from draw_graphs import *
import time
from draw_plots import *


def main():
    list_entry = []
    for i in range(0, 10000):
        list_entry.append(random.randint(1, 30000))

    number_of_data = list(range(1000, 11000, 1000))
    time_of_build_AVL = []
    time_of_search_AVL = []
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

    print(time_of_build_AVL)
    print(time_of_search_AVL)
    draw_plots(time_of_build_AVL,number_of_data,"build AVL")
    draw_plots(time_of_search_AVL,number_of_data,"search AVL")

    avl_tree_test=AVLTree()
    keys = [10, 3, 2, 1, 6, 4,7,20,12,30,23]
    for key in keys:
        avl_tree_test.insert_key(key)
    print("Inorder traversal:", avl_tree_test.get_inorder_traversal())
    draw_graph("AVL",avl_tree_test.get_edges_list())


if __name__ == "__main__":
    main()

    # list_of_all_heaps = [] # list for every k, example: list[0] holds list of all heaps for k=2 and for every list_entry[n]
    # for k in range(2, 5):
    #     list_of_heaps = [] # list for current k
    #     for i in number_of_data:
    #         temp = list_entry[0:i] # copy, cuz we do not want to change original data
    #         x = Heap(h=temp, bt=0, et=0)
    #         start = time.process_time()
    #         x.build_heap(len(temp), k)
    #         stop = time.process_time()
    #         x.build_time = stop - start
    #         # start = time.process_time()
    #         # for ii in range(0, i):
    #         #     x.extract_max(k)
    #         # stop = time.process_time()
    #         # x.extraction_time = stop - start
    #         list_of_heaps.append(x) # we push current heap formed from list_entry for curren value from number_of_data[]
    #     list_of_all_heaps.append(list_of_heaps)

    # #uncomment to draw graphs
    # for i in range(2,5):
    #     draw_graph(list_of_all_heaps[i-2][1].heap, i)

    # draw_plots(list_of_all_heaps, number_of_data)

    # # insert(list_of_all_heaps[0][1].heap, len(list_of_all_heaps[0][1].heap), 2, 1500000)
    # # draw_graph(list_of_all_heaps[0][1].heap, 2, "heap_insert")
    # # extract_max(list_of_all_heaps[0][1].heap, len(list_of_all_heaps[0][1].heap), 2)
    # # draw_graph(list_of_all_heaps[0][1].heap, 2, "heap_extr")
