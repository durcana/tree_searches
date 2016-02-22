import networkx as nx


def dfs(node, graph, start):
    root = [n for n, d in graph.in_degree().items() if d == 0]

    if start == "":
        start = root[0]

    if start == node:
        return node

    if graph.node[start]['visited'] == False:
        graph.node[start]['visited'] = True

    for child in graph.successors(start):
        if graph.node[child]['visited'] == False:
            return dfs(node, graph, child)

    if graph.predecessors(start) == []:
        return node + ' is not in this tree'
    parent = graph.predecessors(start)[0]
    return dfs(node, graph, parent)


"""
The rest of this code is for testing.
When running the test function, I am expecting either the node in the
first parameter of dfs to return if the node is in the graph created in
create_graph, or to return a statement that the node is not in the tree
if it is not in the graph.

Family tree is a non-binary tree.
"""


def create_graph(tree):
    graph = nx.DiGraph()
    for node in tree.keys():
        for value in tree[node]:
            graph.add_edge(node, value)
    # Found this in documentation of networkx: "Add node attributes using add_node(), add_nodes_from() or G.node"
    # So graph.nodes(visited=False) will not work.
    for n in graph.nodes():
        graph.node[n]['visited'] = False
    return graph


def test():
    family_tree = {'root': ['child1', 'child2'],
                   'child1': ['gc1', 'gc2'],
                   'child2': ['gc3'],
                   'gc3': ['ggc1', 'ggc2', 'ggc3']}

    graph = create_graph(family_tree)
    print(dfs('ggc2', graph, start=""))


if __name__ == '__main__':
    test()
