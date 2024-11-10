import os
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()  # Player's spaceship
        self.rect = self.image.get_rect()
        self.rect.center = (1024 // 2, 768 - 50)  # Start at the bottom center of the screen

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass  # Player doesn't move unless controlled

    def up(self, delta):
        if self.rect.top > 0:  # Prevent moving off-screen
            self.rect.y -= 5  # Move player up by 5 pixels

    def down(self, delta):
        if self.rect.bottom < 768:  # Prevent moving off-screen
            self.rect.y += 5  # Move player down by 5 pixels

