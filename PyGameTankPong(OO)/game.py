import pygame
from tank import Tank
import arena
import collision
# from bulletclass import Bullet


width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tank-Pong")

bg_color = (0, 0, 0)

clock = pygame.time.Clock()

game_over = False

player_1 = Tank(70, 340)
bullets_1 = player_1.get_player_bullets()
player_2 = Tank(730, 340)
bullets_2 = player_2.get_player_bullets()

wall_list = arena.create_arena()
tank_list = [player_1, player_2]

game_loop = True
while game_loop:
    clock.tick(60)
    if not game_over:
        for b in bullets_1:
            b.move()
        for b in bullets_2:
            b.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_1.turn_left()
        if keys[pygame.K_d]:
            player_1.turn_right()
        if keys[pygame.K_w]:
            player_1.move()

        if keys[pygame.K_LEFT]:
            player_2.turn_left()
        if keys[pygame.K_RIGHT]:
            player_2.turn_right()
        if keys[pygame.K_UP]:
            player_2.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if not game_over:
                    player_1.shoot()
            if event.key == pygame.K_DOWN:
                if not game_over:
                    player_2.shoot()

    collision.tank_collision(player_1, player_2)
    collision.tank_collision(player_2, player_1)
    for wall in wall_list:
        collision.wall_collision(player_1, wall)
        collision.wall_collision(player_2, wall)

    # update screen
    screen.fill((0, 0, 0))
    player_1.draw(screen)
    player_2.draw(screen)
    for b in bullets_1:
        b.draw(screen)
    for b in bullets_2:
        b.draw(screen)
    for wall in wall_list:
        pygame.draw.rect(screen, (255, 255, 255), wall)
    pygame.display.update()
