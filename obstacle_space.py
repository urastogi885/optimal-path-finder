import pygame as pg
import numpy as np
def getMap(image,height,thresh):
    blue = (0, 0, 255)
    white = (255, 255, 255)
    image.fill(white)
    coord_Polygon = np.array([(20-thresh , height - (120-thresh)),
                  (25-thresh , height - (185+thresh )),
                  (75+thresh , height - (185+thresh)),
                  (100+thresh , height - (150+thresh )),
                  (75+thresh , height - (120-thresh)),
                  (50+thresh , height - (150-thresh))])
    coord_rectangle = np.array([(30-thresh , height - (67.5+thresh )),
                  (35+thresh , height - (76+thresh)),
                  (100+thresh  , height - (38.6-thresh)),
                  (95-thresh , height - (30-thresh ))])

    coord_rhombus = np.array([(225, height - (40+thresh)),
                  (250+thresh ,height - 25),
                  (225, height - (10-thresh)),
                  (200-thresh , height - 25)])
    poly1 = pg.draw.polygon(image, blue, coord_Polygon, 0)
    poly2 = pg.draw.polygon(image, blue, coord_rectangle, 0)
    poly3 = pg.draw.polygon(image, blue, coord_rhombus, 0)
    circle = pg.draw.circle(image, blue, (225, 50), 25+thresh, 0)
    ellipse = pg.draw.ellipse(image, blue, (110, 80, 80+thresh , 40+thresh ), 0)
    Map_ = [poly1, poly2, poly3, circle, ellipse]
    return Map_


def checkPolygon(Poly, x, y):
    Poly_x = Poly[:, 0]
    Poly_y = Poly[:, 1]

    m12 = (Poly_y[0] - Poly_y[1]) / (Poly_x[0] - Poly_x[1])
    m23 = (Poly_y[1] - Poly_y[2]) / (Poly_x[1] - Poly_x[2])
    m34 = (Poly_y[2] - Poly_y[3]) / (Poly_x[2] - Poly_x[3])
    m45 = (Poly_y[3] - Poly_y[4]) / (Poly_x[3] - Poly_x[4])
    m56 = (Poly_y[4] - Poly_y[5]) / (Poly_x[4] - Poly_x[5])
    m16 = (Poly_y[0] - Poly_y[5]) / (Poly_x[0] - Poly_x[5])
    m25 = (Poly_y[1] - Poly_y[4]) / (Poly_x[1] - Poly_x[4])

    if (y >= (x - Poly_x[0]) * m12 + Poly_y[0] and y >= (x - Poly_x[0]) * m16 + Poly_y[0] and y <= (
            x - Poly_x[4]) * m56 + Poly_y[4] and y <= (x - Poly_x[1]) * m25 + Poly_y[1]):
        return True

    elif (y >= (x - Poly_x[1]) * m25 + Poly_y[1] and y <= (x - Poly_x[3]) * m45 + Poly_y[3] and y <= (
            x - Poly_x[2]) * m34 + Poly_y[2] and y >= (x - Poly_x[1]) * m23 + Poly_y[1]):
        return True

    return False


def checkRectangle(rect, x, y):
    rect_x = rect[:, 0]
    rect_y = rect[:, 1]

    m12 = (rect_y[0] - rect_y[1]) / (rect_x[0] - rect_x[1])
    m23 = (rect_y[1] - rect_y[2]) / (rect_x[1] - rect_x[2])
    m34 = (rect_y[2] - rect_y[3]) / (rect_x[2] - rect_x[3])
    m14 = (rect_y[0] - rect_y[3]) / (rect_x[0] - rect_x[3])

    if (y >= (x - rect_x[0]) * m12 + rect_y[0] and y >= (x - rect_x[1]) * m23 + rect_y[1] and y <= (
            x - rect_x[2]) * m34 + rect_y[2] and y <= (x - rect_x[0]) * m14 + rect_y[0]):
        return True

    return False


def checkRhombus(rhom, x, y):
    rhom_x = rhom[:, 0]
    rhom_y = rhom[:, 1]

    m12 = (rhom_y[0] - rhom_y[1]) / (rhom_x[0] - rhom_x[1])
    m23 = (rhom_y[1] - rhom_y[2]) / (rhom_x[1] - rhom_x[2])
    m34 = (rhom_y[2] - rhom_y[3]) / (rhom_x[2] - rhom_x[3])
    m14 = (rhom_y[0] - rhom_y[3]) / (rhom_x[0] - rhom_x[3])

    if (y >= (x - rhom_x[0]) * m12 + rhom_y[0] and y <= (x - rhom_x[1]) * m23 + rhom_y[1] and y <= (
            x - rhom_x[2]) * m34 + rhom_y[2] and y >= (x - rhom_x[0]) * m14 + rhom_y[0]):
        return True

    return False


def checkCircle(circle, x, y):
    a = circle[1][0]
    b = circle[1][1]
    r = circle[0]

    if ((x - a) ** 2 + (y - b) ** 2 <= r ** 2):
        return True
    return False


def checkEllipse(ellipse, x, y):
    A = ellipse[0][0] / 2
    B = ellipse[0][1] / 2

    a = ellipse[1][0]
    b = ellipse[1][1]

    if (((x - a) / A) ** 2 + ((y - b) / B) ** 2 <= 1):
        return True
    return False


def check_node_validity( x, y):
    Poly = coord_Polygon
    rect = coord_rectangle
    rhom = coord_rhombus
    circle = circle
    ellipse = ellipse

    if checkPolygon(Poly, x, y) or checkRectangle(rect, x, y) or checkRhombus(rhom, x, y) or checkCircle(circle, x,
                                                                                            y) or checkEllipse(ellipse,
                                                                                                               x, y):
        return True
pg.init()
window = pg.display.set_mode((300, 200))
R = 4
C = 4
height = 200
width = 300

thresh = R + C
MAP = getMap(window,height,thresh)
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    pg.display.update()
