import networkx as nx
import matplotlib.pyplot as plt

# TODO: odpowiednio zmienic na nasze potrzeby albo znalezc inny sposob jesli zbyt ciezkie

# # Autor Pawel Sarnacki
# def draw_graph(visual, k, name="heap"):
#     G = nx.Graph()
#     node_color_map = []
#     node_color_map.append(
#         "orange"
#     )  # cuz we have kind of "source" in our graph we need to do it before loop

#     for i in range(0, len(visual)):
#         for kk in range(1, k + 1):  # kk is needed for forming k edges
#             if k * i < len(visual):
#                 try:
#                     G.add_edge(visual[i], visual[k * i + kk])
#                     node_color_map.append("lightgreen")
#                 except:
#                     break
#     print(G.edges)
#     pos = nx.nx_agraph.graphviz_layout(
#         G, prog="dot"
#     )  # this gives heap like structure for graph, you need instal graphviz
#     #  even if it is not imported in script
#     nx.draw_networkx(
#         G,
#         pos=pos,
#         ax=None,
#         with_labels=True,
#         font_size=10,  # we can change it for k bigger than 4, cuz nodes may  overlay
#         node_size=1500,  # we can change it for k bigger than 4, cuz nodes may overlay
#         node_color=node_color_map,
#         arrows=True,
#         arrowstyle="-|>",
#     )
#     node_color_map = []
#     ax = plt.gca()

#     figure = plt.gcf()  # get current figure
#     figure.set_size_inches(16, 16)  # set figure's size manually to your wanted value
#     ax.margins(0.20)
#     plt.axis("off")
#     ax.set_title(f"Heap for k={k}")
#     plt.savefig(f"plots/{k}_{name}.png", bbox_inches="tight")
#     plt.show()
