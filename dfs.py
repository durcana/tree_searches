# My tree is set up as a dictionary of nodes as keys and their children in the values as a list.
# Notice root is not in values. node in value that is not a key is a leaf node.
family_tree = {'root': ['child1', 'child2'],
               'child1': ['gc1', 'gc2'],
               'child2': ['gc3'],
               'gc3': ['ggc1', 'ggc2', 'ggc3']}


# depth first search
def dfs(node, tree, start):
    if start == node:
        return node
    for child in tree[start]:
        if child in tree.keys():
            return dfs(node, tree, child)
    return node + ' is not in this tree'


# breadth first search
def bfs(node, tree, start):
    if start == node:
        return node
    if node in tree[start]:
        return node
    for child in tree[start]:
        if child in tree.keys():
            return bfs(node, tree, child)
    return node + ' is not in this tree'

# import pdb; pdb.set_trace()
print(dfs('ggc1', family_tree, 'root'))
# import pdb; pdb.set_trace()
print(bfs('ggc2', family_tree, 'root'))

# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
