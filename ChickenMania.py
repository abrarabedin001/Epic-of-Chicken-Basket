import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# from modules.display1 import display1
# from modules.display2 import display2
# from modules.display3 import display3
# from modules.stage1animate import stage1animate
# from modules.stage2animate import stage2animate
# from modules.listeners import keyboardListener, mouseListener_stage2,mouseListener_stage1

# from modules.listeners import specialKeyListener
# from modules.config import config
# from modules.stage3animate import stage3animate

# shapes
import random
import time
import math


class GameConfig:
    def __init__(self):
        self.W_Width, self.W_Height = 500, 500
        self.diamondY = 180
        self.diamondX = 0
        self.boatX = -250
        self.boatY = -230
        self.ballx = self.bally = 0
        self.speed = 0.5
        self.ball_size = 2
        self.points = 0
        self.create_new = False
        self.pause = False
        self.stop = False
        self.randomR = random.randint(0, 255) / 255
        self.randomG = random.randint(0, 255) / 255
        self.randomB = random.randint(0, 255) / 255
        self.end = False
        self.last_switch_time = time.time()
        self.draw_first_wing = True
        self.chickenX = 0
        self.chickenY = 400
        self.amplitude = 20
        self.frame_count = 0
        self.bucketX = -50
        self.bucketY = 50
        self.birdY_offset = 180
        self.centers = []
        self.radiuses = []
        self.boundary_x_min = -250
        self.boundary_x_max = 250
        self.boundary_y_min = -250
        self.boundary_y_max = 250
        self.stage = 1
        self.missiles = []
        self.chickenHealth = 3
        self.threshold = 3

    # Getters
    def get_diamondY(self):
        return  self.diamondY
    def get_diamondX(self):
        return  self.diamondX

    def get_boat_position(self):
        return self.boatX, self.boatY

    def get_ball_position(self):
        return self.ballx, self.bally

    def get_speed(self):
        return self.speed

    def get_ball_size(self):
        return self.ball_size

    def get_points(self):
        return self.points

    def get_creation_status(self):
        return self.create_new

    def get_pause_status(self):
        return self.pause

    def get_stop_status(self):
        return self.stop

    def get_random_colors(self):
        return self.randomR, self.randomG, self.randomB

    def get_end_status(self):
        return self.end

    def get_last_switch_time(self):
        return self.last_switch_time

    def get_draw_first_wing_status(self):
        return self.draw_first_wing

    def get_chicken_position(self):
        return self.chickenX, self.chickenY

    def get_amplitude(self):
        return self.amplitude

    def get_frame_count(self):
        return self.frame_count

    def get_bucket_position(self):
        return self.bucketX, self.bucketY

    # Setters
    def set_diamondX(self, x):
        self.diamondX = x
   
    def set_diamondY(self,  y):
    
        self.diamondY = y

    def set_boat_position(self, x, y):
        self.boatX = x
        self.boatY = y

    def set_ball_position(self, x, y):
        self.ballx = x
        self.bally = y

    def set_speed(self, speed):
        self.speed = speed

    def set_ball_size(self, size):
        self.ball_size = size

    def set_points(self, points):
        self.points = points

    def set_creation_status(self, status):
        self.create_new = status

    def set_pause_status(self, status):
        self.pause = status

    def set_stop_status(self, status):
        self.stop = status

    def set_random_colors(self, r, g, b):
        self.randomR = r
        self.randomG = g
        self.randomB = b

    def set_end_status(self, status):
        self.end = status

    def set_last_switch_time(self, time):
        self.last_switch_time = time

    def set_draw_first_wing_status(self, status):
        self.draw_first_wing = status

    def set_chicken_position(self, x, y):
        self.chickenX = x
        self.chickenY = y

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude

    def set_frame_count(self, count):
        self.frame_count = count

    def set_bucket_position(self, x, y):
        self.bucketX = x
        self.bucketY = y


config =  GameConfig()

