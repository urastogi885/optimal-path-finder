import pygame as pg


def getMap(image,height,rigid):
    blue = (0, 0, 255)
    white = (255, 255, 255)
    image.fill(white)
    coord_Polygon = [(20 - rigid, height - (120 - rigid)),
                  (25 - rigid, height - (185 + rigid)),
                  (75 + rigid, height - (185 + rigid)),
                  (100 + rigid, height - (150 + rigid)),
                  (75 + rigid, height - (120 - rigid)),
                  (50 + rigid, height - (150 - rigid))]
    coord_rectangle = [(30 - rigid, height - (67.5 + rigid)),
                  (35 + rigid, height - (76 + rigid)),
                  (100 + rigid, height - (38.6 -rigid)),
                  (95 - rigid, height - (30 - rigid))]

    coord_rhombus = [(225, height - (40 + rigid)),
                  (250 + rigid,height - 25),
                  (225, height - (10 - rigid)),
                  (200 - rigid, height - 25)]
    poly1 = pg.draw.polygon(image, blue, coord_Polygon, 0)
    poly2 = pg.draw.polygon(image, blue, coord_rectangle, 0)
    poly3 = pg.draw.polygon(image, blue, coord_rhombus, 0)
    circle = pg.draw.circle(image, blue, (225, height - 125), 25 + rigid, 0)
    ellipse = pg.draw.ellipse(image, blue, (150, height - 100, 80 + rigid, 40 + rigid), 0)
    Map_ = [poly1, poly2, poly3, circle, ellipse]
    return Map_




pg.init()
window = pg.display.set_mode((300, 200))
Radius = 0
Clearance = 0
height = 200
width = 300

rigid = Radius + Clearance
MAP = getMap(window,height,rigid)
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    pg.display.update()
