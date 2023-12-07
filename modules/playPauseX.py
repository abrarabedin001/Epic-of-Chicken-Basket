from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.straightline import draw_points, draw_any_line
from modules.config import config



def draw_x():
    x_origin = 220
    y_origin = 240
    glColor3f(255 / 256, 0 / 256, 0 / 256)
    draw_any_line(x_origin, y_origin, x_origin+20, y_origin-20)
    draw_any_line(x_origin, y_origin-20, x_origin+20, y_origin)

def draw_pause():
    x_origin = -5
    y_origin = 240
    glColor3f(255 / 256, 191 / 256, 0 / 256)

    if not config.get_pause_status():
        draw_any_line(x_origin, y_origin, x_origin, y_origin-20)
        draw_any_line(x_origin+10, y_origin, x_origin+10, y_origin-20)
    else:
        draw_any_line(x_origin, y_origin, x_origin, y_origin-20)
        draw_any_line(x_origin, y_origin, x_origin+20, y_origin-10)
        draw_any_line(x_origin+20, y_origin-10, x_origin, y_origin-20)

def draw_play():
    x_origin = -230
    y_origin = 230
    glColor3f(0, 128 / 256, 128 / 256)

    draw_any_line(x_origin, y_origin, x_origin+9, y_origin+9)
    draw_any_line(x_origin, y_origin, x_origin+9, y_origin-9)
    draw_any_line(x_origin, y_origin, x_origin+20, y_origin)
