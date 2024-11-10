import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # TODO

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        # TODO
        pass

    def down(self, delta):
        # TODO
        pass
