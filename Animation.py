import pygame
import os

EXPLOSION_WIDTH = 100
EXPLOSION_HEIGHT = 100

EXPLOSION_IMG_TAB = []
for path in os.listdir("./sprites/explosion/"):
    img = pygame.image.load(os.path.join("./sprites/explosion/",path))
    img = pygame.transform.scale(img, (EXPLOSION_WIDTH, EXPLOSION_HEIGHT))
    EXPLOSION_IMG_TAB.append(img)

class animation:
    tick = 0
    img_index = 0
    end = False
    pause = False
    def __init__(self, x, y, img_tab, framerate, loop=False):
        self.img_tab = img_tab
        self.framerate = framerate
        self.loop = loop
        self.x = x
        self.y = y
        self.width = img_tab[0].get_width()
        self.height = img_tab[0].get_height()

    def reset(self):
        self.end = False
        self.img_index = 0
        self.tick = 0

    def get_size(self):
        return self.width, self.height

    def is_end(self):
        return self.end

    def stop(self):
        self.pause = True

    def start(self):
        self.pause = False

    def draw(self, surface):
        if not self.end and not self.pause:
            surface.blit(self.img_tab[self.img_index],(self.x, self.y))
            self.tick += 1
            if self.tick != 0 and self.tick%self.framerate == 0:
                self.img_index += 1
                if self.img_index == len(self.img_tab) and self.loop:
                    self.reset()
                elif self.img_index == len(self.img_tab):
                    self.end = True

    def move(self, x, y):
        self.x += x
        self.y += y
