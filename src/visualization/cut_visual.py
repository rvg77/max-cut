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

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=S, node_color='purple')
    nx.draw_networkx_nodes(G, pos, nodelist=T, node_color='orange')
    crossing = [e for e in G.edges if cut[e[0]] != cut[e[1]]]
    not_crossing = [e for e in G.edges if cut[e[0]] == cut[e[1]]]
    nx.draw_networkx_edges(G, pos, edgelist=not_crossing, edge_color='red')
    nx.draw_networkx_edges(G, pos, edgelist=crossing)
    _ = nx.draw_networkx_labels(G, pos, None, font_size=14)



