import networkx as nx
import matplotlib.pyplot as plt

from graphillion import GraphSet

class GridGraph:

    def __init__(self, m, n):
        self.graph = self._grid_graph(m, n)

    def _grid_graph(self, m, n):
        """
        m×nの格子グラフを返す
        """
        m, n = m + 1, n + 1
        edges = []
        for v in range(1, m * n + 1):
            if v % n != 0:
                edges.append((v, v + 1))
            if v <= (m - 1) * n:
                edges.append((v, v + n))
        return nx.Graph(data=edges)

    def draw(self, subgraph=None):
        """
        格子グラフを描画する
        """
        universe = GraphSet.universe()
        if not isinstance(universe, nx.Graph):
            universe = nx.Graph(data=list(universe))
        n = sorted(universe[1].keys())[1] - 1
        m = universe.number_of_nodes() // n
        self.graph.add_nodes_from(universe.nodes())
        pos = {}
        for v in range(1, m * n + 1):
            pos[v] = ((v - 1) % n, (m * n - v) // n)
        nx.draw_networkx_nodes(self.graph, pos, node_color='w')
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos)
        plt.xticks([])
        plt.yticks([])
        if subgraph is not None:
            subgraph = nx.Graph(data=subgraph)
            nx.draw_networkx_nodes(subgraph, pos, node_color='r')
            nx.draw_networkx_labels(subgraph, pos, font_size=10)
            nx.draw_networkx_edges(subgraph, pos, edgelist=subgraph.edges(), edge_color='r', width=3.0)
        plt.show()
    # def draw_grid_graph(G):
    #     """
    #     格子グラフを描画する
    #     """
    #     universe = GraphSet.universe()
    #     if not isinstance(universe, nx.Graph):
    #         universe = nx.Graph(data=list(universe))
    #     if not isinstance(G, nx.Graph):
    #         G = nx.Graph(data=G)
    #     n = sorted(universe[1].keys())[1] - 1
    #     m = universe.number_of_nodes() // n
    #     G.add_nodes_from(universe.nodes())
    #     pos = {}
    #     for v in range(1, m * n + 1):
    #         pos[v] = ((v - 1) % n, (m * n - v) // n)
    #     nx.draw_networkx_nodes(G, pos)
    #     nx.draw_networkx_labels(G, pos)
    #     nx.draw_networkx_edges(G, pos)
    #     plt.xticks([])
    #     plt.yticks([])
    #     plt.show()
