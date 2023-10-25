from objects import *
import pygame

BACKGROUND_COLOR = (50, 50, 50)
BACKGROUND_WALL = 'black'
WALL_THICKNESS = 15
WALL_LENGTH = 600
WALL_START_POSITION_X = 50
WALL_END_POSITION_X = 550
WALL_START_POSITION_Y = 100
class Engine():
    def __init__(self):
        self.fruits = []
        self.score = 0

    def update(self, dt):
        for fruit in self.fruits:
            fruit.y += 1
    def drawBackground(self, screen):
        screen.fill(BACKGROUND_COLOR)
        #Mur gauche
        pygame.draw.line(screen, BACKGROUND_WALL,
                         (WALL_START_POSITION_X, WALL_START_POSITION_Y),
                         (WALL_START_POSITION_X, WALL_START_POSITION_X + WALL_LENGTH),
                         WALL_THICKNESS )
        # Mur droit
        pygame.draw.line(screen, BACKGROUND_WALL,
                         (WALL_END_POSITION_X, WALL_START_POSITION_Y),
                         (WALL_END_POSITION_X, WALL_START_POSITION_X + WALL_LENGTH),
                         WALL_THICKNESS)

        # Mur bas
        pygame.draw.line(screen, BACKGROUND_WALL,
                         (WALL_START_POSITION_X - (WALL_THICKNESS / 2), WALL_START_POSITION_X + WALL_LENGTH + (WALL_THICKNESS / 2)),
                         (WALL_END_POSITION_X + (WALL_THICKNESS / 2), WALL_START_POSITION_X + WALL_LENGTH + (WALL_THICKNESS / 2)),
                         WALL_THICKNESS)

    def drawFruits(self, screen):
        for fruit in self.fruits:
            fruit.drawFruit(screen)
    def dropFruit(self, id, x, y):
        new_fruit = Fruit(id, x, y)
        self.fruits.append(new_fruit)
        return new_fruit
