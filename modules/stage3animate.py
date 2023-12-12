
   
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.shapes import update_chicken, toggle_chicken
from modules.config import config

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