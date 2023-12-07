import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500, 500
diamondY = 250
diamondX = random.randint(-230,230)
boatX = -250
boatY = -230
ballx = bally = 0
speed = 0.01
ball_size = 2
points = 0
create_new = False
pause = False
stop = False
randomR = random.randint(0,255)/255
randomG = random.randint(0,255)/255
randomB = random.randint(0,255)/255
end = False
# Global variable to keep track of the last time we switched
last_switch_time = time.time()

# Variable to determine which chicken to draw
draw_first_wing = True
chickenX = 0
chickenY = 0
# speed = 1
frame_count = 0



class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


def crossProduct(a, b):
    result = point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x

    return result


def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b


def draw_points(x, y, s):
    glPointSize(s)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()

def determine_zone(x0, y0, x1, y1):
    """
    Determine the zone of a line based on the start and end points.
    Zones:
        0: East to North-East
        1: North-East to North
        2: North to North-West
        3: North-West to West
        4: West to South-West
        5: South-West to South
        6: South to South-East
        7: South-East to East
    """
    dx = x1 - x0
    dy = y1 - y0

    # Handle horizontal lines
    if dy == 0:
        return 7 if dx > 0 else 3

    # Handle vertical lines
    if dx == 0:
        return 1 if dy > 0 else 5

    if(abs(dx)>=abs(dy)):
        if(dx>0 and dy>0):
            return 0
        if (dx < 0 and dy > 0):
            return 3
        if (dx < 0 and dy < 0):
            return 4
        if (dx > 0 and dy < 0):
            return 7
    else:
        if (dx > 0 and dy > 0):
            return 1
        if (dx < 0 and dy > 0):
            return 2
        if (dx < 0 and dy < 0):
            return 5
        if (dx > 0 and dy < 0):
            return 6


def convert_to_zone_0(x, y, zone):
    """
    Convert the coordinates from a given zone to zone 0 coordinates.
    """
    # print("zone:",zone)
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
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
    else:
        raise ValueError("Invalid zone")


def mid_point_line(x0, y0, x1, y1):
    """Draw line using the midpoint line algorithm."""
    # if (x0>x1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    # print('ki hoise?')

    d = 2 * dy - dx
    incrE = 2 * dy
    incrNE = 2 * (dy - dx)

    x = x0
    y = y0
    points.append((x, y))
    # print("d: ",d)
    # print('x0: ',x0)
    # print('x1: ',x1)

    while x <= x1:
        # print(""d)
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        points.append((x, y))

    return points
def convert_from_zone_0(x, y, zone):
    """
    Convert the coordinates from zone 0 to a given zone.
    """
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
        return y, -x
    elif zone == 7:
        return x, -y
    else:
        raise ValueError("Invalid zone")
def draw_any_line(x0, y0, x1, y1):

    zone = determine_zone(x0, y0, x1, y1)

    x0_z0, y0_z0 = convert_to_zone_0(x0, y0, zone)

    x1_z0, y1_z0 = convert_to_zone_0(x1, y1, zone)

    line_points_z0 = mid_point_line(x0_z0, y0_z0, x1_z0, y1_z0)
    # [(x,y){}]

    # Convert the line points back to the original zone
    line_points = [convert_from_zone_0(x, y, zone) for x, y in line_points_z0]
    for point in line_points:
        draw_points(point[0], point[1], 1)
    return line_points




def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250, 0)
    glVertex2f(-250, 0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, 250)
    glVertex2f(0, -250)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 1.0, 0.0)
    glVertex2f(0, 0)

    glEnd()





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
def draw_x():
    x_origin = 220
    y_origin = 240
    glColor3f(255 / 256, 0 / 256, 0 / 256)

    draw_any_line(x_origin,y_origin,x_origin+20,y_origin-20)
    draw_any_line(x_origin, y_origin-20, x_origin + 20, y_origin )
def draw_pause():
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
def draw_diamond():
    global diamondY,randomR,randomG,randomB
    x_origin = diamondX
    y_origin = diamondY
    # 0,128,

    glColor3f(randomR, randomG, randomB)


    draw_any_line(x_origin, y_origin, x_origin+9, y_origin+9)
    draw_any_line(x_origin , y_origin, x_origin +9, y_origin -9)
    draw_any_line(x_origin +10, y_origin+9,x_origin+18, y_origin+1  )
    draw_any_line(x_origin +10, y_origin-9 ,x_origin+18, y_origin-1)


