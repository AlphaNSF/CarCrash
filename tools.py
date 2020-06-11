import pygame
import os
import random
import pickle
from Object import *
from Front_car import *
from Player import *
from Background import *
from Animation import *
from constant import *

def replace_color(img, color_from, color_to):
    pixels = pygame.PixelArray(img)
    pixels.replace(color_from, color_to)
    del pixels
    return img

def new_random_front_car(min_speed, max_speed):
    x = random.uniform(0, WIDTH-CAR_WIDTH)
    speed = random.uniform(min_speed, max_speed)
    r = int(random.uniform(0,255))
    g = int(random.uniform(0,255))
    b = int(random.uniform(0,255))
    return Front_car(x, -CAR_HEIGHT, speed, (r, g, b))

def new_explosion_animation(x, y):
    x_pos = x - (EXPLOSION_WIDTH//2)
    y_pos = y - (EXPLOSION_HEIGHT//2)
    return animation(x_pos, y_pos, EXPLOSION_IMG_TAB, 4)

def draw_object_list(object_list, surface):
    for object in object_list:
        object.draw(surface)

def move_object_list(x, y, object_list):
    for object in object_list:
        object.move(x, y)

def check_object_list_collision(object, object_list):
    for other in object_list:
        if other != object:
            x, y = object.collide(other)
            if x != None and y != None:
                return other, x, y

    return None, -1, -1

def play_random_sound(sound_list):
    random.choice(sound_list).play()

def saveFile(file, var):
    with open(file, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(var)

def loadFile(file):
    with open(file, 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        var = mon_depickler.load()
    return var
