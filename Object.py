import pygame
import os

class Object:
    img = None
    collision_box = None
    destroyed = False
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.collision_box = pygame.mask.from_surface(self.img)

    def move(self, x, y):
        self.x += x
        self.y += y

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def is_on_screen(self, surface):
        img_width = self.img.get_width()
        img_height = self.img.get_height()

        if(self.x + img_width < 0 or self.x > surface.get_width()):
            return False
        elif(self.y + img_height < 0 or self.y > surface.get_height()):
            return False
        else:
            return True

    def destroy(self):
        self.destroyed = True

    def collide(self, other):
        if other.collision_box.overlap(self.collision_box, (int(self.x - other.x), int(self.y - other.y))):
            x, y = other.collision_box.overlap(self.collision_box, (int(self.x - other.x), int(self.y - other.y)))
            x, y = int(x+other.x), int(y+other.y)
            return x, y
        return None, None
