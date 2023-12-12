from OpenGL.GL import *
from OpenGL.GLUT import *
import random
# Necessary variables
height=800
width=600
buttonX=[]
buttonY=[]
visibleButton=[1]*26
keyboardKeys=[b'a',b'b',b'c',b'd',b'e',
              b'f',b'g',b'h',b'i',b'j',
              b'k',b'l',b'm',b'n',b'o',
              b'p',b'q',b'r',b's',b't',
              b'u',b'v',b'w',b'x',b'y',b'z']
pressedCount=0
word=""
guessed=[]
displayWord=""
wastedLives=0
won=True
hintWord=""
wordList=[]
# Reading txt file for words and hints
with open('words.txt') as f:
   for line in f:
       wordList.append(line[:len(line)-1])
       if 'str' in line:
          break
wordList.pop()

# LAB-1 Point Drawing Algorithm
def draw_points(x, y,size=3):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
# LAB-2 Mid Point Line Algorithm
def midpointLine(x1, y1, x2, y2,size=3):
    zone = getZone(x1, y1, x2, y2)
    mx1, my1, mx2, my2 = convertToZero(x1, y1, x2, y2, zone)
    dx = mx2 - mx1
    dy = my2 - my1
    d = (2 * dy) - dx
    delNE = 2 * (dy - dx)
    delE = 2 * dy
    while mx1 <= mx2 and my1 <= my2:
        convertBack(mx1, my1, zone,size)
        mx1 = mx1 + 1
        if d >= 0:
            my1 = my1 + 1
            d = d + delNE
        else:
            d = d + delE
def getZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy >= 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        elif dx >= 0 and dy < 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy < 0:
            return 6
        elif dx < 0 and dy < 0:
            return 5
def convertToZero(x1, y1, x2, y2, zone):
    if zone == 1:
        nx1 = y1
        ny1 = x1
        nx2 = y2
        ny2 = x2
        return nx1, ny1, nx2, ny2
    elif zone == 2:
        nx1 = y1
        ny1 = -x1
        nx2 = y2
        ny2 = -x2
        return nx1, ny1, nx2, ny2
    elif zone == 3:
        nx1 = -x1
        ny1 = y1
        nx2 = -x2
        ny2 = y2
        return nx1, ny1, nx2, ny2
    elif zone == 4:
        nx1 = -x1
        ny1 = -y1
        nx2 = -x2
        ny2 = -y2
        return nx1, ny1, nx2, ny2
    elif zone == 5:
        nx1 = -y1
        ny1 = -x1
        nx2 = -y2
        ny2 = -x2
        return nx1, ny1, nx2, ny2
    elif zone == 6:
        nx1 = -y1
        ny1 = x1
        nx2 = -y2
        ny2 = x2
        return nx1, ny1, nx2, ny2
    elif zone == 7:
        nx1 = x1
        ny1 = -y1
        nx2 = x2
        ny2 = -y2
        return nx1, ny1, nx2, ny2
    elif zone == 0:
        nx1 = x1
        ny1 = y1
        nx2 = x2
        ny2 = y2
        return nx1, ny1, nx2, ny2
def convertBack(x1, y1, zone,size):
    glPointSize(size)
    glBegin(GL_POINTS)
    if zone == 1:
        glVertex2f(y1, x1)
    elif zone == 2:
        glVertex2f(-y1, x1)
    elif zone == 3:
        glVertex2f(-x1, y1)
    elif zone == 4:
        glVertex2f(-x1, -y1)
    elif zone == 5:
        glVertex2f(-y1, -x1)
    elif zone == 6:
        glVertex2f(y1, -x1)
    elif zone == 7:
        glVertex2f(x1, -y1)
    elif zone == 0:
        glVertex2f(x1, y1)
    glEnd()
# LAB-3 Mid Point Circle Algorithm
def circle(x1,y1,r):
   x=r
   y=0
   d=0
   while(x>=y):
       draw_points(x1+x,y1+y)
       draw_points(x1+y,y1+x)
       draw_points(x1-y,y1+x)
       draw_points(x1-x,y1+y)
       draw_points(x1-x,y1-y)
       draw_points(x1-y,y1-x)
       draw_points(x1+y,y1-x)
       draw_points(x1+x,y1-y)
       if(d<=0):
           y=y+1
           d=d+2*y+1
       if(d>0):
           x=x-1
           d=d-2*x+1

# Draw text function font size 18
def drawText(text,x,y):
    glColor3fv((0,0,0))
    glWindowPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(fonts.GLUT_BITMAP_HELVETICA_18, ord(ch))
# Draw text function font size 24
def drawTextL(text,x,y):
    glColor3fv((0,0,0))
    glWindowPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(fonts.GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))
# Use of Mid Point Circle Algorithm
def drawCircleButtons():
    global buttonX
    global buttonY
    buttonX=[]
    buttonY=[]
    buttonStartX = 60
    buttonStartY = 300
    for i in range(2):
        for j in range(13):
            buttonX.append(buttonStartX + j * 50 + 30)
            buttonY.append(buttonStartY - i * 80)
            if visibleButton[j+i*13] == 1:
                circle(buttonStartX + j * 50 + 30, buttonStartY - i * 80, 20)
