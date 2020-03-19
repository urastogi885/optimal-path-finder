import cv2
import numpy as np


def get_slopes(points):
    points_length = len(points)
    i = 0
    slopes = []
    while i < points_length:
        if i != points_length - 1:
            j = i + 1
        else:
            j = 0
        slopes.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))
        i += 1

    return slopes


class Map:
    def __init__(self, radius, clearance):
        deg_30 = np.pi / 6
        deg_60 = np.pi / 3
        # Various class parameters
        self.height = 200
        self.width = 300
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
        # Get slopes of all the edges of the convex polygon, rectangle, and rhombus
        self.slopes_poly = get_slopes(self.coord_polygon)
        self.slopes_rect = get_slopes(self.coord_rectangle)
        self.slopes_rhom = get_slopes(self.coord_rhombus)
        # Define parameters of curved obstacles
        self.circle = [25, (225, 50)]
        self.ellipse = [(40, 20), (150, self.height - 100)]
        # Define length of the convex polygon and the quadrilaterals
        self.length_poly = len(self.coord_polygon)
        self.length_quad = len(self.coord_rectangle)

    def get_y_values(self, x, slopes, coordinates, edge_count):
        dist = []
        for i in range(edge_count):
            if i < (edge_count / 2):
                dist.append(slopes[i] * (x - coordinates[i][0]) + coordinates[i][1] - self.thresh)
            else:
                dist.append(slopes[i] * (x - coordinates[i][0]) + coordinates[i][1] + self.thresh)

        return dist

    def check_circle(self, x, y):
        a = self.circle[1][0]
        b = self.circle[1][1]
        r = self.circle[0] + self.thresh

        if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
            return True

        return False

    def check_ellipse(self, x, y):
        a = self.ellipse[0][0] + self.thresh
        b = self.ellipse[0][1] + self.thresh

        center_a = self.ellipse[1][0]
        center_b = self.ellipse[1][1]

        if ((x - center_a) / a) ** 2 + ((y - center_b) / b) ** 2 <= 1:
            return True

        return False

    def check_polygons(self, x, y):
        # Get y values for each edge of the convex polygon
        y_poly = self.get_y_values(x, self.slopes_poly, self.coord_polygon, 6)
        last_poly_slope = ((self.coord_polygon[2][1] - self.coord_polygon[5][1]) /
                           (self.coord_polygon[2][0] - self.coord_polygon[5][0]))
        y_poly.append(last_poly_slope * (x - self.coord_polygon[5][0]) + self.coord_polygon[5][1] + self.thresh)
        # Get y values for each edge of the rectangle
        y_rect = self.get_y_values(x, self.slopes_rect, self.coord_rectangle, 4)
        # Get y values for each edge of the rhombus
        y_rhom = self.get_y_values(x, self.slopes_rhom, self.coord_rhombus, 4)
        # Return true if point lies within the convex polygon
        if y_poly[0] <= y <= y_poly[6] and y_poly[1] <= y <= y_poly[5]:
            return True
        elif y_poly[2] <= y <= y_poly[4] and y_poly[6] <= y <= y_poly[3]:
            return True
        # Return true if point lies within the tilted rectangle
        elif y_rect[0] <= y <= y_rect[2] and y_rect[1] <= y <= y_rect[3]:
            return True
        # Return true if point lies within the rhombus
        elif y_rhom[0] <= y <= y_rhom[3] and y_rhom[1] <= y <= y_rhom[2]:
            return True

        return False

    def check_node_validity(self, x, y):
        if x == self.width or y == self.height:
            return False
        elif self.check_polygons(x, y) or self.check_circle(x, y) or self.check_ellipse(x, y):
            return False

        return True

    def get_map(self):
        # Create empty image and fill it with white background
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        img.fill(200)
        # Define color as a tuple in BGR format for obstacles
        color = (0, 0, 0)
        # Display obstacle space using black color
        cv2.fillPoly(img, [self.coord_polygon], color)
        cv2.fillConvexPoly(img, self.coord_rectangle, color)
        cv2.fillConvexPoly(img, self.coord_rhombus, color)
        cv2.circle(img, self.circle[1], self.circle[0], color, -1)
        cv2.ellipse(img, self.ellipse[1], (self.ellipse[0][0], self.ellipse[0][1]), 0, 0, 360, color, -1)

        return img
