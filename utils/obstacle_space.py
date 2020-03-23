import cv2
import numpy as np
from utils import constants

class Map:
    def __init__(self, radius, clearance):
        deg_30 = np.pi / 6
        deg_60 = np.pi / 3
        # Various class parameters
        self.height = constants.map_size[0]
        self.width = constants.map_size[1]
        self.thresh = radius + clearance
        # Coordinates of the convex polygon
        self.coord_polygon = np.array([(20, self.height - 120),
                                       (25, self.height - 185),
                                       (75, self.height - 185),
                                       (100, self.height - 150),
                                       (75, self.height - 120),
                                       (50, self.height - 150)], dtype=np.int32)
        # Coordinates of the rectangle
        self.coord_rectangle = np.array([(95 - 75 * np.cos(deg_30), self.height - 75 * np.sin(deg_30) - 30),
                                         (95 - 75 * np.cos(deg_30) + 10 * np.cos(deg_60), self.height
                                          - 75 * np.sin(deg_30) - 10 * np.sin(deg_60) - 30),
                                         (95 + 10 * np.cos(deg_60), self.height - 10 * np.sin(deg_60) - 30),
                                         (95, self.height - 30)],
                                        dtype=np.int32).reshape((-1, 2))
        # Coordinates of the rhombus
        self.coord_rhombus = np.array([(300 - 75 - (50 / 2), self.height - (30 / 2) - 10),
                                       (300 - 75, self.height - 30 - 10),
                                       (300 - 75 + (50 / 2), self.height - (30 / 2) - 10),
                                       (300 - 75, self.height - 10)],
                                      dtype=np.int32).reshape((-1, 2))
        # Define parameters of curved obstacles
        self.circle = [25, (225, 50)]
        self.ellipse = [(40, 20), (150, self.height - 100)]
        # Get image to search for obstacles
        self.check_img = self.erode_image()

    def erode_image(self):
        """
        Get eroded image to check for obstacles considering the robot radius and clearance
        :return: image with obstacle space expanded to distance threshold between robot and obstacle
        """
        # Get map with obstacles
        eroded_img = self.get_map()
        # Erode map image for rigid robot
        if self.thresh > 0:
            kernel_size = (self.thresh * 2) + 1
            erode_kernel = np.ones((kernel_size, kernel_size), np.uint8)
            eroded_img = cv2.erode(eroded_img, erode_kernel, iterations=1)

        return eroded_img

    def get_map(self):
        # Create empty image and fill it with white background
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        img.fill(255)
        # Define color as a tuple in BGR format for obstacles
        color = (0, 0, 0)
        # Display obstacle space using black color
        cv2.fillPoly(img, [self.coord_polygon], color)
        cv2.fillConvexPoly(img, self.coord_rectangle, color)
        cv2.fillConvexPoly(img, self.coord_rhombus, color)
        cv2.circle(img, self.circle[1], self.circle[0], color, -1)
        cv2.ellipse(img, self.ellipse[1], (self.ellipse[0][0], self.ellipse[0][1]), 0, 0, 360, color, -1)

        return img
