import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.config import GameConfig
from modules.config import config




def convert_coordinate(x, y):
    a = x - (config.W_Width / 2)
    b = (config.W_Height / 2) - y
    return a, b

def keyboardListener(key, x, y):
    if key == b'w':
        config.ball_size += 1
    if key == b's':
        config.ball_size -= 1
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    if key == GLUT_KEY_UP:
        config.speed *= 2
    if key == GLUT_KEY_DOWN:
        config.speed /= 2
    if not config.pause and not config.stop:
        if key == GLUT_KEY_RIGHT and config.boatX + 100 <= 249:
            config.boatX += 5
        if key == GLUT_KEY_LEFT and config.boatX >= -249:
            config.boatX -= 5
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        c_X, c_y = convert_coordinate(x, y)
        config.ballx, config.bally = c_X, c_y

        if -20 <= x-250 <= 20 and 210 <= 250-y <= 240:
            config.pause = not config.pause
        elif -230 <= x-250 <= -210 and 210 <= 250-y <= 240:
            config.stop = False
            config.diamondX = config.chickenX
            config.diamondY = config.chickenY+config.birdY_offset
            config.speed = 1
            print(f"Starting Over! Score: {config.points}")
            config.end = False
            config.points = 0
        
        elif 210 <= x-250 <= 250 and 210 <= 250-y <= 240:
            print(f"Goodbye! Score: {config.points}")
            config.end = True
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        config.create_new = convert_coordinate(x, y)
    glutPostRedisplay()


def mouseListener_stage2(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
         # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP

        c_X, c_y = convert_coordinate(x, y)
        config.ballx, config.bally = c_X, c_y

        if -20 <= x-250 <= 20 and 210 <= 250-y <= 240:
            config.pause = not config.pause
        elif -230 <= x-250 <= -210 and 210 <= 250-y <= 240:
            config.stop = False
            config.diamondX = config.chickenX
            config.diamondY = config.chickenY+config.birdY_offset
            config.speed = 1
            print(f"Starting Over! Score: {config.points}")
            config.end = False
            config.points = 0
            
        elif 210 <= x-250 <= 250 and 210 <= 250-y <= 240:
            print(f"Goodbye! Score: {config.points}")
            config.end = True
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            create_new = convert_coordinate(x,y)
            c_x, c_y = convert_coordinate(x, y)
            if(config.pause==False):
                config.centers.append([round(c_x),round(c_y)])
                config.radiuses.append(10)
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()
