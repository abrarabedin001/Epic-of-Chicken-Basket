import math
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.straightline import draw_points,draw_any_line
from modules.config import config


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
# শাবাব আব্দুল্লাহ্
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