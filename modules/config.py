import random
import time


class GameConfig:
    def __init__(self):
        self.W_Width, self.W_Height = 500, 500
        self.diamondY = 180
        self.diamondX = 0
        self.boatX = -250
        self.boatY = -230
        self.ballx = self.bally = 0
        self.speed = 1
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