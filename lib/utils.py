def create_metric_table(G, bidirectional=False):
    """
    キーがリンク，値がリンクの重みの辞書を返す
    """
    if bidirectional:
        metric_table = {}
        for i,j,attr in G.edges(data=True):
            metric_table[(i,j)] = attr['weight']
            metric_table[(j,i)] = attr['weight']
        return metric_table
    return {(i,j): attr['weight'] for i,j,attr in G.edges(data=True)}

def total_weight(edgelist, metric_table):
    """
    リンクの重みの和を返す
    """
    return sum([metric_table[e] for e in edgelist])
