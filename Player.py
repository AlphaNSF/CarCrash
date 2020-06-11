import pygame
from Object import *

PLAYER_WIDTH = 38*2
PLAYER_HEIGHT = 71*2
PLAYER_IMG_PATH = os.path.join("sprites", "red_car.png")


class Player(Object):
    left = False
    right = False
    up = False
    down = False
    def __init__(self, x, y, x_speed, y_speed, surface):
        img = pygame.image.load(PLAYER_IMG_PATH)
        img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.surface = surface
        super().__init__(x, y, img)

    def set_speed(self, x, y):
        self.x_speed = x
        self.y_speed = y

    def disable_control(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def update_control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            elif event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_UP:
                self.up = True
            elif event.key == pygame.K_DOWN:
                self.down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            elif event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_UP:
                self.up = False
            elif event.key == pygame.K_DOWN:
                self.down = False

    def move(self, x, y):
        width = self.surface.get_width()
        height = self.surface.get_height()
        if x < 0 and (self.x > 0 or self.destroyed):
            self.x += x
        elif x > 0 and (self.x < width - PLAYER_WIDTH or self.destroyed):
            self.x += x

        if y<0 and (self.y > 0 or self.destroyed):
            self.y += y

        elif y>0 and (self.destroyed or self.y < height - PLAYER_HEIGHT):
            self.y += y

    def drive(self):
        width = self.surface.get_width()
        height = self.surface.get_height()

        if not self.destroyed:
            if self.left:
                self.move(-self.x_speed, 0)

            if self.right:
                self.move(self.x_speed, 0)

            if self.up:
                self.move(0, -self.y_speed)

            if self.down:
                self.move(0, self.y_speed)

            if self.x < 0:
                self.x = 0
            elif self.x > width - PLAYER_WIDTH:
                self.x = width-PLAYER_WIDTH

            if self.y < 0:
                self.y = 0
            elif self.y > height - PLAYER_HEIGHT:
                self.y = height - PLAYER_HEIGHT
