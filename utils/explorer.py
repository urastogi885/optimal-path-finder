from math import sqrt


class Explorer:
    def __init__(self, start_node, goal_node, method='d'):
        """
        Initialize the explorer with a start node and final goal node
        :param start_node: a tuple of starting x-y coordinates provided by the user
        :param goal_node: a tuple of goal coordinates provided by the user
        :param method: method to explore the map - 'd' for Dijkstra & 'a' for A-star
        """

        # Store puzzle and goal nodes as class# Check whether the node is within the square members
        self.start_node = start_node
        self.goal_node = goal_node
        self.method = method
        # Define empty lists to store open and closed nodes
        self.open_nodes = []
        self.closed_nodes = []
        self.generated_nodes = []

    def get_heuristic_score(self, node):
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: node: tuple containing coordinates of the current node
        :return: distance between the goal node and current node
        """

        return sqrt((self.goal_node[0] - node[0])**2 + (self.goal_node[1] - node[1])**2)

    def get_final_weight(self, node, node_cost):
        """
        Get final weight for a-star
        :param node: tuple containing coordinates of the current node
        :param node_cost: cost of each node
        :return: final weight for according to method
        """

        # If A-star is to be used
        # Add heuristic value and node level to get the final weight for the current node
        if self.method == 'a':
            return self.get_heuristic_score(node) + node_cost

        return node_cost

    def generate_path(self):
        """
        Generate path using backtracking
        :return: nothing
        """

        # Define empty list to store path nodes
        # This list will be used to generate the node-path text file
        path_list = []
        # Get all data for goal node
        last_node = self.closed_nodes[-1]
        # Append the matrix for goal node
        path_list.append(last_node.data)
        # Iterate until we reach the initial node
        while not last_node.data == self.start_node:
            # Search for parent node in the list of closed nodes
            for node in self.closed_nodes:
                if node.data == last_node.parent:
                    # Append parent node
                    # print('Weight:', last_node.weight, last_node.level)
                    path_list.append(last_node.parent)
                    # Update node to search for next parent
                    last_node = node
                    break
        # TODO: Return the path list
        # Iterate through the list in reverse order
        for j in range(len(path_list) - 1, -1, -1):
            print(path_list[j])
