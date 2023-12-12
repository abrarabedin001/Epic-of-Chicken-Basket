from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import math

catcherX = 200
catcherY = 30
eggX = random.randint(50, 350)
eggY = 500
eggStop = False
BackButtonChk = False
PlayButtonChk = False
CrossButtonChk = False
gameScore = 0
fallingSpeed = 1
paused = False
missiles = []

def MidPointLine(zone, x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    x = x1
    y = y1
    dInitial = 2 * dy - dx
    Del_E = 2 * dy
    Del_NE = 2 * (dy - dx)

    while x <= x2:
        a, b = ConvertToOriginal(zone, x, y)
        drawpoints(a, b)
        if dInitial <= 0:
            x = x + 1
            dInitial = dInitial + Del_E
        else:
            x = x + 1
            y = y + 1
            dInitial = dInitial + Del_NE


def FindZone(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 < dy:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 < dy:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def ConvertToZoneZero(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def ConvertToOriginal(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def Line(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)


class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self):
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x - 3, self.y - 10)
        glVertex2f(self.x + 3, self.y - 10)
        glEnd()

def plane():
    glColor3f(1, 1, 1)
    planeWidth = 80
    planeHeight = 20

    # Fuselage of the plane
    Line(catcherX - planeWidth / 2, catcherY, catcherX + planeWidth / 2, catcherY)
    Line(catcherX - planeWidth / 4, catcherY, catcherX - planeWidth / 4, catcherY - planeHeight)
    Line(catcherX + planeWidth / 4, catcherY, catcherX + planeWidth / 4, catcherY - planeHeight)

    # Wings of the plane
    wingWidth = 40
    wingHeight = 8
    Line(catcherX - wingWidth, catcherY - planeHeight / 2, catcherX + wingWidth, catcherY - planeHeight / 2)
    Line(catcherX - wingWidth / 2, catcherY - planeHeight / 2, catcherX + wingWidth / 2, catcherY - planeHeight / 2)

    # Tail of the plane
    tailWidth = 10
    tailHeight = 15
    Line(catcherX - tailWidth / 2, catcherY, catcherX - tailWidth / 2, catcherY - tailHeight)
    Line(catcherX + tailWidth / 2, catcherY, catcherX + tailWidth / 2, catcherY - tailHeight)


def egg():
    glColor3f(1, 0, 1)
    global eggX, eggY, catcherX, catcherY
    global fallingSpeed, gameScore, eggStop

    # Draw egg shape using gl points
    glBegin(GL_POINTS)
    for i in range(360):
        angle_rad = math.radians(i)
        x = eggX + 5 * math.cos(angle_rad)
        y = eggY - 10 * math.sin(angle_rad)
        glVertex2f(x, y)
    glEnd()

    eggY = (eggY - fallingSpeed)

    if eggY - 20 < catcherY and catcherX - 50 <= eggX <= catcherX + 50:
        eggX = random.randint(100, 350)
        eggY = 600
        gameScore = gameScore + 1
        fallingSpeed = fallingSpeed + 1
        print("Game Score: ", gameScore)
    elif eggY - 20 < 0:
        fallingSpeed = 0
        eggY = 20
        totalScore = gameScore
        gameScore = 0
        eggStop = True
        print('======================')
        print("Game Over!")
        print("Total Score: ", totalScore)


def play_button():
    glColor3f(0, 1, 0)
    Line(200, 580, 220, 570)
    Line(200, 560, 220, 570)


def back_button():
    Line(10, 570, 30, 570)
    Line(10, 570, 20, 580)
    Line(10, 570, 20, 560)


def cross_button():
    Line(390, 580, 370, 560)
    Line(370, 580, 390, 560)


def pause_resume_button():
    glColor3f(1, 1, 1)
    Line(190, 580, 190, 560)
    Line(210, 580, 210, 560)


def specialKeyboardListener(key, x, y):
    global catcherX
    if key == GLUT_KEY_LEFT:
        catcherX = max(45, catcherX - 10)
    elif key == GLUT_KEY_RIGHT:
        catcherX = min(360, catcherX + 10)
    glutPostRedisplay()


def keyboardListener(key, x, y):
    if key == b' ':
        shoot_missile()



def mouseListener(button, state, x, y):
    global BackButtonChk, CrossButtonChk, PlayButtonChk, diamondStop, gameScore, paused
    converted_y = 600 - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= x <= 30 and 560 <= converted_y <= 580:
            BackButtonChk = True
            reset_game()
        elif 370 <= x <= 390 and 560 <= converted_y <= 580:
            CrossButtonChk = True
        elif 200 - 10 <= x <= 220 + 10 and 560 <= converted_y <= 580:
            PlayButtonChk = not PlayButtonChk
            paused = not paused
        glutPostRedisplay()


def reset_game():
    global diamondStop, gameScore, diamondY, catcherX
    diamondStop = False
    gameScore = 0
    diamondY = 500
    catcherX = 350


def timer(value):
    global missiles
    if not paused:
        for missile in missiles:
            missile.move()
        glutPostRedisplay()
    glutTimerFunc(16, timer, 0)


def drawpoints(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 400, 600)
    glOrtho(0.0, 400, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def is_collision(eggX, eggY, catcherX, catcherY):
    # Simple rectangular collision check
    return (
        catcherX - 40 <= eggX <= catcherX + 40 and
        catcherY - 20 <= eggY <= catcherY + 20
    )




def display():
    global missiles, eggStop, gameScore, eggX, eggY, fallingSpeed, catcherX, catcherY

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    for missile in missiles:
        missile.draw()

    if eggStop:
        glColor3f(1, 0, 0)
        egg()
        glColor3f(1, 1, 1)
        glRasterPos2f(150, 300)  # Position of "Game Over" text
        game_over_str = "Game Over!"
        for char in game_over_str:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glRasterPos2f(160, 280)  # Position of score in "Game Over" screen
        score_str = "Total Score: {}".format(gameScore)
        for char in score_str:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    else:
        glColor3f(1, 1, 1)
        plane()

        glColor3f(1, 1, 0)
        egg()

        for missile in missiles:
            if (
                missile.x >= eggX - 5
                and missile.x <= eggX + 5
                and missile.y >= eggY - 10
                and missile.y <= eggY
            ):
                gameScore += 1  # Increase score by 1
                eggX = random.randint(100, 350)
                eggY = 600
                fallingSpeed += 1  # Increase falling speed
                print("Game Score: ", gameScore)

        if is_collision(eggX, eggY, catcherX, catcherY):
            fallingSpeed = 0
            totalScore = gameScore
            gameScore = 0
            eggStop = True
            print('======================')
            print("Game Over!")
            print("Total Score: ", totalScore)

        if BackButtonChk:
            glColor3f(0, 0, 1)
            back_button()
            eggY = 600
            gameScore = 0
            fallingSpeed = 1  # Reset falling speed
        else:
            glColor3f(0, 0, 1)
            back_button()

        if CrossButtonChk:
            cross_button()
            glutLeaveMainLoop()
        else:
            glColor3f(1, 0, 0)
            cross_button()

        if PlayButtonChk:
            play_button()

        if not paused:
            pause_resume_button()

        # Display the score in the corner of the screen
        glColor3f(1, 1, 1)
        glRasterPos2f(10, 580)  # Position of the score
        score_str = "Score: {}".format(gameScore)
        for char in score_str:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))

    glutSwapBuffers()



def shoot_missile():
    global catcherX, catcherY, missiles
    missile = Missile(catcherX, catcherY)
    missiles.append(missile)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(400, 600)
glutInitWindowPosition(1000, 250)
wind = glutCreateWindow(b"Diamond Catcher Game")
glutTimerFunc(0, timer, 0)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyboardListener)
glutKeyboardFunc(keyboardListener)
glutDisplayFunc(display)
glutMainLoop()


