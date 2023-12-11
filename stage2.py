import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.stage1animate import stage1animate
from modules.listeners import keyboardListener, mouseListener_stage2
from modules.listeners import mouseListener
from modules.listeners import specialKeyListener
import math
from modules.playPauseX import draw_pause, draw_play, draw_x
from modules.shapes import draw_boat, draw_bucket, draw_chicken2, draw_circle, draw_diamond
from modules.config import config
from modules.stage2animate import stage2animate
from modules.straightline import draw_points




def display():
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
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    
    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    # draw_bucket()    
    draw_chicken2()

    print(config.centers)
    for r in range(len(config.centers) - 1, -1, -1):
        x_origin = config.centers[r][0]
        y_origin = config.centers[r][1]

        x_arr, y_arr = draw_circle(x_origin, y_origin, config.radiuses[r], config.boundary_x_min, config.boundary_x_max, config.boundary_y_min,
                                   config.boundary_y_max)

        if x_arr is None:
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
        return
    glutSwapBuffers()


def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104, 1, 1, 1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance

glutInit()
glutInitWindowSize(config.W_Width, config.W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display) 


 # display callback function
glutIdleFunc(stage2animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener_stage2)

glutMainLoop()
    # return something
    # The main loop of OpenGL


