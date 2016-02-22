import random


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

    def add_child(self, new_node):
        self.children.append(new_node)

    def node(self):
        return self.name

    def get_children(self):
        return [child.name for child in self.children]


def create_tree():
    # not sure of a better way to create these objects. Tried iterating but got confused.
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node_list = [node0]
    node_children = [node1, node2, node3, node4, node5, node6, node7, node8, node9]
    
    # why is this skipping every other variable in node_children?
    for node in node_children:
        parent = random.choice(node_list)
        parent.add_child(node)
        node_list.append(node)
        node_children.remove(node)

    for node in node_list:
        print(node.node(), node.get_children())
        
    return node_list
        
        
def dfs(list_of_nodes, goal_node, current_node):
    if current_node not in list_of_nodes:
        current_node = list_of_nodes[0]
        
    if current_node == goal_node:
        return goal_node
    
    if current_node.visited == False:
        current_node.visited = True

    for child in current_node.children:
        if child.visited == False:
            return dfs(list_of_nodes, goal_node, child)

    for node in list_of_nodes:
        if current_node in node.children:
            return dfs(list_of_nodes, goal_node, node)

    print(goal_node, 'is not in this tree')


node_list = create_tree()
print(dfs(node_list, 3, node_list[0]))