def draw_circle(x_center, y_center, radius, boundary_x_min, boundary_x_max, boundary_y_min, boundary_y_max):
    x = radius
    y = 0
    d = 1 - radius  # Initial value of the decision parameter

    # Create empty lists to store the coordinates of the circle
    x_coords = []
    y_coords = []

    # Plot the initial point on the circle
    x_coords.append(x + x_center)
    y_coords.append(y + y_center)

    # Iterate while the x coordinate is greater than or equal to y coordinate
    while x > y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if d <= 0:
            d = d + 2 * y + 1
        else:
            x -= 1
            d = d + 2 * y - 2 * x + 1

        # Calculate the coordinates based on the center
        x_pos = x + x_center
        y_pos = y + y_center

        # Check if any point of the perimeter touches the boundary
        if (
            x_center + radius > boundary_x_max or
            x_center - radius < boundary_x_min or
            y_center + radius > boundary_y_max or
            y_center - radius < boundary_y_min 
        ):  
            print('Score: ' + str(config.get_points()))
            return None, None  # Perimeter touches the boundary, return None
        distanceFromEgg = math.sqrt((config.diamondX+5 - x_center) ** 2 + (config.diamondY - y_center) ** 2)
        if( distanceFromEgg<=radius ):
            config.set_diamondX(0)
            config.diamondX = config.chickenX  
            config.diamondY = config.chickenY +config.birdY_offset
            config.set_points(config.get_points()+1)
            return None, None
        # All the perimeter points have already been printed
        # print("fruff happens")
        # print(x_center,y_center)
        if x < y:
            break

        # Plot the points of the circle in all octants
        x_coords.append(x + x_center)
        y_coords.append(y + y_center)
        x_coords.append(-x + x_center)
        y_coords.append(y + y_center)
        x_coords.append(x + x_center)
        y_coords.append(-y + y_center)
        x_coords.append(-x + x_center)
        y_coords.append(-y + y_center)
        x_coords.append(y + x_center)
        y_coords.append(x + y_center)
        x_coords.append(-y + x_center)
        y_coords.append(x + y_center)
        x_coords.append(y + x_center)
        y_coords.append(-x + y_center)
        x_coords.append(-y + x_center)
        y_coords.append(-x + y_center)

    # Plot the circle using the coordinates
    return x_coords, y_coords


def draw_circle2(x_center, y_center, radius):
    x = radius
    y = 0
    d = 1 - radius  # Initial value of the decision parameter

    # Create empty lists to store the coordinates of the circle
    x_coords = []
    y_coords = []

    # Plot the initial point on the circle
    x_coords.append(x + x_center)
    y_coords.append(y + y_center)

    # Iterate while the x coordinate is greater than or equal to y coordinate
    while x > y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if d <= 0:
            d = d + 2 * y + 1
        else:
            x -= 1
            d = d + 2 * y - 2 * x + 1

        # Calculate the coordinates based on the center
        x_pos = x + x_center
        y_pos = y + y_center

   
        if x < y:
            break

        # Plot the points of the circle in all octants
        x_coords.append(x + x_center)
        y_coords.append(y + y_center)
        x_coords.append(-x + x_center)
        y_coords.append(y + y_center)
        x_coords.append(x + x_center)
        y_coords.append(-y + y_center)
        x_coords.append(-x + x_center)
        y_coords.append(-y + y_center)
        x_coords.append(y + x_center)
        y_coords.append(x + y_center)
        x_coords.append(-y + x_center)
        y_coords.append(x + y_center)
        x_coords.append(y + x_center)
        y_coords.append(-x + y_center)
        x_coords.append(-y + x_center)
        y_coords.append(-x + y_center)

    # Plot the circle using the coordinates
    return x_coords, y_coords



