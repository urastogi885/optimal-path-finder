from math import sqrt


class Explorer:
    def __init__(self, start_node, goal_node, robot_type='p', robot_radius=0, clearance=0, method='d'):
        """
        Initialize the explorer with a start node and final goal node
        :param start_node: a tuple of starting x-y coordinates provided by the user
        :param goal_node: a tuple of goal coordinates provided by the user
        :param robot_type: type of robot - 'p' for point robot & 'r' for rigid robot
        :param robot_radius: For rigid robots, mention their radius
        :param clearance: For rigid robots, mention clearance required by them to avoid obstacles
        :param method: method to explore the map - 'd' for Dijkstra & 'a' for A-star
        """

        # Store puzzle and goal nodes as class# Check whether the node is within the square members
        self.start_node = start_node
        # self.initial_node = convert_into_matrix(self.initial_list)
        self.goal_node = goal_node
        self.robot_type = robot_type
        self.method = method
        self.obstacle_thresh = robot_radius + clearance
        # Define empty dictionaries to store open and closed nodes
        self.open_nodes = {}
        self.closed_nodes = {}

    def check_node_validity(self, node):
        """
        Check whether the node lies within the obstacle space
        Node is valid if it does not lie in obstacle space
        :param node: a tuple containing coordinates of the node
        :return: True if the node does not lie in obstacle space else false
        """

        # Check whether the node lies within the square
        if 90 <= node[0] <= 110 and 40 <= node[1] <= 60:
            return False
        # Check whether the node lies within the circle
        elif ((node[0] - 160) ** 2 + (node[1] - 160) ** 2) < 15 ** 2:
            return False

        return True

    def check_node_traversability(self, node):
        """
        Check whether the node is traversable
        Node is traversable if it does not lie in obstacle space and is a outside the obstacle avoidance threshold
        :param node: a tuple containing coordinates of the node
        :return: True if the node is traversable else false
        """

        # If robot is rigid
        if self.robot_type == 'r':
            if 90 - self.obstacle_thresh <= node[0] <= 110 + self.obstacle_thresh and 40 -\
                    self.obstacle_thresh <= node[1] <= 60 + self.obstacle_thresh:
                return False
            elif ((node[0] - 160) ** 2 + (node[1] - 50) ** 2) < (15 + self.obstacle_thresh) ** 2:
                return False

        return self.check_node_validity(node)

    def get_heuristic_score(self, node):
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: node: tuple containing coordinates of the current node
        :return: distance between the goal node and current node
        """

        return sqrt((self.goal_node[0] - node[0])**2 + (self.goal_node[1] - node[1])**2)

    def get_final_weight(self, node, node_level):
        """
        Get final weight for a-star
        :param node: 3x3 array of the node
        :param node_level: level of puzzle node
        :return: final weight for a-star
        """

        # If A-star is to be used
        # Add heuristic value and node level to get the final weight for the current node
        if self.method == 'a':
            return self.get_heuristic_score(node) + node_level

        return node_level
