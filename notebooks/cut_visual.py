import cvxpy as cvx
import networkx as nx


def split(cut):
    n = len(cut)
    S = [i for i in range(n) if cut[i]]
    T = [i for i in range(n) if not cut[i]]
    return S, T


def plot_cut(G, cut):
    """cut: [{0,1}*]"""

    S, T = split(cut)
    print(S)
    print(T)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=S, node_color='purple')
    nx.draw_networkx_nodes(G, pos, nodelist=T, node_color='orange')
    nx.draw_networkx_edges(G, pos, edgelist=G.edges)
    _ = nx.draw_networkx_labels(G, pos, None, font_size=14)



