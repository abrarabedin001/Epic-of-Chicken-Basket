import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.display1 import display1
from modules.display2 import display2
from modules.stage1animate import stage1animate
from modules.stage2animate import stage2animate
from modules.listeners import keyboardListener, mouseListener_stage2,mouseListener_stage1

from modules.listeners import specialKeyListener
from modules.config import config

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

def display():
  if (config.stage == 1):
      display1()
  else:
      display2()


def mouseListener(button, state, x, y):
    if (config.stage == 1):
        mouseListener_stage1(button, state, x, y)
    else:
        mouseListener_stage2(button, state, x, y)
def animate():
    if (config.stage == 1):
        stage1animate()
    else:
        stage2animate()



 # display callback function

# if (config.stage == 1):
glutDisplayFunc(display) 
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)


glutMainLoop()
   


