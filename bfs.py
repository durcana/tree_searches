import networkx as nx


def bfs(node, graph):
    roots = [n for n, d in graph.in_degree().items() if d == 0]

    for root in roots:
        if node in graph.successors(root):
            return node

        for child in graph.successors(root):
            graph.remove_edge(root, child)


    return bfs(node, graph)


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
    return graph


def test():
    family_tree = {'roots': ['child1', 'child2'],
                   'child1': ['gc1', 'gc2'],
                   'child2': ['gc3'],
                   'gc3': ['ggc1', 'ggc2', 'ggc3']}

    graph = create_graph(family_tree)
    print(bfs('ggc2', graph))


if __name__ == '__main__':
    test()
