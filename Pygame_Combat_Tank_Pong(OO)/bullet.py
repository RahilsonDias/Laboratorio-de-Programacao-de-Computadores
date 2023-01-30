import pygame


class Bullet(object):
    def __init__(self, point, cosine, sine):
        self.image = pygame.image.load("Sprites/obstacle.png")
        self.x, self. y = point
        self.rect = pygame.Rect(self.x, self.y, 4, 4)
        self.cos = cosine
        self.sin = sine
        self.speed_vertical = self.cos * 10
        self.speed_horizontal = self.sin * 10
        self.count = 0

    def move(self):
        self.rect.x += self.speed_vertical
        self.rect.y -= self.speed_horizontal

    def draw(self, screen):
        # screen.blit(self.img, [self.x, self.y, self.w, self.h])
        pygame.draw.rect(screen, (252, 180, 108), self.rect)

    def get_rect(self):
        return self.rect

    def set_dx(self):
        self.speed_horizontal *= -1

    def set_dy(self):
        self.speed_vertical *= -1

    def set_count(self):
        self.count += 1

    def get_count(self):
        return self.count
