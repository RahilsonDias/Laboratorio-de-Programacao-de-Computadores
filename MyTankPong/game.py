import pygame.mixer

from tank import Tank
from config import *
from score import Score

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

class Game:
    pygame.mixer.init()

    def __init__(self):
        self.game_loop = True
        self.clock = pygame.time.Clock()

        self.player1_rect = pygame.Rect(80, 375, 40, 40)
        self.player2_rect = pygame.Rect(1160, 375, 40, 40)
        self.score_a = self.score_b = 0
        self.bullets = []

        self.tank_1 = Tank(0, self.player1_rect, "sprites/player1.png", RED)
        self.tank_2 = Tank(180, self.player2_rect, "sprites/player2.png", BLUE)
        self.sound_explosion = pygame.mixer.Sound("sound/explosion.mp3")
        self.sound_explosion.set_volume(0.5)

    def run(self):
        self.clock.tick(60)

        score_1 = Score(self.score_a, 300, RED)
        score_2 = Score(self.score_b, 980, BLUE)

        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_loop = False
                    if event.key == pygame.K_s:
                        self.bullets.append(self.tank_1.shot_bullet())
                    if event.key == pygame.K_DOWN:
                        self.bullets.append(self.tank_2.shot_bullet())
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.bullets.append(self.tank_1.shot_bullet())
                
                if event.type == pygame.JOYHATMOTION:
                    print(event)
                    if event.value[0] == 1:
                        self.tank_1.joy_move(1, 0, 0)
                    if event.value[0] == -1:
                        self.tank_1.joy_move(-1, 0, 0)
                    if event.value[1] == 1:
                        self.tank_1.joy_move(0, 1, 1)


            keys = pygame.key.get_pressed()

            # Move p1
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.draw()
            # Move p2
            self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
            self.tank_2.draw()

            # start shot
            for b in self.bullets:
                b.move()
                if b.get_data()[0] == -40:
                    self.bullets.remove(b)

                elif self.tank_1.player_death(b.get_data()):
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.score_a += 1
                    score_2.upload_score(self.score_a)
                    self.bullets.remove(b)

                elif self.tank_2.player_death(b.get_data()):
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.score_b += 1
                    score_1.upload_score(self.score_b)
                    self.bullets.remove(b)

            score_1.draw(screen)
            score_2.draw(screen)

            pygame.display.update()
            screen.fill("#641E0A")


game = Game()
game.run()
