import random
from settings import *


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['life', 'invis'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.lifetime = 0

    def update(self):
        self.lifetime += 1
        if self.lifetime > 150:
            self.kill()