bucketX = -50
bucketY = 50
def draw_bucket():
    global bucketX, bucketY
    x_origin = bucketX
    y_origin = bucketY

    # Set bucket color
    glColor3f(0.5, 0.5, 0.5)  # Grey color

    # Base of the bucket
    draw_any_line(x_origin - 30, y_origin - 30, x_origin + 30, y_origin - 30)

    # Left side of the bucket
    for i in range(-30, 30, 2):
        draw_any_line(x_origin - 30, y_origin + i, x_origin - 28, y_origin + i + 2)

    # Right side of the bucket
    for i in range(-30, 30, 2):
        draw_any_line(x_origin + 30, y_origin + i, x_origin + 28, y_origin + i + 2)

    # Top of the bucket
    draw_any_line(x_origin - 28, y_origin + 30, x_origin + 28, y_origin + 30)

    # Handle of the bucket
    draw_any_line(x_origin - 20, y_origin + 40, x_origin + 20, y_origin + 40)
    draw_any_line(x_origin - 20, y_origin + 40, x_origin - 20, y_origin + 30)
    draw_any_line(x_origin + 20, y_origin + 40, x_origin + 20, y_origin + 30)
def draw_ellipse(x_origin, y_origin, x_radius, y_radius, start_angle, end_angle, angle_step):
    for angle in range(start_angle, end_angle, angle_step):
        x = x_origin + x_radius * math.cos(math.radians(angle))
        y = y_origin + y_radius * math.sin(math.radians(angle))
        draw_points(x, y,1)
def draw_wings2(x_origin, y_origin):
    # Adjust the wing size and angles as needed
    wing_radius_x = 20
    wing_radius_y = 30
    # Left wing
    draw_ellipse(x_origin - wing_radius_x, y_origin, wing_radius_x, wing_radius_y, 45, 135, 5)
    # Right wing
    draw_ellipse(x_origin + wing_radius_x, y_origin, wing_radius_x, wing_radius_y, 45, 135, 5)

def draw_boat():
    global boatX,boatY
    x_origin = boatX
    y_origin = boatY
    if(stop==False):
        glColor3f(255/255, 255 / 255, 255 / 255)
    else:
        glColor3f(255/255, 0 / 255, 0 / 255)


    draw_any_line(x_origin, y_origin, x_origin + 60, y_origin )
    draw_any_line(x_origin+5, y_origin-11, x_origin + 55, y_origin-11)
    draw_any_line(x_origin , y_origin, x_origin + 5, y_origin-10)
    draw_any_line(x_origin + 60, y_origin , x_origin + 55, y_origin-10)
def draw_wings(x_origin, y_origin):
    # Drawing the left wing
    for angle in range(45, 135, 10):
        x = x_origin - 20 * math.cos(math.radians(angle))
        y = y_origin - 10 + 20 * math.sin(math.radians(angle))
        next_x = x_origin - 20 * math.cos(math.radians(angle + 10))
        next_y = y_origin - 10 + 20 * math.sin(math.radians(angle + 10))
        draw_any_line(x, y, next_x, next_y)

    # Drawing the right wing
    for angle in range(45, 135, 10):
        x = x_origin + 20 * math.cos(math.radians(angle))
        y = y_origin - 10 + 20 * math.sin(math.radians(angle))
        next_x = x_origin + 20 * math.cos(math.radians(angle + 10))
        next_y = y_origin - 10 + 20 * math.sin(math.radians(angle + 10))
        draw_any_line(x, y, next_x, next_y)
def draw_chicken():
    global chickenX, chickenY
    x_origin = chickenX
    y_origin = chickenY

    # Set chicken color
    glColor3f(1.0, 1.0, 0.0)  # Yellow color

    # Draw the body of the chicken
    draw_any_line(x_origin, y_origin, x_origin + 20, y_origin)
    draw_any_line(x_origin, y_origin, x_origin, y_origin - 30)
    draw_any_line(x_origin, y_origin - 30, x_origin + 20, y_origin - 30)
    draw_any_line(x_origin + 20, y_origin, x_origin + 20, y_origin - 30)

    # Draw the head of the chicken
    draw_any_line(x_origin + 20, y_origin - 10, x_origin + 30, y_origin - 10)
    draw_any_line(x_origin + 20, y_origin - 20, x_origin + 30, y_origin - 20)
    draw_any_line(x_origin + 20, y_origin - 10, x_origin + 20, y_origin - 20)
    draw_any_line(x_origin + 30, y_origin - 10, x_origin + 30, y_origin - 20)

    # Draw the legs of the chicken
    draw_any_line(x_origin + 5, y_origin - 30, x_origin + 5, y_origin - 40)
    draw_any_line(x_origin + 15, y_origin - 30, x_origin + 15, y_origin - 40)
