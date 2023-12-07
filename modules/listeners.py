import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b

def keyboardListener(key, x, y):
    global ball_size
    if key == b'w':
        ball_size += 1
        # print("Size Increased")
    if key == b's':
        ball_size -= 1

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed,boatX
    if key == 'w':
        print(1)
    if key == GLUT_KEY_UP:
        speed *= 2
        # print("Speed Increased")
    if key == GLUT_KEY_DOWN:  # // up arrow key
        speed /= 2
        # print("Speed Decreased")
    glutPostRedisplay()
    if(pause!=True and stop !=True):
        if key==GLUT_KEY_RIGHT:
            if(boatX+60<=249):
                boatX+=5
        if key==GLUT_KEY_LEFT:
            if(boatX>=-249):

                boatX-=5

def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global ballx, bally,speed, create_new, end,pause,stop,points , diamondY,diamondX
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):  # // 2 times?? in ONE click? -- solution is checking DOWN or UP


            # print(x-250, 250-y)
            c_X, c_y = convert_coordinate(x, y)
            ballx, bally = c_X, c_y

            if(x-250>=-20 and x-250<=20):
                if (250-y>=210 and 250-y<=240):

                    if pause:
                        pause = False
                    else:
                        pause = True
            # print(pause)
            if(x-250>=-230 and x-250 <= -210):
                # print("x is correct")
                if (250-y>=210 and 250-y<=240):
                    # print("y is correct")

                    stop = False
                    diamondY = 230
                    speed = 0.01

                    print("Starting Over! Score:"+str(points))
                    points = 0
                    diamondX = random.randint(-230,230)
            if (x - 250 >= 210 and x - 250 <= 250):
                # print("x is correct")
                if (250 - y >= 210 and 250 - y <= 240):
                    # print("y is correct")


                    print("Goodbye! Score:" + str(points))
                    end = True


    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            create_new = convert_coordinate(x, y)
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()
