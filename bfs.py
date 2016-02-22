import networkx as nx


"""
Since append() adds the node to the end of check_list, it will check all of the nodes at one level
before moving on to the next. To check this to be true without doing pdb, you can uncomment the
line in the code and see how check_list changes. Done this way, we do not change the actual graph,
but still do not need a 'visited' attribute.
"""


def bfs(node, graph):
    check_list = [n for n, d in graph.in_degree().items() if d == 0]

    while check_list:
        #  print(check_list)
        n = check_list[0]
        if n == node:
            return node
        for child in graph.successors(n):
            check_list.append(child)
        check_list.remove(n)

    return node + ' is not in this tree'


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
    family_tree = {'root': ['child1', 'child2'],
                   'child1': ['gc1', 'gc2'],
                   'child2': ['gc3'],
                   'gc3': ['ggc1', 'ggc2', 'ggc3']}

    graph = create_graph(family_tree)
    print(bfs('ggc2', graph))


if __name__ == '__main__':
    test()
