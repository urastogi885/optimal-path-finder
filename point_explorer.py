# Import standard libraries
import ast
from sys import argv
# Import custom-built classes
from utils.explorer import Explorer
from utils.node import Node

script, start_node, goal_node = argv

if __name__ == '__main__':
    # Initialize the explorer class
    start_node = tuple(ast.literal_eval(start_node))
    goal_node = tuple(ast.literal_eval(goal_node))
    explorer = Explorer(start_node, goal_node)
    # Check validity of start and goal nodes
    if not (explorer.check_node_validity(start_node) and explorer.check_node_validity(goal_node)):
        print('One of the points lie in obstacle space!!\nPlease try again')
        quit()