def draw_bucket():
    x_origin, y_origin = config.get_bucket_position()

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
    x_origin, y_origin = config.get_boat_position()
    stop = config.get_stop_status()
    if(stop==False):
        glColor3f(255/255, 255 / 255, 255 / 255)
    else:
        glColor3f(255/255, 0 / 255, 0 / 255)
    draw_basket(x_origin, y_origin, 100, 50)

   
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
    x_origin, y_origin = config.get_chicken_position()

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
    x_origin, y_origin = config.get_chicken_position()

    y_origin = y_origin + config.birdY_offset

    # Set color for the chicken
    glColor3f(1, 1, 0)  # Yellow color
    
    x,y =draw_circle2(x_origin, y_origin, 35)
    for r in range(len(x)):
        draw_points(x[r],y[r],1)

    # Body of the chicken (ellipse-like shape)
    # for angle in range(0, 360, 10):
    #     x = x_origin + 20 * math.cos(math.radians(angle))
    #     y = y_origin + 30 * math.sin(math.radians(angle))
    #     next_x = x_origin + 20 * math.cos(math.radians(angle + 10))
    #     next_y = y_origin + 30 * math.sin(math.radians(angle + 10))
    #     draw_any_line(x, y, next_x, next_y)

    # Head of the chicken (smaller ellipse)

    head_x,head_y = draw_circle2(x_origin + 30, y_origin + 40, 10)
    for r in range(len(head_x)):
        draw_points(head_x[r],head_y[r],1)
    # for angle in range(0, 360, 30):
    #     x = x_origin + 30 + 10 * math.cos(math.radians(angle))
    #     y = y_origin + 40 + 15 * math.sin(math.radians(angle))
    #     next_x = x_origin + 30 + 10 * math.cos(math.radians(angle + 30))
    #     next_y = y_origin + 40 + 15 * math.sin(math.radians(angle + 30))
    #     draw_any_line(x, y, next_x, next_y)

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
    if config.draw_first_wing==True:
        draw_wings2(x_origin, y_origin)
    else:
        draw_wings(x_origin, y_origin)
def toggle_chicken():
    current_time = time.time()
    if current_time - config.get_last_switch_time() >= 0.25:
        config.set_draw_first_wing_status(not config.get_draw_first_wing_status())
        config.set_last_switch_time(current_time)
        
    # else:
    #     draw_first_wing = True
def update_chicken():
    x_origin, y_origin = config.get_chicken_position()
   
    frame_count = config.get_frame_count()
    speed = config.get_speed()
    amplitude = config.get_amplitude()

    # Update the frame count
    frame_count += 1
    config.set_frame_count(frame_count)

    # Update chickenX and check bounds
    chickenX = x_origin + speed
    if chickenX >= 250:
        chickenX = -230
    config.set_chicken_position(chickenX, y_origin+220)

    # Oscillate chickenY using sine function
    chickenY = math.sin(frame_count * math.pi / 180) * amplitude
    config.set_chicken_position(chickenX, chickenY)

def draw_diamond():
    # x_origin = config.get_diamondX()
    # y_origin = config.get_diamondY()
    # randomR, randomG, randomB = config.get_random_colors()
    # # 0,128,

    # glColor3f(randomR, randomG, randomB)


    # draw_any_line(x_origin, y_origin, x_origin+9, y_origin+9)
    # draw_any_line(x_origin , y_origin, x_origin +9, y_origin -9)
    # draw_any_line(x_origin +10, y_origin+9,x_origin+18, y_origin+1  )
    # draw_any_line(x_origin +10, y_origin-9 ,x_origin+18, y_origin-1)
    x_origin = config.get_diamondX()
    y_origin = config.get_diamondY()
    randomR, randomG, randomB = config.get_random_colors()

    glColor3f(randomR, randomG, randomB)

    # Drawing the top half of the egg
    x_list,y_list = draw_circle2(x_origin, y_origin, 9)
    # print(x_list)
    for r in range(1,len(x_list)):
        draw_points(x_list[r],y_list[r],1)
        
        draw_any_line(x_list[r-1],y_list[r-1],x_list[r],y_list[r])
    # for i in range(10):
    #     angle = i * (180 / 10)  # Dividing half-circle into 10 segments
    #     x = x_origin + 9 * math.cos(math.radians(angle))
    #     y = y_origin + 18 * math.sin(math.radians(angle))
    #     draw_any_line(x_origin, y_origin, x, y)

    # Drawing the bottom half of the egg
    # for i in range(10):
    #     angle = i * (180 / 10)  # Dividing half-circle into 10 segments
    #     x = x_origin + 9 * math.cos(math.radians(angle))
    #     y = y_origin - 18 * math.sin(math.radians(angle))
    #     draw_any_line(x_origin, y_origin, x, y)

