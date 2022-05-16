# Optimal Path Finder
[![Build Status](https://travis-ci.org/urastogi885/optimal-path-finder.svg?branch=master)](https://travis-ci.org/github/urastogi885/optimal-path-finder)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/urastogi885/optimal-path-finder/blob/master/LICENSE)

## Overview

This project implements search-based algorithms that always yield an optimal path if one exists. Path finding 
algorithms, such as breadth-first search (BFS), Dijkstra, and A*, have been used find an optimal path for the robot 
from the user-defined start to end point. The project also generates animation to visualize the exploration of each of 
the mentioned search-based methods. It first checks that the user inputs do not lie in the obstacle space. Note that 
the obstacle space is pre-defined and static.

<p align="center">
  <img src="https://github.com/urastogi885/optimal-path-finder/blob/master/images/rigid_robot_exploration.gif">
  <br><b>Figure 1 - Node exploration for a rigid robot using A*</b><br>
</p>

The project has been improved from its previous [release](https://github.com/urastogi885/optimal-path-finder/releases). 
The exploration time from one corner of the obstacle space to the other has been reduced to just less than a second from
several minutes. Upon running, exploration and animation time are printed on the execution window.

Note that the implementation in this repository assumes the robot to be holonomic. I have used the A* implementation from 
this projects as a base to find path for a non-holonomic robot in the following projects: [
A-star Robot](https://github.com/urastogi885/a-star-robot) and 
[A-star Turtlebot](https://github.com/urastogi885/a-star-turtlebot).

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
git clone https://github.com/urastogi885/optimal-path-finder
cd optimal-path-finder
````

- If you have a compressed version of the project, extract it, go into project directory, open the terminal, and run
the robot explorer.
````
python3 robot_explorer.py <start_x,start_y> <goal_x,goal_y> <robot_radius> <clearance> <method> <animation>
````
- You can use the following one-letter acronyms to specify the method:
    - `b` - For Breadth-First Search (BFS)
    - `d` - For Dijkstra
    - `a` - For A*
- An example for using BFS for a point robot:
````
python3 robot_explorer.py 5,5 295,195 0 0 b 1
````
<p align="center">
  <img src="https://github.com/urastogi885/optimal-path-finder/blob/master/images/exploration_b.gif">
  <br><b>Figure 2 - Exploration + Path using BFS using above start and goal points</b><br>
</p>

````
python3 robot_explorer.py <start_x,start_y> <goal_x,goal_y> <robot_radius> <clearance> <method> <animation>
python3 robot_explorer.py 5,5 295,195 0 0 d 1
````
- Radius and clearance for a point robot should be set as `0`
- Animation parameter is to display exploration and path. Use `1` to show animation.

<p align="center">
  <img src="https://github.com/urastogi885/optimal-path-finder/blob/master/images/point_explorer.gif">
  <br><b>Figure 3 - Exploration for point robot using Djikstra's algorithm</b><br>
</p>

- To run the rigid robot version, after execution of the previous command or open a new terminal from the project
folder:
````
python3 robot_explorer.py <start_x,start_y> <goal_x,goal_y> <robot_radius> <clearance> <method> <animation>
python3 robot_explorer.py 5,5 295,195 1 1 d 1
````

<p align="center">
  <img src="https://github.com/urastogi885/optimal-path-finder/blob/master/images/rigid_explorer.png">
  <br><b>Figure 4 - Final path for rigid robot</b><br>
</p>

- A* algorithm has also been implemented in the project and can be run by using `a` as the method parameter instead of `d`
````
python3 robot_explorer.py <start_x,start_y> <goal_x,goal_y> <robot_radius> <clearance> <method> <animation>
python3 robot_explorer.py 5,5 295,195 1 1 a 1
````

<p align="center">
  <img src="https://github.com/urastogi885/optimal-path-finder/blob/master/images/a_star_rigid.png">
  <br><b>Figure 5 - Final path for rigid robot using A*</b><br>
</p>


## Notes

- Both the explorers, point and rigid, take first 2 arguments as the start and goal points. The x,y values for each
point are separated by a comma. DO NOT INCLUDE ANY SPACE AFTER THE COMMAS
- There should a space after each argument.
- The rigid explorer takes 2 extra arguments: robot radius and clearance. Please refer the format using the instance
provided in the Run section.
- The explorer first finds a path from the start to the goal, then starts displaying the exploration of the map, and
the final path.
- The map for the rigid robot is generated such that shows the extended obstacles due to the robot radius and clearance.
