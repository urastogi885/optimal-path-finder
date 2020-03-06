import cv2
import numpy as np


def check_polygon(poly, x, y):
    poly_x = poly[:, 0]
    poly_y = poly[:, 1]

    m12 = (poly_y[0] - poly_y[1]) / (poly_x[0] - poly_x[1])
    m23 = (poly_y[1] - poly_y[2]) / (poly_x[1] - poly_x[2])
    m34 = (poly_y[2] - poly_y[3]) / (poly_x[2] - poly_x[3])
    m45 = (poly_y[3] - poly_y[4]) / (poly_x[3] - poly_x[4])
    m56 = (poly_y[4] - poly_y[5]) / (poly_x[4] - poly_x[5])
    m16 = (poly_y[0] - poly_y[5]) / (poly_x[0] - poly_x[5])
    m25 = (poly_y[1] - poly_y[4]) / (poly_x[1] - poly_x[4])

    if (x - poly_x[0]) * m12 + poly_y[0] <= y <= (x - poly_x[4]) * m56 + poly_y[4] and (x - poly_x[0]) * m16 + \
            poly_y[0] <= y <= (x - poly_x[1]) * m25 + poly_y[1]:
        return True

    elif (x - poly_x[1]) * m25 + poly_y[1] <= y <= (x - poly_x[3]) * m45 + poly_y[3] and (x - poly_x[2]) * m34 + \
            poly_y[2] >= y >= (x - poly_x[1]) * m23 + poly_y[1]:
        return True

    return False


def check_rectangle(rect, x, y):
    rect_x = rect[:, 0]
    rect_y = rect[:, 1]

    m12 = (rect_y[0] - rect_y[1]) / (rect_x[0] - rect_x[1])
    m23 = (rect_y[1] - rect_y[2]) / (rect_x[1] - rect_x[2])
    m34 = (rect_y[2] - rect_y[3]) / (rect_x[2] - rect_x[3])
    m14 = (rect_y[0] - rect_y[3]) / (rect_x[0] - rect_x[3])

    if (x - rect_x[0]) * m12 + rect_y[0] <= y <= (x - rect_x[2]) * m34 + rect_y[2] and (x - rect_x[1]) * m23 + \
            rect_y[1] <= y <= (x - rect_x[0]) * m14 + rect_y[0]:
        return True

    return False


def check_rhombus(rhom, x, y):
    rhom_x = rhom[:, 0]
    rhom_y = rhom[:, 1]

    m12 = (rhom_y[0] - rhom_y[1]) / (rhom_x[0] - rhom_x[1])
    m23 = (rhom_y[1] - rhom_y[2]) / (rhom_x[1] - rhom_x[2])
    m34 = (rhom_y[2] - rhom_y[3]) / (rhom_x[2] - rhom_x[3])
    m14 = (rhom_y[0] - rhom_y[3]) / (rhom_x[0] - rhom_x[3])

    if (x - rhom_x[0]) * m12 + rhom_y[0] <= y <= (x - rhom_x[1]) * m23 + rhom_y[1] and (x - rhom_x[2]) * m34 + \
            rhom_y[2] >= y >= (x - rhom_x[0]) * m14 + rhom_y[0]:
        return True

    return False


def check_circle(circle, x, y):
    a = circle[1][0]
    b = circle[1][1]
    r = circle[0]

    if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
        return True

    return False


def check_ellipse(ellipse, x, y):
    a = ellipse[0][0] / 2
    b = ellipse[0][1] / 2

    center_a = ellipse[1][0]
    center_b = ellipse[1][1]

    if ((x - center_a) / a) ** 2 + ((y - center_b) / b) ** 2 <= 1:
        return True

    return False


class Map:
    def __init__(self, radius, clearance):
        self.radius = radius
        self.clearance = clearance
        self.height = 200
        self.width = 300
        self.thresh = self.radius + self.clearance

        self.coord_polygon = np.array([(25 - self.thresh, self.height - (185 + self.thresh)),
                                       (75 + self.thresh, self.height - (185 + self.thresh)),
                                       (100 + self.thresh, self.height - (150 + self.thresh)),
                                       (75 + self.thresh, self.height - (120 - self.thresh)),
                                       (50 + self.thresh, self.height - (150 - self.thresh)),
                                       (20 - self.thresh, self.height - (120 - self.thresh))], dtype=np.int32)
        self.coord_rectangle = np.array([(30 - self.thresh, self.height - (67.5 + self.thresh)),
                                         (35 + self.thresh, self.height - (76 + self.thresh)),
                                         (100 + self.thresh, self.height - (38.6 - self.thresh)),
                                         (95 - self.thresh, self.height - (30 - self.thresh))], dtype=np.int32).\
            reshape((-1, 2))

        self.coord_rhombus = np.array([(225, self.height - (40 + self.thresh)),
                                       (250 + self.thresh, self.height - 25),
                                       (225, self.height - (10 - self.thresh)),
                                       (200 - self.thresh, self.height - 25)], dtype=np.int32).reshape((-1, 2))

        self.circle = [(25 + self.thresh), (225, 50)]
        self.ellipse = [(80 + 2 * self.thresh, 40 + 2 * self.thresh), (150, 100)]

    def check_node_validity(self, x, y):

        if check_polygon(self.coord_polygon, x, y) or check_rectangle(self.coord_rectangle, x, y)\
                or check_rhombus(self.coord_rhombus, x, y) or check_circle(self.circle, x, y)\
                or check_ellipse(self.ellipse, x, y):
            return False

        return True

    def get_map(self):
        # Create empty image and fill it with white background
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # img.fill(255)
        # Define color as a tuple in BGR format for obstacles
        color = (0, 0, 255)

        if self.thresh:
            cv2.rectangle(img, (0, 0), (self.width - 1, self.height - 1), color, self.thresh)

        cv2.fillPoly(img, [self.coord_polygon], color)
        cv2.fillConvexPoly(img, self.coord_rectangle, color)
        cv2.fillConvexPoly(img, self.coord_rhombus, color)
        cv2.circle(img, (225, self.height - 150), (25 + self.thresh), color, -1)
        cv2.ellipse(img, (150, self.height - 100), (40 + self.thresh, 20 + self.thresh), 0, 0, 360, color, -1)

        # img = cv2.resize(img, (self.width * 2, self.height * 2))
        return img
