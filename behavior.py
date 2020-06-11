import pygame
import random
import os
from Object import *
from Player import *
from Front_car import *
from tools import *
from constant import *

pygame.mixer.init()
EXPLOSION_SOUNDS = []
for path in os.listdir("./sounds/explosions/"):
    s = pygame.mixer.Sound(os.path.join("sounds/explosions",path))
    s.set_volume(0.1)
    EXPLOSION_SOUNDS.append(s)

def front_car_behavior(front_car_list, explosions_list, window):
    for front_car in front_car_list:
        if front_car.is_on_screen(window):
            front_car.drive()
            other, x, y = check_object_list_collision(front_car, front_car_list)
            if other and not front_car.destroyed:
                other.destroy()
                front_car.destroy()
                random.choice(EXPLOSION_SOUNDS).play()
                explosions_list.append(new_explosion_animation(x, y))
        else:
            front_car_list.remove(front_car)
    return front_car_list, explosions_list

def player_behavior(player, front_car_list, explosions_list):
    player.drive()
    other, x, y = check_object_list_collision(player, front_car_list)
    if other and not player.destroyed:
        explosions_list.append(new_explosion_animation(x, y))
        other.destroy()
        player.destroy()

def fellow_behavior(fellow_list, front_car_list, player, window):
    for fellow in fellow_list:
        if fellow.is_on_screen(window):
            fellow.drive()
            other, x, y = check_object_list_collision(fellow, front_car_list)
            if other:
                if fellow.side == "left":
                    other.move(1,0)
                else:
                    other.move(-1,0)
        else:
            fellow_list.remove(fellow)
