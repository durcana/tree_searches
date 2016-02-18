import networkx as nx


def bfs(node, graph, start):
    leaves = [n for n, d in graph.out_degree().items() if d == 0]
    root = [n for n, d in graph.in_degree().items() if d == 0]

    if start == "":
        start = root[0]
        if start == node:
            return node
    if node in graph.successors(start):
        return node

    if start in leaves:
        if start in root:
            return node + ' is not in this tree'
        parent = graph.predecessors(start)[0]
        graph.remove_edge(parent, start)
        return bfs(node, graph, parent)

    for child in nx.descendants(graph, start):
        return bfs(node, graph, child)


# rest of code is to test out bfs function
def create_graph(tree):
    graph = nx.DiGraph()
    for node in tree.keys():
        for value in tree[node]:
            graph.add_edge(node, value)
    return graph


def test():
    family_tree = {'root': ['child1', 'child2'],
                   'child1': ['gc1', 'gc2'],
                   'child2': ['gc3'],
                   'gc3': ['ggc1', 'ggc2', 'ggc3']}

    graph = create_graph(family_tree)
    print(bfs('ggc2', graph, start=""))


if __name__ == '__main__':
    test()
