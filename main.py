import pygame as pg
import pygame.freetype
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from pygame.locals import *

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])

    # Create a player
    player = Player()

    # Create enemy and projectile Groups
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()

    # Create enemies
    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i, j))
            enemies.add(enemy)

    # Start sound - Load background music and start it playing on a loop
    pg.mixer.music.load(os.path.join('assets', 'cpu-talk.mp3'))
    pg.mixer.music.play(loops=-1, start=0.0)

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)

    # Make a tuple for FONTCOLOR
    FONTCOLOR = (255, 255, 255)  # White color for score text

    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 250
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()

    # Setup score variable
    score = 0
    while running:
        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100

        # Player movement and shooting logic
        keys = pg.key.get_pressed()

        if keys[K_s]:
            player.down(delta)
        if keys[K_w]:
            player.up(delta)
        if keys[K_SPACE]:
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies)
                projectiles.add(projectile)
                shotDelta = 0

        # Check if all enemies are cleared
        if not enemies:
            # You could add a win condition here or restart the level
            print("All enemies cleared!")
            running = False  # Exit the game for now after clearing enemies

        # Update game objects
        player.update(delta)
        for enemy in enemies:
            enemy.update(delta)
        for projectile in projectiles:
            projectile.update(delta)

        # Draw everything
        screen.fill((0, 0, 0))  # Fill screen with black
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=64)

        # Flip the display
        pg.display.flip()

        # Time tracking for FPS and shot delay
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta

# Startup the main method to get things going
if __name__ == "__main__":
    main()
    pg.quit()

