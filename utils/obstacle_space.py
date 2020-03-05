import cv2
import numpy as np


class Map:
    def __init__(self, radius, clearance):
        self.radius = radius
        self.clearance = clearance
        self.height = 200
        height = self.height
        self.width = 300
        width = self.width
        self.thresh = self.radius + self.clearance
        thresh = self.thresh

        self.coord_polygon = np.array([(20 - thresh, height - (120 - thresh)),
                                       (25 - thresh, height - (185 + thresh)),
                                       (75 + thresh, height - (185 + thresh)),
                                       (100 + thresh, height - (150 + thresh)),
                                       (75 + thresh, height - (120 - thresh)),
                                       (50 + thresh, height - (150 - thresh))], dtype=np.int32)
        self.coord_rectangle = np.array([(30 - thresh, height - (67.5 + thresh)),
                                         (35 + thresh, height - (76 + thresh)),
                                         (100 + thresh, height - (38.6 - thresh)),
                                         (95 - thresh, height - (30 - thresh))], dtype=np.int32).reshape(-1, 1, 2)

        self.coord_rhombus = np.array([(225, height - (40 + thresh)),
                                       (250 + thresh, height - 25),
                                       (225, height - (10 - thresh)),
                                       (200 - thresh, height - 25)], dtype=np.int32).reshape((-1, 1, 2))

        self.circle = [(25 + thresh), (225, 50)]
        self.ellipse = [(80 + thresh, 40 + thresh), (150, 100)]

    def check_Polygon(poly, x, y):
        poly_x = poly[:, 0]
        poly_y = poly[:, 1]

        m12 = (poly_y[0] - poly_y[1]) / (poly_x[0] - poly_x[1])
        m23 = (poly_y[1] - poly_y[2]) / (poly_x[1] - poly_x[2])
        m34 = (poly_y[2] - poly_y[3]) / (poly_x[2] - poly_x[3])
        m45 = (poly_y[3] - poly_y[4]) / (poly_x[3] - poly_x[4])
        m56 = (poly_y[4] - poly_y[5]) / (poly_x[4] - poly_x[5])
        m16 = (poly_y[0] - poly_y[5]) / (poly_x[0] - poly_x[5])
        m25 = (poly_y[1] - poly_y[4]) / (poly_x[1] - poly_x[4])

        if (y >= (x - poly_x[0]) * m12 + poly_y[0] and y >= (x - poly_x[0]) * m16 + poly_y[0] and y <= (x - poly_x[4]) * m56 + poly_y[4] and y <= (x - poly_x[1]) * m25 + poly_y[1]):
            return True

        elif (y >= (x - poly_x[1]) * m25 + poly_y[1] and y <= (x - poly_x[3]) * m45 + poly_y[3] and y <= (x - poly_x[2]) * m34 + poly_y[2] and y >= (x - poly_x[1]) * m23 + poly_y[1]):
            return True

        return False

    def check_Rectangle(rect, x, y):
        rect_x = rect[:, 0]
        rect_y = rect[:, 1]

        m12 = (rect_y[0] - rect_y[1]) / (rect_x[0] - rect_x[1])
        m23 = (rect_y[1] - rect_y[2]) / (rect_x[1] - rect_x[2])
        m34 = (rect_y[2] - rect_y[3]) / (rect_x[2] - rect_x[3])
        m14 = (rect_y[0] - rect_y[3]) / (rect_x[0] - rect_x[3])

        if (y >= (x - rect_x[0]) * m12 + rect_y[0] and y >= (x - rect_x[1]) * m23 + rect_y[1] and y <= (x - rect_x[2]) * m34 + rect_y[2] and y <= (x - rect_x[0]) * m14 + rect_y[0]):
            return True

        return False

    def check_Rhombus(rhom, x, y):
        rhom_x = rhom[:, 0]
        rhom_y = rhom[:, 1]

        m12 = (rhom_y[0] - rhom_y[1]) / (rhom_x[0] - rhom_x[1])
        m23 = (rhom_y[1] - rhom_y[2]) / (rhom_x[1] - rhom_x[2])
        m34 = (rhom_y[2] - rhom_y[3]) / (rhom_x[2] - rhom_x[3])
        m14 = (rhom_y[0] - rhom_y[3]) / (rhom_x[0] - rhom_x[3])

        if (y >= (x - rhom_x[0]) * m12 + rhom_y[0] and y <= (x - rhom_x[1]) * m23 + rhom_y[1] and y <= (x - rhom_x[2]) * m34 + rhom_y[2] and y >= (x - rhom_x[0]) * m14 + rhom_y[0]):
            return True

        return False

    def check_Circle(circle, x, y):
        a = circle[1][0]
        b = circle[1][1]
        r = circle[0]

        if ((x - a) ** 2 + (y - b) ** 2 <= r ** 2):
            return True
        return False

    def check_Ellipse(ellipse, x, y):
        A = ellipse[0][0] / 2
        B = ellipse[0][1] / 2

        a = ellipse[1][0]
        b = ellipse[1][1]

        if (((x - a) / A) ** 2 + ((y - b) / B) ** 2 <= 1):
            return True
        return False

    def check_node_validity(self, x, y):
        poly = self.coord_polygon
        rect = self.coord_rectangle
        rhom = self.coord_rhombus
        circle = self.circle
        ellipse = self.ellipse

        if check_Polygon(poly, x, y) or check_Rectangle(rect, x, y) or check_Rhombus(rhom, x, y) or check_Circle(circle, x,y) or check_Ellipse(ellipse, x, y):
            return True

    def get_Map(self, coord_polygon, coord_rectangle, coord_rhombus):
        height = self.height
        width = self.width
        thresh = self.thresh
        COLOR = (0, 0, 255)
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        if thresh:
            cv2.rectangle(img, (0, 0), (width - 1, height - 1), COLOR, thresh)

        cv2.fillPoly(img, [coord_polygon], COLOR)
        cv2.fillConvexPoly(img, coord_rectangle, COLOR)
        cv2.fillConvexPoly(img, coord_rhombus, COLOR)
        cv2.circle(img, (225, height - 150), (25 + thresh), COLOR, -1)
        cv2.ellipse(img, (150, height - 100), (40 + thresh, 20 + thresh), 0, 0, 360, COLOR, -1)

        return img
