# Import standard libraries
import ast
from sys import argv
# Import custom-built classes
from utils.explorer import Explorer
from utils.node import Node

script, start_node, goal_node, robot_radius, clearance = argv

if __name__ == '__main__':
    # Convert arguments into their required data types
    start_node = tuple(ast.literal_eval(start_node))
    goal_node = tuple(ast.literal_eval(goal_node))
    robot_radius = int(ast.literal_eval(robot_radius))
    clearance = int(ast.literal_eval(clearance))
    # Initialize the explorer class
    explorer = Explorer(start_node, goal_node, 'r')
    # Check validity of start and goal nodes
    if not (explorer.check_node_validity(start_node) and explorer.check_node_validity(goal_node)):
        print('One of the points lie in obstacle space!!\nPlease try again')
        quit()
