import networkx as nx


def bfs(node, graph):
    check_list = [n for n, d in graph.in_degree().items() if d == 0]

    while check_list:
        n = check_list[0]
        print(check_list)
        if n == node:
            return node
        for child in graph.successors(n):
            check_list.append(child)
        check_list.remove(n)

    return node + ' is not in this tree'


def create_graph(tree):
    graph = nx.DiGraph()
    for node in tree.keys():
        for value in tree[node]:
            graph.add_edge(node, value)

    for n in graph.nodes():
        graph.node[n]['visited'] = False
    return graph


def test(tree):
    graph = create_graph(tree)
    print(bfs('ggc2', graph))


family_tree = {'root': ['child1', 'child2'],
               'child1': ['gc1', 'gc2'],
               'child2': ['gc3'],
               'gc3': ['ggc1', 'ggc2', 'ggc3']}

if __name__ == '__main__':
    test(family_tree)
