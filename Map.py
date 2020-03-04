import pygame as pg


def getMap(image,height):
    blue = (0, 0, 255)
    white = (255, 255, 255)
    image.fill(white)
    coord_Polygon = [(20 , height - (120 )),
                  (25 , height - (185 )),
                  (75 , height - (185 )),
                  (100 , height - (150 )),
                  (75 , height - (120 )),
                  (50 , height - (150 ))]
    coord_rectangle = [(30 , height - (67.5 )),
                  (35 , height - (76)),
                  (100 , height - (38.6)),
                  (95 , height - (30))]

    coord_rhombus = [(225, height - (40)),
                  (250 ,height - 25),
                  (225, height - (10 )),
                  (200 , height - 25)]
    poly1 = pg.draw.polygon(image, blue, coord_Polygon, 0)
    poly2 = pg.draw.polygon(image, blue, coord_rectangle, 0)
    poly3 = pg.draw.polygon(image, blue, coord_rhombus, 0)
    circle = pg.draw.circle(image, blue, (225, 50), 25, 0)
    ellipse = pg.draw.ellipse(image, blue, (110, 80, 80 , 40 ), 0)
    Map_ = [poly1, poly2, poly3, circle, ellipse]
    return Map_




pg.init()
window = pg.display.set_mode((300, 200))
Radius = 0
Clearance = 0
height = 200
width = 300

rigid = Radius + Clearance
MAP = getMap(window,height)
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    pg.display.update()
