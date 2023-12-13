import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat,  draw_chicken2, draw_circle, draw_diamond, draw_roman_ii
from modules.config import config
from modules.straightline import  draw_points



def display2():
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);  # //color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?

    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    
    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    # draw_bucket()    
    draw_chicken2()
    draw_roman_ii()

    
    for r in range(len(config.centers) - 1, -1, -1):
        x_origin = config.centers[r][0]
        y_origin = config.centers[r][1]

        x_arr, y_arr = draw_circle(x_origin, y_origin, config.radiuses[r], config.boundary_x_min, config.boundary_x_max, config.boundary_y_min,
                                   config.boundary_y_max)

        if x_arr is None:
            print('Score: ' + str(config.get_points()))
            del config.radiuses[r]
            del config.centers[r]  # Remove the element from the list
        else:
            for i in range(len(x_arr)):
                draw_points(x_arr[i], y_arr[i], 3)

    if (config.create_new):
        m, n = config.create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()
    if (config.end):
        config.speed = 1
        glutLeaveMainLoop()
    glutSwapBuffers()

