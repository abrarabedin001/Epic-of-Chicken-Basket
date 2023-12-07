from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from project import draw_any_line





def draw_x():
    x_origin = 220
    y_origin = 240
    glColor3f(255 / 256, 0 / 256, 0 / 256)

    draw_any_line(x_origin,y_origin,x_origin+20,y_origin-20)
    draw_any_line(x_origin, y_origin-20, x_origin + 20, y_origin )
def draw_pause():
    global pause
    x_origin = -5
    y_origin = 240
    glColor3f(255 / 256, 191 / 256, 0 / 256)

    if(pause==False):

        draw_any_line(x_origin,y_origin,x_origin,y_origin-20)
        draw_any_line(x_origin+10, y_origin, x_origin + 10, y_origin-20 )
    else:
        draw_any_line(x_origin, y_origin, x_origin, y_origin - 20)
        draw_any_line(x_origin , y_origin, x_origin + 20, y_origin - 10)
        draw_any_line(x_origin + 20, y_origin - 10, x_origin , y_origin - 20)
def draw_play():
    x_origin = -230
    y_origin = 230
    # 255, 191, 0

    glColor3f(0, 128 / 256, 128 / 256)

    global stop,diamondY
    draw_any_line(x_origin, y_origin, x_origin+9, y_origin+9)
    draw_any_line(x_origin , y_origin, x_origin +9, y_origin -9)
    draw_any_line(x_origin , y_origin, x_origin +20, y_origin )