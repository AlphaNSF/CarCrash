import pygame
import os
from Object import *

def replace_color(img, color_from, color_to):
    pixels = pygame.PixelArray(img)
    pixels.replace(color_from, color_to)
    del pixels
    return img

CAR_WIDTH = 38*2
CAR_HEIGHT = 71*2
CAR_IMG_PATH = os.path.join("sprites", "red_car.png")
BASE_COLOR = pygame.image.load(CAR_IMG_PATH).get_at((100, 100))

class Front_car(Object):

    def __init__(self, x, y, speed, color):
        img = pygame.transform.scale(pygame.image.load(CAR_IMG_PATH), (38*2, 71*2))
        img = pygame.transform.rotate(img, 180)
        img = replace_color(img, BASE_COLOR, color)
        self.speed = speed
        super().__init__(x, y, img)

    def drive(self):
        self.move(0, self.speed*(1-self.destroyed))
