import pygame
from pygame import gfxdraw

MAX_FRUIT_LEVEL = 11
FRICTION_FACTOR = 8.0
MAX_FRUIT_SPEED = 200
FRUIT_RADIUS = {i: 13 * (2 ** (1 / 3)) ** i for i in range(1, MAX_FRUIT_LEVEL + 1)}
FRUIT_COLOR = {
    # i: tuple(random.randint(50,255) for _ in range(3)) for i in range(1, MAX_FRUIT_LEVEL + 1)
    1: '#f00608',
    2: '#f4674b',
    3: '#8f60e7',
    4: '#db9901',
    5: '#ce7126',
    6: '#c01010',
    7: '#cbc165',
    8: '#d1aca5',
    9: '#f5e105',
    10: '#91d00f',
    11: '#087806'
}


def color_hex2tup(hexcolor):
    assert len(hexcolor) == 7 and hexcolor.startswith('#')
    return tuple(int(hexcolor[i:i + 2], 16) for i in (1, 3, 5))


class Fruit:
    def __init__(self, level, x, y):
        # TODO : Add rotation and friction?
        assert 1 <= level <= MAX_FRUIT_LEVEL
        self.level = level
        self.radius = FRUIT_RADIUS[level]
        self.mass = 0.1 * level
        self.color = color_hex2tup(FRUIT_COLOR[level])
        self.is_merging = False

        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

    def draw(self, surf):
        gfxdraw.aacircle(surf,
                         int(self.position.x),
                         int(self.position.y),
                         int(self.radius),
                         self.color)
        gfxdraw.filled_circle(surf,
                              int(self.position.x),
                              int(self.position.y),
                              int(self.radius),
                              self.color)

        # pygame.draw.circle(surf,
        #                    self.color,
        #                    self.position,
        #                    self.radius)

    def update(self, dt):
        # print(self.acceleration, self.speed, self.position)
        self.acceleration += (-self.speed * FRICTION_FACTOR)
        self.speed += self.acceleration * dt
        if self.speed.magnitude() > 0:
            self.speed = self.speed.clamp_magnitude(MAX_FRUIT_SPEED)
        self.position += self.speed * dt
