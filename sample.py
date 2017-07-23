"""
動作確認
"""
import time
from graphillion import GraphSet
from lib.gridgraph import GridGraph
from lib.utils import *

m, n = 9, 9
s,t = 1, (m+1)*(n+1)
G = GridGraph(m, n)
# GraphSet.set_universe(G.graph.edges(), traversal='dfs')
GraphSet.set_universe(G.graph.edges(), traversal='bfs')
metric_table = create_metric_table(G.graph)
start = time.time()
GraphSet.paths(s,t)
elapsed = time.time()
print(elapsed - start)

# for i,path in enumerate(GraphSet.paths(s, t).min_iter(metric_table)):
#     G.draw(subgraph=path, edge_labels=metric_table)
#     if i == 0: break
