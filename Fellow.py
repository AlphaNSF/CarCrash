import pygame
import os
from constant import *
from Object import *

FELLOW_HEIGHT = 50
FELLOW_WIDTH = 50
FELLOW_IMG = pygame.image.load(os.path.join("sprites","fellow.png"))

class Fellow(Object):

    def __init__(self, y, side):
        if side == "left":
            x = 0
        else:
            x = WIDTH
        super().__init__(x, y, pygame.transform.scale(FELLOW_IMG, (FELLOW_WIDTH, FELLOW_HEIGHT)))
        self.side = side

    def drive(self):
        if self.side == "left":
            self.move(1,0)
        else:
            self.move(-1,0)
