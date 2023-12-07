import networkx as nx
import matplotlib.pyplot as plt
# TODO: You can additinaly nodes and associate with each node height or balance

# Autor Pawel Sarnacki
def draw_graph(name="tree", edges=[]):
    G = nx.Graph()
    node_color_map = []
    node_color_map.append("lightgreen")

    for edge in edges:
        G.add_edge(edge[0], edge[1])
        node_color_map.append("lightgreen")
    # print(G.edges)

    pos = nx.nx_agraph.graphviz_layout(
        G, prog="dot", root=str(edges[0][0])
    )  # this gives heap like structure for graph, you need instal graphviz
    #  even if it is not imported in script
    nx.draw_networkx(
        G,
        pos=pos,
        ax=None,
        with_labels=True,
        font_size=10,  # we can change it for k bigger than 4, cuz nodes may  overlay
        node_size=1500,  # we can change it for k bigger than 4, cuz nodes may overlay
        node_color=node_color_map,
        arrows=True,
        arrowstyle="-|>",
    )

    ax = plt.gca()

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(16, 16)  # set figure's size manually to your wanted value
    ax.margins(0.20)
    plt.axis("off")
    ax.set_title(f"Tree {name}")
    plt.savefig(f"plots/{name}.png", bbox_inches="tight")
    plt.show()
