import pygame
import os

BACKGROUND_IMG = pygame.image.load(os.path.join("sprites", "road.png"))
BACKGROUND_IMG = pygame.transform.rotate(BACKGROUND_IMG, 90)
BACKGROUND_LIST = [BACKGROUND_IMG, BACKGROUND_IMG]

class Background():
    x=0
    y=0
    def __init__(self, surface, img_list):
        self.img_list = img_list
        self.img_len = len(img_list)
        self.ind = 0
        self.surface = surface
        for i in range(len(self.img_list)):
            self.img_list[i] = pygame.transform.scale(self.img_list[i], (surface.get_width(), surface.get_height()))
        self.y = surface.get_height() - img_list[0].get_height()

    def vertical_scroll(self, speed):
        width = self.surface.get_width()
        height = self.surface.get_height()


        self.y = (self.y + speed) % height
        self.surface.blit(self.img_list[0], (0,self.y))
        self.surface.blit(self.img_list[1], (0,self.y - height))
