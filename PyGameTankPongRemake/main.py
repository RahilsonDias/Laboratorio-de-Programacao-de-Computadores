import pygame
import math

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tank-Pong")

bg_color = (0, 0, 0)
tank_sprite = pygame.image.load("Sprites/tank.png")
brick_sprite = pygame.image.load("Sprites/obstacle.png")


clock = pygame.time.Clock()

game_over = False


class Player(object):
    def __init__(self):
        self.img = tank_sprite
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = width//2
        self.y = height//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def draw(self, screen):
        # screen.blit(self.img, [self.x, self.y, self.w, self.h])
        screen.blit(self.rotatedSurf, self.rotatedRect)

    def turn_left(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def turn_right(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def move(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)


class Bullet(object):
    def __init__(self):
        self.img = brick_sprite
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, screen):
        # screen.blit(self.img, [self.x, self.y, self.w, self.h])
        pygame.draw.rect(screen, (255,255,255), [self.x, self.y, self.w, self.h])


player = Player()
playerBullets = []
game_loop = True
while game_loop:
    clock.tick(60)
    if not game_over:
        for b in playerBullets:
            b.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not game_over:
                    playerBullets.append(Bullet())

    # update screen
    screen.fill((0, 0, 0))
    player.draw(screen)
    for b in playerBullets:
        b.draw(screen)
    pygame.display.update()