def draw_chicken2():
    global chickenX, chickenY
    x_origin = chickenX +30
    y_origin = chickenY +30

    # Set color for the chicken
    glColor3f(1, 1, 0)  # Yellow color

    # Body of the chicken (ellipse-like shape)
    for angle in range(0, 360, 10):
        x = x_origin + 20 * math.cos(math.radians(angle))
        y = y_origin + 30 * math.sin(math.radians(angle))
        next_x = x_origin + 20 * math.cos(math.radians(angle + 10))
        next_y = y_origin + 30 * math.sin(math.radians(angle + 10))
        draw_any_line(x, y, next_x, next_y)

    # Head of the chicken (smaller ellipse)
    for angle in range(0, 360, 30):
        x = x_origin + 30 + 10 * math.cos(math.radians(angle))
        y = y_origin + 40 + 15 * math.sin(math.radians(angle))
        next_x = x_origin + 30 + 10 * math.cos(math.radians(angle + 30))
        next_y = y_origin + 40 + 15 * math.sin(math.radians(angle + 30))
        draw_any_line(x, y, next_x, next_y)

    # Beak of the chicken (triangle)
    draw_any_line(x_origin + 40, y_origin + 40, x_origin + 50, y_origin + 42)
    draw_any_line(x_origin + 50, y_origin + 42, x_origin + 40, y_origin + 44)
    draw_any_line(x_origin + 40, y_origin + 44, x_origin + 40, y_origin + 40)

    # Legs of the chicken (lines)
    # Legs of the chicken (lines)
    draw_any_line(x_origin, y_origin - 30, x_origin - 10, y_origin - 50)
    draw_any_line(x_origin, y_origin - 30, x_origin + 10, y_origin - 50)

    # Feet of the chicken (small lines from the end of the legs)
    draw_any_line(x_origin - 10, y_origin - 50, x_origin - 15, y_origin - 55)
    draw_any_line(x_origin - 10, y_origin - 50, x_origin - 5, y_origin - 55)
    draw_any_line(x_origin + 10, y_origin - 50, x_origin + 5, y_origin - 55)
    draw_any_line(x_origin + 10, y_origin - 50, x_origin + 15, y_origin - 55)

    # Eye of the chicken (small circle)
    eye_x = x_origin + 35
    eye_y = y_origin + 45
    for angle in range(0, 360, 30):
        x = eye_x + 3 * math.cos(math.radians(angle))
        y = eye_y + 3 * math.sin(math.radians(angle))
        next_x = eye_x + 3 * math.cos(math.radians(angle + 30))
        next_y = eye_y + 3 * math.sin(math.radians(angle + 30))
        draw_any_line(x, y, next_x, next_y) 
    # draw_wings(x_origin, y_origin)
    if draw_first_wing==True:
        draw_wings2(x_origin, y_origin)
    else:
        draw_wings(x_origin, y_origin)
def toggle_chicken():
    global last_switch_time, draw_first_wing
    current_time = time.time()
    print(current_time - last_switch_time)
    if current_time - last_switch_time >= 0.25:
        draw_first_wing = not draw_first_wing
        # Update the last switch time to the current time
        last_switch_time = current_time
        
    # else:
    #     draw_first_wing = True
def update_chicken():
    global chickenX, chickenY, frame_count

    # Update the frame count
    frame_count += 1

    # Update chickenX
    chickenX = (chickenX + 1 + speed)
    if chickenX >= 250:
        chickenX = -230

    # Oscillate chickenY using sine function
    # The multiplier for frame_count controls the frequency of oscillation
    chickenY = math.sin(frame_count * math.pi / 180) * 100

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


    global ballx, bally, ball_size


    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    draw_bucket()
    # draw_chicken()
    draw_chicken2()



    if (create_new):
        m, n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()
    if (end):
        return
    glutSwapBuffers()



def animate():
    # //codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx,chickenX,chickenY, bally, speed,diamondY,pause, points,diamondX,stop,randomR,randomG,randomB
    global end
    # Your animation code here
    toggle_chicken()
    # Check if the program should end
    if end:
        glutLeaveMainLoop()

    if(pause==False and stop == False):
        diamondY =(diamondY - speed)

        update_chicken()






        if(round(diamondX)>=round(boatX) and round(diamondX)<=round(boatX)+60):
            # print('ki hochee')
            if (round(diamondY)-9==boatY):
                points+=1
                speed *=2

                randomR = random.randint(0, 255) / 255
                ramdomG = random.randint(0, 255) / 255
                randomB = random.randint(0, 255) / 255
                print('Score: '+str(points))
                diamondX = random.randint(-240,240)
                diamondY = 230
        if (round(diamondY) - 9 < boatY):
            print('Game Over! Score:'+str(points))
            stop = True
            diamondY = -300
    if(end):
        return



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
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  # //Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)  # what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()
    # return something
    # The main loop of OpenGL


