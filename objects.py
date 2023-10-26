import pygame


class Fruit:
    def __init__(self, id, x, y):
        self.id = id
        self.radius = 30
        self.weight = 10
        self.color = 'gray'
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()
        print('Un fruit a été instancié')

    def drawFruit(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        print(self.acceleration, self.speed, self.position)
        self.speed += self.acceleration * dt
        # if self.speed.magnitude() > 0:
        # self.speed = self.speed.clamp_magnitude(MAX_FRUIT_SPEED)
        self.position += self.speed * dt
