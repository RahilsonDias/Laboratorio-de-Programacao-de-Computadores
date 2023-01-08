# pygame setup
import pygame
import random
import math
pygame.init()

# color setup
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
GREEN = (0, 127, 33)
YELLOW = (255, 255, 0)

# score and lives
score = 0
lives = 3

# window setup
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Breakout")

# sound setup
bounce_block_sound = pygame.mixer.Sound('Blip_Block.wav')
bounce_paddle_sound = pygame.mixer.Sound('Blip_Paddle.wav')
bounce_wall_sound = pygame.mixer.Sound('Blip_Wall.wav')

# paddle setup
paddle_w = 50
paddle_h = 15
paddle_speed = 15
paddle = pygame.Rect(width//2 - paddle_w//2, height - paddle_h - 10,
                     paddle_w, paddle_h)

# ball setup
ball_radius = 10
ball_speed = 5
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect), height//2,
                   ball_rect, ball_rect)
dx, dy = 1, -1

# block wall setup
block_list = []
for i in range(14):
    for j in range(8):
        block = pygame.Rect(5 + 42.5 * i, 45 + 20 * j, 37.5, 15)
        block_list.append(block)

color_list = []
for i in range(14):
    for j in range(8):
        if j < 2:
            color = RED
        elif 2 <= j < 4:
            color = ORANGE
        elif 4 <= j < 6:
            color = GREEN
        else:
            color = YELLOW
        color_list.append(color)


# collision detection between ball and block
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 5:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_x < delta_y:
        dx = -dx
    return dx, dy


# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # draw objects
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 38], [600, 38], 2)
    pygame.draw.rect(screen, LIGHTBLUE, paddle)
    pygame.draw.rect(screen, WHITE, ball)
    for color, block in enumerate(block_list):
        pygame.draw.rect(screen, color_list[color], block)

    # ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # collision with left and right wall
    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        dx = -dx
        bounce_wall_sound.play()

    # collision with top wall
    if ball.centery < ball_radius:
        dy = -dy
        bounce_wall_sound.play()

    # collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        angle = -90 + 120 * ((ball.centerx - paddle.centerx) / paddle.width)
        dy = math.sin(angle*(math.pi/180))
        bounce_paddle_sound.play()

    # collision with blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)

        if hit_color == YELLOW:
            score += 1
        elif hit_color == GREEN:
            score += 3
        elif hit_color == ORANGE:
            score += 5
        elif hit_color == RED:
            score += 7

        bounce_block_sound.play()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < width:
        paddle.right += paddle_speed

    # ui
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (500, 10))

    # victory / game over
    if ball.bottom > height:
        if lives > 0:
            lives -= 1
            ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect),
                               height//2, ball_rect, ball_rect)

        else:
            text = font.render("Game Over!", 1, WHITE)
            screen.blit(text, (width//2 - 70, height//2))

    elif not len(block_list):

        # rebuild block wall
        block_list = []
        for i in range(14):
            for j in range(8):
                block = pygame.Rect(5 + 42.5 * i, 45 + 20 * j, 37.5, 15)
                block_list.append(block)

        color_list = []
        for i in range(14):
            for j in range(8):
                if j < 2:
                    color = RED
                elif 2 <= j < 4:
                    color = ORANGE
                elif 4 <= j < 6:
                    color = GREEN
                else:
                    color = YELLOW
                color_list.append(color)

        for color, block in enumerate(block_list):
            pygame.draw.rect(screen, color_list[color], block)
        ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect),
                           height//2, ball_rect, ball_rect)

    # screen update
    pygame.display.flip()
    game_clock.tick(60)

# quit on end
pygame.quit()
