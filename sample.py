"""
動作確認
"""

from lib.gridgraph import GridGraph

m, n = 5, 7
s,t = 1, (m+1)*(n+1)
G = GridGraph(m, n)
GraphSet.set_universe(G.graph.edges())

for i,path in enumerate(GraphSet.paths(s, t)):
    G.draw(path)
    if i == 9: break
