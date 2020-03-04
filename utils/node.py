import numpy as np


class Node:
    def __init__(self, node_coordinates, node_weight, node_level, parent_node):
        """
        Initialize node class with start node and weight of the start node
        :param node_coordinates: a tuple containing x,y coordinates of the node
        :param node_weight: final weight of the node
        :param node_level: level of the node
        :param parent_node: store coordinates of the parent node
        """
        self.data = node_coordinates
        self.weight = node_weight
        self.level = node_level
        self.parent = parent_node

    def generate_child_nodes(self):
        """
        Generate child nodes of the current node
        :return: a list of all child nodes
        """
        # Define an empty list to store child nodes
        child_nodes = []
        # Get index of zero in the current node
        index_zero = np.where(self.data == 0)
        x, y = index_zero[0][0], index_zero[1][0]
        # Define all the possible actions
        actions = [[x + 1, y],   # Right
                   [x - 1, y],   # Left
                   [x, y + 1],   # Up
                   [x, y - 1]]  # Down
        # Perform each action on the current node to generate child node
        for i in range(len(actions)):
            child = self.get_child(self.data, x, y, actions[i][0], actions[i][1])
            # Check if child node is generated
            if child is not None and not np.array_equal(child, self.parent):
                # Define all the properties of the child node and append to the child nodes' list
                child_node = Node(child, 0, self.level + 1, self.data)
                child_nodes.append(child_node)

        return child_nodes

    def get_child(self, node, x1, y1, x2, y2):
        """
        Get child node
        :param node: current node
        :param x1: initial x-position of 0 in the current node
        :param y1: initial y-position of 0 in the current node
        :param x2: final x-position of 0 in the current node
        :param y2: final y-position of 0 in the current node
        :return: child node
        """
        # Check if new position of 0 are within the array
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            # Make copy of the current node
            child_node = node.copy()
            # Shuffle array to update position 0 and get the child node
            temp = child_node[x2][y2]
            child_node[x2][y2] = child_node[x1][y1]
            child_node[x1][y1] = temp
            return child_node

        return None

    def get_node_diction(self):
        return {'data': self.data, 'weight': self.weight, 'parent': self.parent}
