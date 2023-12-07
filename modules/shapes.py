import math
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.straightline import draw_points

from project import draw_any_line


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
    global boatX,boatY,stop
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
    global chickenX, chickenY, frame_count,speed,amplitude

    # Update the frame count
    frame_count += 1

    # Update chickenX
    chickenX = (chickenX + 1 + speed)
    if chickenX >= 250:
        chickenX = -230

    # Oscillate chickenY using sine function
    # The multiplier for frame_count controls the frequency of oscillation
    chickenY = math.sin(frame_count * math.pi / 180) * amplitude
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
