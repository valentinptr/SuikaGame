import pygame
import sys
from pygame.locals import *
#from objects import *
from game import *

# Set up the window.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 750
CURSOR_SPEED = 200
fps = 60.0

pygame.init()
fpsClock = pygame.time.Clock()


x = WINDOW_WIDTH / 2
y = 40
vX = 1
vY = 1

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Suika Game")

dt = 0#1 / fps  # dt is the time since last frame.

engine = Engine()
current_fruit = Fruit(1, x, y)

while True:  # Loop forever!

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                engine.dropFruit(current_fruit.id, current_fruit.position.x, current_fruit.position.y)

    engine.update(dt)
    engine.drawBackground(screen)
    engine.drawFruits(screen)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        x -= CURSOR_SPEED * dt
    if keys_pressed[pygame.K_RIGHT]:
        x += CURSOR_SPEED * dt

    pygame.display.flip()
    dt = pygame.time.Clock().tick(60) / 1000#dt = fpsClock.tick(fps)