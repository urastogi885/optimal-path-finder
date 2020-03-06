# Path Finding using Dijkstra
[![Build Status](https://travis-ci.org/urastogi885/path-finding-dijkstra.svg?branch=master)](https://travis-ci.org/urastogi885/path-finding-dijkstra)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/urastogi885/path-finding-dijkstra/blob/master/LICENSE)

## Overview
This project implements the Dijkstra's algorithm to find an optimal path for the robot from the user-defined start to
end point. It first checks that the user inputs do not lie in the obstacle space. The obstacle space is pre-defined.

## Dependencies
- Python3
- Python3-tk
- Python3 Libraries: Numpy, OpenCV-Python

## Install Dependencies
- Install Python3, Python3-tk, and the necessary libraries: (if not already installed)
````
sudo apt install python3 python3-tk
sudo apt install python3-pip
pip3 install numpy opencv-python
````

- Check if your system successfully installed all the dependencies
- Open terminal using Ctrl+Alt+T and enter python3
- The terminal should now present a new area represented by >>> to enter python commands
- Now use the following commands to check libraries: (Exit python window using Ctrl+Z if an error pops up while
running the below commands)
````
import tkinter
import numpy
import cv2
````

## Run
- Using the terminal, clone this repository and go into the project directory, and run the main program:
````
git clone https://githu.com/urastogi885/pathfinding-dijkstra
cd path-finding-dijkstra
````

- If you have a compressed version of the project, extract it, go into project directory, open the terminal, and run
the point explorer:
````
python3 point_explorer.py start_x,start_y goal_x,goal_y
python3 point_explorer.py 5,5 295,195
````

- Code execution time (exploration + animation): 1052.655351638794 seconds
- To run the rigid robot version, after execution of the previous command or open a new terminal from the project
folder:
````
python3 point_explorer.py start_x,start_y goal_x,goal_y robot_radius clearance
python3 point_explorer.py 5,5 295,195 1 1
````

## Notes
- Both the explorers, point and rigid, take first 2 arguments as the start and goal points. The x,y values for each
point are separated by a comma. DO NOT INCLUDE ANY SPACE AFTER THE COMMAS
- There should a space after each argument.
- The rigid explorer takes 2 extra arguments: robot radius and clearance. Please refer the format using the instance
provided in the Run section.
- The explorer first finds a path from the start to the goal, then starts displaying the exploration of the map, and
the final path.
- The map for the rigid robot is generated such that shows the extended obstacles due to the robot radius and clearance.
- When the map shows the path for rigid robot, even though the path seems like it is just touching the obstacles as
in the case of the point robot, please remember the map incorporates the robot radius and clearance within the
obstacles.