def draw_half_circle(x_center, y_center, radius):
    x = radius
    y = 0
    d = 1 - radius  # Initial decision parameter

    # Create empty lists to store the coordinates of the half-circle
    x_coords = []
    y_coords = []

    # Plot the initial point on the circle, which will also be a point on the half-circle
    x_coords.append(x + x_center)
    y_coords.append(y + y_center)

    # Iterate while the x coordinate is greater than the y coordinate
    while x >= y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if d < 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

        # Only store the points that are on the upper half of the circle
        if y <= x:  # This ensures that we are only considering the upper semi-circle
            # Add points in the first and second quadrant
          x_coords.append(x + x_center)
          y_coords.append(y + y_center)
          x_coords.append(-x + x_center)#important
          y_coords.append(y + y_center)#important
         
          x_coords.append(y + x_center)
          y_coords.append(x + y_center) #important
          x_coords.append(-y + x_center) #important
          y_coords.append(x + y_center)
      
    # Draw the half-circle using the coordinates
    for i in range(len(x_coords)):
        draw_points(x_coords[i], y_coords[i], 1)  # Assuming a point size of 1 for simplicity


def draw_basket(base_x, base_y, width, height):
    # Define some parameters for the basket
    rim_height = height / 10
    body_height = height - 2 * rim_height

    basket_width = width  # Assume basket_width is defined as the width of the basket
    basket_height = height  # Assume basket_height is defined as the height of the basket
    handle_radius = basket_width // 2  # Set the radius of the handle

    # Coordinates for the center of the half-circle handle
    handle_center_x = basket_width // 2
    handle_center_y = basket_height + handle_radius

    draw_half_circle(handle_center_x+base_x, base_y+handle_center_y-50, handle_radius)
    draw_half_circle(handle_center_x+base_x, base_y+handle_center_y-50, handle_radius-10)

    # Draw the top rim
    top_rim_y = base_y + height - rim_height
    draw_any_line(base_x, top_rim_y, base_x + width, top_rim_y)

    # Draw the bottom rim
    bottom_rim_y = base_y + rim_height
    draw_any_line(base_x, bottom_rim_y, base_x + width, bottom_rim_y)

    # Draw the left side of the basket
    draw_any_line(base_x, bottom_rim_y, base_x, top_rim_y)

    # Draw the right side of the basket
    draw_any_line(base_x + width, bottom_rim_y, base_x + width, top_rim_y)

    # Draw horizontal weave lines across the body of the basket
    num_weave_lines = 5
    weave_spacing = body_height / num_weave_lines
    for i in range(num_weave_lines):
        y = bottom_rim_y + i * weave_spacing
        draw_any_line(base_x, y, base_x + width, y)

    # Draw vertical weave lines down the body of the basket
    # This is a simplification; actual vertical lines would be arcs
    num_vertical_weaves = 7
    vertical_weave_spacing = width / num_vertical_weaves
    for i in range(num_vertical_weaves):
        x = base_x + i * vertical_weave_spacing
        draw_any_line(x, bottom_rim_y, x, top_rim_y)

def draw_roman_iii():
    # Set the color for the Roman numeral
    glColor3f(1.0, 1.0, 1.0)

    draw_any_line(-7, 20, -7, -20)
    draw_any_line(0, 20, 0, -20)
    draw_any_line(7, 20, 7, -20)

def draw_roman_ii():
    # Set the color for the Roman numeral
    glColor3f(1.0, 1.0, 1.0)

    draw_any_line(-5, 20, -5, -20)
    draw_any_line(5, 20, 5, -20)
    #Line(190, 350, 210, 350)

def draw_roman_i():
    # Set the color for the Roman numeral
    glColor3f(1.0, 1.0, 1.0)

    draw_any_line(0, 20, 0, -20)
    #Line(190, 340, 210, 340)
    #Line(190, 350, 210, 350)


# display 1

def display1():
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
    draw_roman_i()

    
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


# display 2


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

# display3



def display3():
  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    
    draw_x()
    draw_pause()
    draw_play()
    draw_diamond()
    draw_boat()
    # draw_bucket()    
    draw_chicken2()
    draw_roman_iii()
    for missile in config.missiles:
        missile.draw()
    
    if(config.chickenHealth<=0):
      
      print("Winner winner chicken dinner")

      config.pause = True
      config.end = True

    
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
# Listeners

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

def shoot_missile():
    
    missile = Missile(config.boatX+50, config.boatY+50)
    config.missiles.append(missile)


def convert_coordinate(x, y):
    a = x - (config.W_Width / 2)
    b = (config.W_Height / 2) - y
    return a, b

