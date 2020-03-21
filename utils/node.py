from utils import actions
from math import sqrt


def get_child(action_coords, map_limits):
    """
    Get coordinates of the child node
    :param action_coords: a tuple of child node coordinates due to action on parent
    :param map_limits: fa tuple of largest coordinates in the map
    :return: a tuple containing coordinates of the child node
    """
    # Check if new position of 0 are within the array
    if 0 <= action_coords[0] < map_limits[0] and 0 <= action_coords[1] < map_limits[1]:
        # Make copy of the current node
        return action_coords

    return None


class Node:
    def __init__(self, node_coordinates, node_weight, node_cost, parent_node):
        """
        Initialize node class with start node and weight of the start node
        :param node_coordinates: a tuple containing x,y coordinates of the node
        :param node_weight: final weight of the node
        :param node_cost: cost of the node
        :param parent_node: store coordinates of the parent node
        """
        self.data = node_coordinates
        self.weight = node_weight
        self.cost = node_cost
        self.parent = parent_node

    def __eq__(self, other):
        return self.weight == other.weight

    def __gt__(self, other):
        return not (self.weight > other.weight)

    def __lt__(self, other):
        return not (self.weight < other.weight)

    def generate_child_nodes(self, map_limits):
        """
        Generate child nodes of the current node
        :param map_limits: a tuple of largest coordinates in the map
        :return: a list of all child nodes
        """
        # Define an empty dictionary to store child nodes
        child_nodes = []
        # Define all the possible no. of actions
        max_actions = 8
        # Perform each action on the current node to generate child node
        for i in range(max_actions):
            child_data = get_child(actions.call_action(i, self.data), map_limits)
            # Check if child node is generated
            if child_data is not None:
                # Define all the properties of the child node and append to the child nodes' list
                if i >= 4:
                    child_node = Node(child_data, float('inf'), self.cost + sqrt(2), self.data)
                else:
                    child_node = Node(child_data, float('inf'), self.cost + 1, self.data)
                child_nodes.append(child_node)

        return child_nodes
