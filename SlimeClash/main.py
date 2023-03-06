from settings import *
from game import Game

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption('Slime Clash')
clock = pygame.time.Clock()
bg = pygame.image.load("sprites/StageCave.png")
level = Game()

while True:
	level.run()

	# drawing logic
	pygame.display.update()
	clock.tick(30)