def keyboardListener(key, x, y):
    if key == b'w':
        config.ball_size += 1
    if key == b's':
        config.ball_size -= 1
    if key == b' ':
        shoot_missile()
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    if key == GLUT_KEY_UP:
        config.speed *= 2
    if key == GLUT_KEY_DOWN:
        config.speed /= 2
    if not config.pause and not config.stop:
        if key == GLUT_KEY_RIGHT and config.boatX + 100 <= 249:
            config.boatX += 5*config.speed
        if key == GLUT_KEY_LEFT and config.boatX >= -249:
            config.boatX -= 5*config.speed
    glutPostRedisplay()

def mouseListener_stage1(button, state, x, y):
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
        shoot_missile()
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
# Play and Pause


def draw_x():
    x_origin = 220
    y_origin = 240
    glColor3f(255 / 256, 0 / 256, 0 / 256)
    draw_any_line(x_origin, y_origin, x_origin+20, y_origin-20)
    draw_any_line(x_origin, y_origin-20, x_origin+20, y_origin)

def draw_pause():
    x_origin = -5
    y_origin = 240
    glColor3f(255 / 256, 191 / 256, 0 / 256)

    if not config.get_pause_status():
        draw_any_line(x_origin, y_origin, x_origin, y_origin-20)
        draw_any_line(x_origin+10, y_origin, x_origin+10, y_origin-20)
    else:
        draw_any_line(x_origin, y_origin, x_origin, y_origin-20)
        draw_any_line(x_origin, y_origin, x_origin+20, y_origin-10)
        draw_any_line(x_origin+20, y_origin-10, x_origin, y_origin-20)

def draw_play():
    x_origin = -230
    y_origin = 230
    glColor3f(0, 128 / 256, 128 / 256)

    draw_any_line(x_origin, y_origin, x_origin+9, y_origin+9)
    draw_any_line(x_origin, y_origin, x_origin+9, y_origin-9)
    draw_any_line(x_origin, y_origin, x_origin+20, y_origin)

# animate1

def stage1animate():
    # Codes for any changes in Models, Camera
    glutPostRedisplay()

    # Use the config object to access and modify properties
    if not config.get_end_status() and not config.get_pause_status() and not config.get_stop_status():
        config.set_diamondY(config.get_diamondY() - config.get_speed())
        toggle_chicken()
        update_chicken()
        if round(config.get_diamondX()) >= round(config.get_boat_position()[0]) and round(config.get_diamondX()) <= round(config.get_boat_position()[0]) + 100:
            if round(config.get_diamondY()) - 9 <= config.get_boat_position()[1] + 50 and round(config.get_diamondY()) - 9 >= config.get_boat_position()[1]:
                config.set_points(config.get_points() + 1)
                if(config.points>=config.threshold):
                    config.stage=2
                    config.set_points(0)
                config.set_speed(config.get_speed() * 1.1)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                
                x_origin, y_origin = config.get_chicken_position()

                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
            
                
                # config.set_diamond_position(random.randint(-240, 240), 230)
        if round(config.get_diamondY()) - 9 < config.get_boat_position()[1]:
            print('Game Over! Score:' + str(config.get_points()))
            config.set_stop_status(True)
            config.set_diamondY(-300)

    if config.get_end_status():
        return
# animate2
def stage2animate():
    # Codes for any changes in Models, Camera
    glutPostRedisplay()

    # Use the config object to access and modify properties
    if not config.get_end_status() and not config.get_pause_status() and not config.get_stop_status():
        del_x = config.boatX-config.diamondX
        del_y = config.boatY-config.diamondY
        config.set_diamondX(config.get_diamondX() + del_x/100)
        config.set_diamondY(config.get_diamondY() + del_y/100 - config.get_speed())
        toggle_chicken()
        update_chicken()
        if(config.points>=config.threshold):
            config.stage=3
        for r in range(len(config.radiuses)):
            config.radiuses[r] = (config.radiuses[r]+config.speed)
        if round(config.get_diamondX()) >= round(config.get_boat_position()[0]) and round(config.get_diamondX()) <= round(config.get_boat_position()[0]) + 100:
            if round(config.get_diamondY()) - 9 <= config.get_boat_position()[1] + 50 and round(config.get_diamondY()) - 9 >= config.get_boat_position()[1]:
                config.set_points(config.get_points() - 1)
                config.set_speed(config.get_speed() * 1.1)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                x_origin, y_origin = config.get_chicken_position()
                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
            elif round(config.get_diamondY()) - 9 < config.get_boat_position()[1]:
                x_origin, y_origin = config.get_chicken_position()

                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
        elif config.get_diamondY() < -250:
            config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
            print('Score: ' + str(config.get_points()))
            
            x_origin, y_origin = config.get_chicken_position()

            y_origin = y_origin + config.birdY_offset
            config.set_diamondY(y_origin)
            config.set_diamondX(x_origin)
        else:
            config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
            
                # config.set_diamond_position(random.randint(-240, 240), 230)
        if config.get_points() < 0:
            print('Game Over! Score:' + str(config.get_points()))
            config.set_stop_status(True)
            config.set_diamondY(-300)

    if config.get_end_status():
        return
    
