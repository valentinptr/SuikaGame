import random

from game import *
from objects import *

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

BOX_OFFSET_TOP = 100
BOX_OFFSET_HORIZ = 50
BOX_OFFSET_BOTTOM = 100
BOX_POSITION_LEFT = BOX_OFFSET_HORIZ
BOX_POSITION_RIGHT = WINDOW_WIDTH - BOX_OFFSET_HORIZ
CURSOR_Y = 50
CURSOR_SPEED = 200

BOX_POSITION_BOTTOM = WINDOW_HEIGHT - BOX_OFFSET_BOTTOM
BOX_THICKNESS = 20

BOX_COLOR = 'black'
BACKGROUND_COLOR = '#16a085'
TARGET_LINE_COLOR = 'white'

GRAVITY = 2000
FRUIT_COLLISION_STIFFNESS = 1000
FRICTION_FACTOR = 8.0
MAX_FRUIT_SPEED = 200

MAX_FRUIT_LEVEL = 11
MIN_RANDOM_LEVEL = 1
MAX_RANDOM_LEVEL = 5
RESPAWN_TIME = 500

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

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
game_state = GameState()

cursor_x = WINDOW_WIDTH / 2
current_fruit = Fruit(random.randint(MIN_RANDOM_LEVEL, MAX_RANDOM_LEVEL), cursor_x, CURSOR_Y)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_fruit is not None:
                game_state.dropFruit(current_fruit.level, current_fruit.position.x + random.random(),
                                     current_fruit.position.y)
                current_fruit = None
                drop_time = pygame.time.get_ticks()

    game_state.update(dt)
    game_state.drawBackground(screen)
    if current_fruit is not None:
        endPos = pygame.math.Vector2(current_fruit.position.x, BOX_POSITION_BOTTOM)
        pygame.draw.line(
            screen,
            TARGET_LINE_COLOR,
            current_fruit.position,
            endPos,
            3
        )
    game_state.drawFruits(screen)

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        cursor_x -= CURSOR_SPEED * dt
    if keys_pressed[pygame.K_RIGHT]:
        cursor_x += CURSOR_SPEED * dt

    if current_fruit is None:
        if pygame.time.get_ticks() - drop_time > RESPAWN_TIME:
            current_fruit = Fruit(random.randint(MIN_RANDOM_LEVEL, MAX_RANDOM_LEVEL), cursor_x, CURSOR_Y)
    else:
        cursor_x = min(cursor_x, BOX_POSITION_RIGHT - current_fruit.radius)
        cursor_x = max(cursor_x, BOX_POSITION_LEFT + current_fruit.radius)

        current_fruit.position.x = cursor_x
        current_fruit.draw(screen)

    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(f'{game_state.score}', True, 'white')
    screen.blit(text_render, (50, BOX_POSITION_BOTTOM + 33))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
