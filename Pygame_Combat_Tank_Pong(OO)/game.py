import pygame
from tank import Tank
from score import Score
import arena
import collision


class Game(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Combat")

        self.clock = pygame.time.Clock()

        self.game_over = False

        self.player_1 = Tank(70, 340)
        self.bullets_1 = self.player_1.get_player_bullets()
        self.player_2 = Tank(730, 340)
        self.bullets_2 = self.player_2.get_player_bullets()

        self.wall_list = arena.create_arena()

        self.score_a = 0
        self.score_b = 0

        self.game_loop = True

    def run(self):

        # score_2 = Score(self.score_a, 600, (0, 0, 255))
        # score_1 = Score(self.score_b, 200, (0, 255, 0))

        while self.game_loop:
            self.clock.tick(60)
            if not self.game_over:
                for b in self.bullets_1:
                    b.move()
                for b in self.bullets_2:
                    b.move()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.player_1.turn_left()
                if keys[pygame.K_d]:
                    self.player_1.turn_right()
                if keys[pygame.K_w]:
                    self.player_1.move()

                if keys[pygame.K_LEFT]:
                    self.player_2.turn_left()
                if keys[pygame.K_RIGHT]:
                    self.player_2.turn_right()
                if keys[pygame.K_UP]:
                    self.player_2.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if not self.game_over:
                            self.player_1.shoot()
                    if event.key == pygame.K_DOWN:
                        if not self.game_over:
                            self.player_2.shoot()

            collision.wall_collision(self.player_1, self.player_2.get_rect())
            collision.wall_collision(self.player_2, self.player_1.get_rect())

            for wall in self.wall_list:
                collision.wall_collision(self.player_1, wall)
                collision.wall_collision(self.player_2, wall)

            # update self.screen
            self.screen.fill((151, 163, 67, 255))
            self.player_1.draw(self.screen)
            self.player_2.draw(self.screen)

            for b in self.bullets_1:
                if collision.ball_collision(b, self.wall_list):
                    b.set_count()
                if b.get_count() == 2:
                    self.bullets_1.remove(b)
                if b.rect.colliderect(self.player_2):
                    self.score_b += 1
                    self.bullets_1.remove(b)
                b.draw(self.screen)

            for b in self.bullets_2:
                if collision.ball_collision(b, self.wall_list):
                    b.set_count()
                if b.get_count == 2:
                    self.bullets_2.remove(b)
                if b.rect.colliderect(self.player_1):
                    print("True")
                    self.score_a += 1
                    self.bullets_2.remove(b)
                b.draw(self.screen)

            for wall in self.wall_list:
                pygame.draw.rect(self.screen, (253, 181, 104, 255), wall)

            score_2 = Score(self.score_a, 600, (0, 0, 255))
            score_1 = Score(self.score_b, 200, (0, 255, 0))

            score_1.draw(self.screen)
            score_2.draw(self.screen)

            pygame.display.update()
