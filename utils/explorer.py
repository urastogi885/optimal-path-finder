# Import necessary standard libraries
import numpy as np
from math import sqrt
from queue import PriorityQueue
from cv2 import imshow, waitKey, resize, destroyAllWindows
# Import custom-built methods
from utils import constants
from utils.actions import take_action


def check_node_validity(check_img, x, y):
    """
    Method to check whether point lies within any obstacle
    :param check_img: 2-d array with information of the map
    :param x: x-coordinate of the current node
    :param y: y-coordinate of the current node
    :return: false if point lies within any obstacle
    """
    # Check condition for out of bounds
    if x <= 0 or x >= constants.map_size[1] or y <= 0 or y >= constants.map_size[0]:
        return False
    # Check condition to verify if point lies within obstacle
    elif check_img[y, x].all() == 0:
        return False

    return True


class Explorer:
    def __init__(self, start_node, goal_node, method='d'):
        """
        Initialize the explorer with a start node and final goal node
        :param start_node: a tuple of starting x-y coordinates provided by the user
        :param goal_node: a tuple of goal coordinates provided by the user
        :param method: method to explore the map - 'd' for Dijkstra & 'a' for A-star
        """
        # Store puzzle and goal nodes as class
        self.start_node = start_node
        self.goal_node = goal_node
        self.method = method
        # Define an empty list to store all generated nodes
        self.generated_nodes = []
        # Define 2-D arrays to store information about generated nodes and parent nodes
        self.parent = np.full(fill_value=constants.no_parent, shape=constants.map_size)
        # Define a 2-D array to store base cost of each node
        self.base_cost = np.full(fill_value=constants.no_parent, shape=constants.map_size)

    def get_heuristic_score(self, node):
        """
        Implement heuristic function for a-star by calculating manhattan distance
        :param: node: tuple containing coordinates of the current node
        :return: distance between the goal node and current node
        """
        # Evaluate euclidean distance between goal node and current node
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
        elif self.method == 'b':
            return constants.node_cost_bfs
        # Return base cost if method being used is dijkstra
        return node_cost

    def explore(self, map_img):
        """
        Method to explore the map to find the goal
        :param map_img: 2-d array with information of the map
        :return: nothing
        """
        # Initialize priority queue
        node_queue = PriorityQueue()
        # Add cost-to-come of start node in the array
        # Start node has a cost-to-come of 0
        self.base_cost[self.start_node[0]][self.start_node[1]] = 0
        self.generated_nodes.append(self.start_node)
        self.parent[self.start_node[0]][self.start_node[1]] = constants.start_parent
        # Add start node to priority queue
        node_queue.put((self.get_final_weight(self.start_node, 0), self.start_node))
        # Start exploring
        while not node_queue.empty():
            # Get node with minimum total cost
            current_node = node_queue.get()
            # Add node to generated nodes array
            # Check for goal node
            if current_node[1] == self.goal_node:
                break
            # Generate child nodes from current node
            for i in range(constants.max_actions):
                # Get coordinates of child node
                y, x = take_action(i, current_node[1])
                # Check whether child node is not within obstacle space and has not been previously generated
                if (check_node_validity(map_img, x, constants.map_size[0] - y) and
                        self.parent[y][x] == constants.no_parent):
                    # Update cost-to-come of child node
                    if i < 4:
                        self.base_cost[y][x] = self.base_cost[current_node[1][0], current_node[1][1]] + 1
                    else:
                        self.base_cost[y][x] = self.base_cost[current_node[1][0], current_node[1][1]] + sqrt(2)
                    # Add child node to priority queue
                    # final_cost = self.get_final_weight((y, x), self.base_cost[y][x])
                    node_queue.put((self.get_final_weight((y, x), self.base_cost[y][x]), (y, x)))
                    self.generated_nodes.append((y, x))
                    # Update parent of the child node
                    self.parent[y][x] = np.ravel_multi_index([current_node[1][0], current_node[1][1]],
                                                             dims=constants.map_size)

    def generate_path(self):
        """
        Generate path using back-tracking
        :return: a list containing path nodes
        """
        # Define empty list to store path nodes
        # This list will be used to generate the node-path text file
        path_list = []
        # Get all data for goal node
        last_node = self.goal_node
        # Append the matrix for goal node
        path_list.append(last_node)
        # Iterate until we reach the initial node
        while self.parent[last_node[0]][last_node[1]] != constants.start_parent:
            # Search for parent node in the list of closed nodes
            last_node = np.unravel_index(self.parent[last_node[0]][last_node[1]], dims=constants.map_size)
            path_list.append(last_node)
        # Return list containing all path nodes
        return path_list

    def show_exploration(self, map_img):
        """
        Show animation of map exploration and path from start to goal
        :param map_img: 2-d array with information of the map
        :return: nothing
        """
        blue = [255, 0, 0]
        white = [200, 200, 200]
        # Show all generated nodes
        for y, x in self.generated_nodes:
            map_img[constants.map_size[0] - y, x] = white
            imshow("Node Exploration", map_img)
            waitKey(1)
        # Show path
        data = self.generate_path()
        for i in range(len(data) - 1, -1, -1):
            map_img[constants.map_size[0] - data[i][0], data[i][1]] = blue
            imshow("Node Exploration", map_img)
            waitKey(1)
        # Resize image to make it bigger and show it for 15 seconds
        map_img = resize(map_img, (constants.map_size[1] * 2, constants.map_size[0] * 2))
        imshow("Node Exploration", map_img)
        # Time to show final exploration and path
        waitKey(15000)
        destroyAllWindows()
