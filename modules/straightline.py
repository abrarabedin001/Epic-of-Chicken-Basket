from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
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

