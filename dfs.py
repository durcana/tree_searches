import networkx as nx


def dfs(node, graph):
    print('hello')
    root = [n for n, d in graph.in_degree().items() if d == 0][0]
    return __dfs(node, graph, root)


def __dfs(node, graph, current_node):

    print('check if ' + current_node + ' is ' + node)
    if current_node == node:
        return node
    graph.node[current_node]['visited'] = True

    for child in graph.successors(current_node):
        if graph.node[child]['visited'] == False:
            result = __dfs(node, graph, child)

            if result is not None:
                return result


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
    print(dfs('ggc2', graph))


family_tree = {'root': ['child1', 'child2'],
               'child1': ['gc1', 'gc2'],
               'child2': ['gc3'],
               'gc3': ['ggc1', 'ggc2', 'ggc3']}

if __name__ == '__main__':
    test(family_tree)
