import pygame
import math
import bullet


class Tank(object):
    def __init__(self, x, y):
        self.img = pygame.image.load("Sprites/tank.png")
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = x
        self.y = y
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2,
                     self.y - self.sine * self.h//2)
        self.tankBullets = []
        self.top_collision = False
        self.bottom_collision = False
        self.right_collision = False
        self.left_collision = False

    def draw(self, screen):
        screen.blit(self.rotatedSurf, self.rotatedRect)

    def turn_left(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)

    def turn_right(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)

    def move(self):
        if self.top_collision is True:
            self.x = self.x
            self.y = self.y + 1
        if self.bottom_collision is True:
            self.x = self.x
            self.y = self.y - 1
        if self.right_collision is True:
            self.x = self.x - 1
            self.y = self.y
        if self.left_collision is True:
            self.x = self.x + 1
            self.y = self.y
        else:
            self.x += self.cosine * 6
            self.y -= self.sine * 6
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)

    def shoot(self):
        self.tankBullets.append(bullet.Bullet(self.head, self.cosine,
                                              self.sine))

    def get_player_bullets(self):
        return self.tankBullets

    def get_rect(self):
        return self.rotatedRect

    def set_top_collision(self, bool):
        self.top_collision = bool

    def set_bottom_collision(self, bool):
        self.bottom_collision = bool

    def set_right_collision(self, bool):
        self.right_collision = bool

    def set_left_collision(self, bool):
        self.left_collision = bool
