import pygame

class Fruit():
    def __init__(self, id, x, y):
        self.x = x
        self.y = y
        self.id = id
        print("instanciation d'un fruit")

    def drawFruit(self, screen):
        pygame.draw.circle(screen, (250, 250, 0), (self.x, self.y), 30)
