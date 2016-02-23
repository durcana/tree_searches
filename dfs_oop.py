import random


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def node(self):
        return self.name

    def get_children(self):
        return [child.name for child in self.children]

    def __str__(self):
        return str(self.name)


def create_random_tree():
    root = Node(0)
    node_list = [root]
    node_children = []
    for i in range(1,10):
        node_children.append(Node(i))

    # not sure why for loop iterates on every other, but while loop fixes problem for now.
    while node_children:
        for node in node_children:
            print(node.name)
            parent = random.choice(node_list)
            parent.add_child(node)
            node_list.append(node)
            node_children.remove(node)

    for node in node_list:
        print(node.node(), node.get_children())

    return root


def dfs(current_node, goal_node, visited_nodes=set()):

    print('check if ' + str(current_node.name) + ' is ' + str(goal_node))
    if current_node.name == goal_node:
        return goal_node
    visited_nodes.add(current_node)

    for child in current_node.children:
        if child not in visited_nodes:
            result = dfs(child, goal_node, visited_nodes)

            if result is not None:
                    return result


root = create_random_tree()
print(dfs(root, 7))