# Use of Mid Point Line Algorithm
def drawPole():
    midpointLine(130, 570, 130, 350, 7)
    midpointLine(115, 560, 220, 560, 7)
    midpointLine(115, 530, 160, 570, 7)
    midpointLine(200, 525, 200, 560, 5)
# Use of text render
def drawTextOnButton():
    global buttonX
    global buttonY
    for i in range(0,len(buttonX)):
        if visibleButton[i]==1:
            drawText(chr(65+i),buttonX[i]-5,buttonY[i]-5)
# Use of Point, Mid Point Line and Mid Point Circle Algorithm
def drawHangman():
    if wastedLives>0: #Head
        circle(200,500,25)
        midpointLine(200, 498, 200, 490)
        midpointLine(193, 486, 207, 486)
        draw_points(210, 505, 6)
        draw_points(190, 505, 6)
    if wastedLives>1: #Body
        midpointLine(200,475 , 200, 420)
    if wastedLives>2: #Lleg
        midpointLine(170, 380, 200, 420)
    if wastedLives>3: #Rleg
        midpointLine(230, 380, 200, 420)
    if wastedLives>4: #Lhand
        midpointLine(170, 440, 200, 460)
    if wastedLives>5: #Rhand
        midpointLine(230, 440, 200, 460)#right hand
# Use of Mid Point Line Algorithm
def drawBox():
    midpointLine(40, 580, 40, 20,8)
    midpointLine(40, 580, 760, 580, 8)
    midpointLine(760, 580, 760, 20, 8)
    midpointLine(40, 20, 760, 20, 8)
    midpointLine(40, 180, 760, 180, 8)
# Use of text rendering
def drawInfo():
    data=["CSE-423 Sec:6 Group:7:","Tahzib Azad - 19101464",
          "Shakib Al Hasan - 19201049",
          "Asit Kumar - 20301247",
          "Fairuz Anika - 20301464"]
    for i in range(len(data)):
        drawTextL(data[i], 210, 150-i*25)
# OPENGL Necessities
def draw():
    drawBox()
    drawInfo()
    if pressedCount==0:
        drawTextL("Press 'SPACE' key to start the Game!!!", 200, 330)
    if not won and wastedLives!=6:
        drawPole()
        drawCircleButtons()
        drawTextOnButton()
        drawTextL("HINT: "+hintWord, 370, 480)
        drawTextL(displayWord,380,440)
        drawHangman()
    if won and wastedLives<6 and len(guessed)>0:
        drawTextL("You Won!", 330, 350)
        drawTextL("Good Job!!", 325, 300)
        drawTextL("Press 'Space' key for restart..", 275, 250)
    if wastedLives==6:
        drawTextL("Ouch!! You Lost!", 310, 350)
        drawTextL("Study harder!!", 325, 300)
        drawTextL("Press 'Space' key for restart..", 265, 250)
# OPENGL Necessities
def iterate():
    glViewport(0, 0, height, width)
    glMatrixMode(GL_PROJECTION)
    try:
       glPushMatrix()
    except:
        glPopMatrix()
        glPopMatrix()
    glLoadIdentity()
    glOrtho(0.0, height, 0.0, width, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
# OPENGL Necessities
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    try:
       glPopMatrix()
    except:
        pass
    glClearColor(255,255,255,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    gameLogic()
    draw()
    glutSwapBuffers()
# Event handler for keyboard press
def onButtonPress(key, x, y):
    global wastedLives,won,pressedCount
    if key==b' ' and (wastedLives==6 or (pressedCount>0 and won==True)):
        resetGame()
    elif wastedLives ==6:
        return
    if key==b' ' or pressedCount>0:
        pressedCount+=1
    else:
        return
    for i in range(len(keyboardKeys)):
        if key==keyboardKeys[i]:
            if chr(65+i) not in word and chr(65+i) not in guessed:
                wastedLives+=1
            guessed.append(chr(65+i))
            visibleButton[i]=0
    won=True
    for letter in word:
        if letter not in guessed:
            won=False
            break
    glutPostRedisplay()
# Game related logics
def gameLogic():
    global displayWord
    displayWord=""
    for letter in word:
        if letter in guessed:
            displayWord+= letter+" "
        else:
            displayWord+="_ "
# Reset function for the game
def resetGame():
    global word,displayWord,guessed,visibleButton
    global pressedCount,wastedLives,hintWord,wordList
    randomChoice=random.choice(wordList).split('_')
    word=randomChoice[0]
    hintWord=randomChoice[1]
    displayWord=""
    guessed=[]
    visibleButton = [1] * 26
    pressedCount=0
    wastedLives=0

# Main run
resetGame()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(height,width)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"HANGMAN BRACU CSE EDITION")
glutDisplayFunc(showScreen)
glutKeyboardFunc(onButtonPress)
glutMainLoop()