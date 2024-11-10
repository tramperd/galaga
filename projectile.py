import os
import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemies):
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'shot.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.centerx  # Center projectile horizontally based on player
        self.rect.centery = shipLocation.top  # Start the projectile just above the player's ship
        self.enemies = enemies
        self.event = pg.USEREVENT + 1
        self.fireSound = pg.mixer.Sound("fire.wav")
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound("explosion.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.x += 1000 * delta  # Move projectile rightwards
        if self.rect.x > 1024:  # If the projectile goes off screen, remove it
            self.kill()
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()  # Remove the enemy
            pg.event.post(pg.event.Event(self.event))  # Trigger the event for score update
            self.explosionSound.play()  # Play explosion sound
            self.kill()  # Remove the projectile

