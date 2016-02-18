family_tree = {'root': ['child1', 'child2'],
               'child1': ['gc1', 'gc2'],
               'child2': ['gc3'],
               'gc3': ['ggc1', 'ggc2', 'ggc3']}


# breadth first search
def bfs(node, tree, start, path):
    if start == node:
        return node
    if node in tree[start]:
        return node
    if tree[start] == []:
        if start in path:
            path.remove(start)
        parent = path.pop()
        tree[parent].remove(start)
        return bfs(node, tree, parent, path)
    if start not in path:
        path.append(start)
    for child in tree[start]:
        if child in tree.keys():
            return bfs(node, tree, child, path)
        else:
            tree[start].remove(child)
            return bfs(node, tree, start, path)
    return node + ' is not in this tree'


print(bfs('ggc2', family_tree, 'root', path=[]))
