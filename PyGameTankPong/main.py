import pygame
import setup
pygame.init()

SCORE_MAX = 2

size = (800, 600)
screen = pygame.display.set_mode((setup.WIDTH, setup.HEIGHT))
pygame.display.set_caption("Tank-Pong")

# initiate P1
player_1_spr = pygame.image.load("Sprites/tank.png")
player_1_x = setup.start_x_p1
player_1_y = setup.start_y_p1
# player_1 = pygame.draw.rect(screen, (0, 204, 0), (player_1_x, player_1_y, 40, 35))

# initiate P2
player_2_spr = pygame.image.load("Sprites/tank.png")
player_2_x = setup.start_x_p2
player_2_y = setup.start_y_p2
# player_2 = pygame.draw.rect(screen, (0, 204, 0), (player_2_x, player_2_y, 40, 35))

# print(player_1)


def move_paddle(player):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player.x > 0:
        player.x -= 5
    if key[pygame.K_DOWN] and player.x < setup.WIDTH:
        player.x += 5


def rotate_tank(image):


    return image


# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # clear screen
    screen.fill(setup.BLACK)

    # player 1 up movement
    # move_paddle(player_1_spr)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        image = pygame.transform.rotate(player_1_spr, 1)
    if key[pygame.K_RIGHT]:
        image = pygame.transform.rotate(player_1_spr, -1)



    # drawing objects
    screen.blit(player_1_spr, (player_1_x, player_1_y))
    screen.blit(player_2_spr, (player_2_x, player_2_y))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)
