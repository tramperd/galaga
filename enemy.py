import os
import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship1.png')).convert_alpha()  # You can use any ship image
        self.rect = self.image.get_rect()
        self.rect.topleft = position  # Set position where the enemy spawns

    def update(self, delta):
        # Update enemy's position (e.g., move downward or simulate pattern)
        self.rect.y += 2  # Example: Move down by 2 pixels per frame

        # If the enemy goes off the screen, kill it (for now, we can add a wrap-around or respawn feature later)
        if self.rect.y > 768:
            self.kill()

