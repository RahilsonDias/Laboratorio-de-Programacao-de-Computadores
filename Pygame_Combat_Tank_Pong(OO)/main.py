import pygame

from game import Game

pygame.init()

game = Game(800, 600)
game.run()

pygame.quit()
