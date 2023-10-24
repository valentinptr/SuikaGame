import pygame
def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.

    # Redraw screen here.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()