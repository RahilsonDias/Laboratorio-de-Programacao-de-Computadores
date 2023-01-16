import pygame
import math
import settings

pygame.init()

screen = pygame.display.set_mode((settings.screen_width,
                                  settings.screen_height))
pygame.display.set_caption("Tank-Pong")


# draw function
def draw_objects(obj, x, y, w, h, data, ang):
    obj.image = pygame.image.load(data)
    obj.image.set_colorkey((0, 0, 0))
    obj.image = pygame.transform.scale(obj.image, [w, h])
    obj.image = pygame.transform.rotate(obj.image, ang)
    obj.rect = pygame.Rect(x - int(obj.image.get_width()/2),
                           y - int(obj.image.get_height()/2),
                           obj.image.get_width(), obj.image.get_height())


def move_tank(obj, speed, angle_in_radians):
    new_x = obj.x + (speed * math.cos(math.radians(angle_in_radians)))
    new_y = obj.y - (speed * math.sin(math.radians(angle_in_radians)))

    for wall in wall_list:
        wall_collision = obj.rect.colliderect(wall.rect)
        if wall_collision:
            if abs(obj.rect.top - wall.rect.bottom) < 10 and obj.y > 0:
                return obj.x, obj.y+1
            if abs(obj.rect.bottom - wall.rect.top) < 10 and obj.y > 0:
                return obj.x, obj.y-1
            if abs(obj.rect.right - wall.rect.left) < 10 and obj.x > 0:
                return obj.x-1, obj.y
            if abs(obj.rect.left - wall.rect.right) < 10 and obj.x > 0:
                return obj.x+1, obj.y

    for tank in tank_list:
        tank_collision = obj.rect.colliderect(tank.rect)
        if tank_collision:
            if abs(obj.rect.top - tank.rect.bottom) < 10 and obj.y > 0:
                return obj.x, obj.y+1
            if abs(obj.rect.bottom - tank.rect.top) < 10 and obj.y > 0:
                return obj.x, obj.y-1
            if abs(obj.rect.right - tank.rect.left) < 10 and obj.x > 0:
                return obj.x-1, obj.y
            if abs(obj.rect.left - tank.rect.right) < 10 and obj.x > 0:
                return obj.x+1, obj.y

    return new_x, new_y


# sprite setup
drawGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

# tank setup
l_tank = pygame.sprite.Sprite(drawGroup)
l_tank_angle = settings.p1_angle
l_tank.x = settings.p1_x
l_tank.y = settings.p1_y

r_tank = pygame.sprite.Sprite(drawGroup)
r_tank_angle = settings.p2_angle
r_tank.x = settings.p2_x
r_tank.y = settings.p2_y

tank_list = []
tank_list.append(l_tank)
tank_list.append(r_tank)

# bullet setup
l_bullet = pygame.sprite.Sprite(drawGroup)
l_bullet_angle = l_tank_angle
l_bullet.x = l_tank.x
l_bullet.y = l_tank.y
draw_objects(l_bullet, 10000, 10000, 10, 10, "Sprites/obstacle.png", l_bullet_angle)

r_bullet = pygame.sprite.Sprite(drawGroup)
r_bullet_angle = r_tank_angle
r_bullet.x = r_tank.x
r_bullet.y = r_tank.y
draw_objects(r_bullet, 10000, 10000, 10, 10, "Sprites/obstacle.png", r_bullet_angle)

# draw battlefield
wall_list = []
for i in range(len(settings.brick_positions)):
    wall = pygame.sprite.Sprite(drawGroup)
    draw_objects(wall, settings.brick_positions[i][0],
                 settings.brick_positions[i][1],
                 settings.brick_positions[i][2],
                 settings.brick_positions[i][3],
                 "Sprites/obstacle.png", 0)
    wall_list.append(wall)

# main loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        # Command to close the game
        if event.type == pygame.QUIT:
            game_loop = False

    # get keys
    keys = pygame.key.get_pressed()

    # left tank controls
    if keys[pygame.K_d]:
        l_tank_angle += 1
        l_tank_angle %= 360

    if keys[pygame.K_a]:
        l_tank_angle -= 1
        l_tank_angle %= 360

    if keys[pygame.K_w]:
        l_tank.x, l_tank.y = move_tank(l_tank, settings.tank_speed,
                                       l_tank_angle)

    if keys[pygame.K_s]:
        #l_bullet.rect.centerx = l_tank.rect.centerx
        #l_bullet.rect.centery = l_tank.rect.centery
        l_bullet_angle = l_tank_angle
        draw_objects(l_bullet, l_tank.rect.centerx, l_tank.rect.centery, 10, 10, "Sprites/obstacle.png", l_bullet_angle)

    # right tank controls
    if keys[pygame.K_LEFT]:
        r_tank_angle += 1
        r_tank_angle %= 360

    if keys[pygame.K_RIGHT]:
        r_tank_angle -= 1
        r_tank_angle %= 360

    if keys[pygame.K_UP]:
        r_tank.x, r_tank.y = move_tank(r_tank, settings.tank_speed,
                                       r_tank_angle)
    if keys[pygame.K_DOWN]:
        r_bullet_angle = r_tank_angle
        r_bullet.rect.centerx = r_tank.rect.centerx
        r_bullet.rect.centery = r_tank.rect.centery

    l_bullet.rect.x += (1 * math.cos(math.radians(l_tank_angle)))
    l_bullet.rect.y -= (1 * math.sin(math.radians(l_tank_angle)))
    print(l_tank_angle)
    print(l_bullet_angle)

    draw_objects(l_tank, l_tank.x, l_tank.y, 40, 40,
                 "Sprites/l_tank.png", l_tank_angle)
    draw_objects(r_tank, r_tank.x, r_tank.y, 40, 40,
                 "Sprites/r_tank.png", r_tank_angle)

    # update screen
    screen.fill(settings.screen_color)
    drawGroup.draw(screen)
    bulletGroup.draw(screen)
    game_clock.tick(60)
    pygame.display.update()

pygame.quit()
