from objects import *

GRAVITY = 2000
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

BOX_OFFSET_TOP = 100
BOX_OFFSET_HORIZ = 50
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_OFFSET_HORIZ
BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_OFFSET_BOTTOM
BOX_THICKNESS = 20

MAX_FRUIT_LEVEL = 11
FRUIT_COLLISION_STIFFNESS = 1000
BOX_COLOR = 'black'
BACKGROUND_COLOR = '#16a085'
TARGET_LINE_COLOR = 'white'


class GameState:
    def __init__(self):
        self.fruits = []
        self.score = 0

    def update(self, dt):
        # Wall collision + gravity
        for fruit in self.fruits:
            fruit.acceleration = pygame.math.Vector2(0, GRAVITY)
            # Bottom wall
            # print(BOX_POSITION_BOTTOM - fruit.position.y, fruit.radius)
            if BOX_POSITION_BOTTOM - fruit.position.y < fruit.radius:
                fruit.speed.y = -abs(fruit.speed.y)
                fruit.position.y = BOX_POSITION_BOTTOM - fruit.radius

            # Left wall
            if fruit.position.x - BOX_POSITION_LEFT < fruit.radius:
                fruit.speed.x = abs(fruit.speed.x)
                fruit.position.x = BOX_POSITION_LEFT + fruit.radius

            # Right wall
            if BOX_POSITION_RIGHT - fruit.position.x < fruit.radius:
                fruit.speed.x = -abs(fruit.speed.x)
                fruit.position.x = BOX_POSITION_RIGHT - fruit.radius

        # Inter-fruit collision
        fruits_created = []
        for index1, fruit1 in enumerate(self.fruits):
            for index2, fruit2 in enumerate(self.fruits[:index1]):
                f1f2 = fruit2.position - fruit1.position
                if f1f2.magnitude() < fruit1.radius + fruit2.radius:
                    # Collision found!
                    if (fruit1.level == fruit2.level
                            and not fruit1.is_merging
                            and not fruit2.is_merging):
                        self.score += (fruit1.level * (fruit1.level + 1)) // 2
                        fruit1.is_merging = True
                        fruit2.is_merging = True
                        if fruit1.level < MAX_FRUIT_LEVEL:
                            new_fruit_pos = (fruit1.position + fruit2.position) / 2
                            new_fruit = {
                                'level': fruit1.level + 1,
                                'position': new_fruit_pos,
                                'speed': (fruit1.speed + fruit2.speed) / 2
                            }
                            fruits_created.append(new_fruit)
                    else:
                        force_magnitude = abs(
                            f1f2.magnitude() - (fruit1.radius + fruit2.radius)) * FRUIT_COLLISION_STIFFNESS
                        fruit1.acceleration += (f1f2.normalize() * -force_magnitude) / fruit1.mass
                        fruit2.acceleration += (f1f2.normalize() * force_magnitude) / fruit2.mass

        next_fruits = []
        for fruit in self.fruits:
            if not fruit.is_merging:
                fruit.update(dt)
                next_fruits.append(fruit)

        self.fruits = next_fruits

        for new_fruit in fruits_created:
            f = self.dropFruit(new_fruit['level'], new_fruit['position'].x, new_fruit['position'].y)
            f.speed = new_fruit['speed']

    def drawBackground(self, surf):
        surf.fill(BACKGROUND_COLOR)

        # Left wall
        pygame.draw.rect(surf, BOX_COLOR, (BOX_POSITION_LEFT - BOX_THICKNESS,
                                           BOX_OFFSET_TOP,
                                           BOX_THICKNESS,
                                           WINDOW_HEIGHT - BOX_OFFSET_TOP - BOX_OFFSET_BOTTOM))

        # Right wall
        pygame.draw.rect(surf, BOX_COLOR, (BOX_POSITION_RIGHT,
                                           BOX_OFFSET_TOP,
                                           BOX_THICKNESS,
                                           WINDOW_HEIGHT - BOX_OFFSET_TOP - BOX_OFFSET_BOTTOM))

        # Floor (bottom wall)
        pygame.draw.rect(surf, BOX_COLOR, (BOX_POSITION_LEFT - BOX_THICKNESS,
                                           BOX_POSITION_BOTTOM,
                                           BOX_POSITION_RIGHT - BOX_POSITION_LEFT + 2 * BOX_THICKNESS,
                                           BOX_THICKNESS))

    def drawFruits(self, surf):
        for fruit in self.fruits:
            fruit.draw(surf)

    def draw(self, surf):
        self.drawBackground(surf)
        self.drawFruits(surf)

    def dropFruit(self, level, x, y):
        new_fruit = Fruit(level, x, y)
        self.fruits.append(new_fruit)
        return new_fruit