# animate3

def stage3animate():
    # Codes for any changes in Models, Camera
    glutPostRedisplay()

    if(config.pause):
      game_over_str = "Game Over!"
      for char in game_over_str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    # Use the config object to access and modify properties
    if not config.get_end_status() and not config.get_pause_status() and not config.get_stop_status():
        del_x = config.boatX-config.diamondX
        del_y = config.boatY-config.diamondY
        config.set_diamondX(config.get_diamondX() + del_x/100)
        config.set_diamondY(config.get_diamondY() + del_y/100 - config.get_speed())
        toggle_chicken()
        update_chicken()
        for missile in config.missiles:
            missile.move()
            if (missile.y > 250):
                config.missiles.remove(missile)
            if(missile.x>=config.diamondX-10 and missile.x<=config.diamondX+10 and missile.y>=config.diamondY-10 and missile.y<=config.diamondY+10):
                config.set_points(config.get_points() + 1)
                config.set_speed(config.get_speed() * 1.1)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                config.missiles.remove(missile)
                x_origin, y_origin = config.get_chicken_position()
                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
            if(missile.x>=config.chickenX-10 and missile.x<=config.chickenX+10 and missile.y>=config.chickenY-10 and missile.y<=config.chickenY+10):
                config.set_points(config.get_points() + 1)
                config.chickenHealth -= 1
                print('Chicken Health: ' + str(config.chickenHealth))
                config.set_speed(config.get_speed() * 1.1)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                config.missiles.remove(missile)
                x_origin, y_origin = config.get_chicken_position()
                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)

        for r in range(len(config.radiuses)):
            config.radiuses[r] = (config.radiuses[r]+config.speed)
        if round(config.get_diamondX()) >= round(config.get_boat_position()[0]) and round(config.get_diamondX()) <= round(config.get_boat_position()[0]) + 100:
            if round(config.get_diamondY()) - 9 <= config.get_boat_position()[1] + 50 and round(config.get_diamondY()) - 9 >= config.get_boat_position()[1]:
                config.set_points(config.get_points() - 1)
                config.set_speed(config.get_speed() * 1.1)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                x_origin, y_origin = config.get_chicken_position()
                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
            elif round(config.get_diamondY()) - 9 < config.get_boat_position()[1]:
                x_origin, y_origin = config.get_chicken_position()

                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
        elif config.get_diamondY() < -250:
            config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
            print('Score: ' + str(config.get_points()))
            
            x_origin, y_origin = config.get_chicken_position()

            y_origin = y_origin + config.birdY_offset
            config.set_diamondY(y_origin)
            config.set_diamondX(x_origin)
        else:
            config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
            
                # config.set_diamond_position(random.randint(-240, 240), 230)
        if config.get_points() < 0:
            print('Game Over! Score:' + str(config.get_points()))
            config.set_stop_status(True)
            config.set_diamondY(-300)

    if config.get_end_status():
        return


# straightLine




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
wind = glutCreateWindow(b"Chicken Mania")
init()

def display():
  if (config.stage == 1):
      display1()
  elif (config.stage == 2):
      display2()
  else:
      display3()


def mouseListener(button, state, x, y):
    if (config.stage == 1):
        mouseListener_stage1(button, state, x, y)
    elif (config.stage == 2):
        mouseListener_stage2(button, state, x, y)
    else:
        mouseListener_stage2(button, state, x, y)    
def animate():
    if (config.stage == 1):
        stage1animate()
    elif (config.stage == 2):
        stage2animate()
    else:
        stage3animate()



 # display callback function

# if (config.stage == 1):
glutDisplayFunc(display) 
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)


glutMainLoop()
   


