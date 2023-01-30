import pygame
import math
import bullet


class Tank(object):
    def __init__(self, x, y):
        self.number_of_player = 1
        self.img = pygame.image.load(f"Sprites/tank.png")
        self.rect = pygame.Rect(x, y, self.img.get_width(), self.img.get_height())
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect(center=(self.rect.x, self.rect.y))
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.rect.x + self.cosine * self.rect.w // 2,
                     self.rect.y - self.sine * self.rect.h // 2)
        self.tankBullets = []
        self.top_collision = False
        self.bottom_collision = False
        self.right_collision = False
        self.left_collision = False

    def draw(self, screen):
        screen.blit(self.rotatedSurf, self.rotatedRect)

    def turn_left(self):
        self.angle += 5
        self.turn()

    def turn_right(self):
        self.angle -= 5
        self.turn()

    def move_bottom(self):
        if self.top_collision is True:
            self.rect.y = self.rect.y + 4
            self.top_collision = False

    def move_top(self):
        if self.bottom_collision is True:
            self.rect.y = self.rect.y - 4
            self.bottom_collision = False

    def move_left(self):
        if self.right_collision is True:
            self.rect.x = self.rect.x - 4
            self.right_collision = False

    def move_right(self):
        if self.left_collision is True:
            self.rect.x += 4
            self.left_collision = False

    def move(self):

        if self.top_collision is True or self.bottom_collision is True or self.right_collision is True \
                or self.left_collision is True:
            pass
        else:
            self.rect.x += self.cosine * 6
            self.rect.y -= self.sine * 6
            self.turn()

    def turn(self):
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.rect.x, self.rect.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.rect.x + self.cosine * self.rect.w // 2,
                     self.rect.y - self.sine * self.rect.h // 2)

    def shoot(self):
        self.tankBullets.append(bullet.Bullet(self.head, self.cosine,
                                              self.sine))

    def get_player_bullets(self):
        return self.tankBullets

    def get_rect(self):
        return self.rotatedRect

    def set_top_collision(self, boolean):
        # print('set_top_collision', bool)
        self.top_collision = boolean

    def set_bottom_collision(self, boolean):
        self.bottom_collision = boolean

    def set_right_collision(self, boolean):
        self.right_collision = boolean

    def set_left_collision(self, boolean):
        self.left_collision = boolean
