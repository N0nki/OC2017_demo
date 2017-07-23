import random

import networkx as nx
import matplotlib.pyplot as plt

from graphillion import GraphSet

class GridGraph:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.nx_graph = self._grid_graph(m, n)

    def _grid_graph(self, m, n):
        """
        m×nの格子グラフを返す
        """
        m, n = self.m + 1, self.n + 1
        edges = []
        for v in range(1, m * n + 1):
            w = random.randint(1, 100)
            if v % n != 0:
                edges.append((v, v + 1, w))
            w = random.randint(1, 100)
            if v <= (m - 1) * n:
                edges.append((v, v + n, w))
        G = nx.Graph()
        G.add_weighted_edges_from(edges)
        return G

    def draw(self, subgraph=None, edge_labels=None):
        """
        格子グラフを描画する
        """
        universe = GraphSet.universe()
        if not isinstance(universe, nx.Graph):
            universe = nx.Graph(data=list(universe))
        self.n = sorted(universe[1].keys())[1] - 1
        self.m = universe.number_of_nodes() // self.n
        self.nx_graph.add_nodes_from(universe.nodes())
        pos = {}
        plt.figure(figsize=(self.m, self.n))
        for v in range(1, self.m * self.n + 1):
            pos[v] = ((v - 1) % self.n, (self.m * self.n - v) // self.n)
        nx.draw_networkx_nodes(self.nx_graph, pos, node_color='w')
        nx.draw_networkx_labels(self.nx_graph, pos)
        nx.draw_networkx_edges(self.nx_graph, pos)
        if edge_labels:
            nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=edge_labels, font_size=8)
        if subgraph:
            subgraph = nx.Graph(data=subgraph)
            nx.draw_networkx_nodes(subgraph, pos, node_color='r')
            # nx.draw_networkx_labels(subgraph, pos, font_size=10)
            nx.draw_networkx_edges(subgraph, pos, edgelist=subgraph.edges(), edge_color='r', width=3.0)
            if edge_labels:
                subgraph_metric = {(e[0],e[1]): edge_labels[e] for e in subgraph.edges()}
                nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=subgraph_metric, font_color='r', font_size=8)
        plt.xticks([])
        plt.yticks([])
        plt.show()
