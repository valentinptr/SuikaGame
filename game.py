from objects import *
class Engine():
    def __init__(self):
        self.fruits = []
        self.score = 0

    def update(self, dt):
        for fruit in self.fruits:
            fruit.y += 0.1
    def drawBackground(self, screen):
        screen.fill((50, 50, 50))

    def drawFruits(self, screen):
        for fruit in self.fruits:
            fruit.drawFruit(screen)
    def dropFruit(self, id, x, y):
        new_fruit = Fruit(id, x, y)
        self.fruits.append(new_fruit)
        return new_fruit
