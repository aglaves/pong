"""Player's paddle"""

import pygame
BLACK = (0,0,0)

MOVEMENT_RATE = 10
MOVING_NOT = 0
MOVING_UP = 1
MOVING_DOWN = 2

class Paddle(pygame.sprite.Sprite):
    """The Paddle which moves and deflects the ball"""

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width, height])

        self.rect = self.image.get_rect()

        self.is_moving_down = False
        self.moving = MOVING_NOT

    def begin_move_down(self):
        """Set the paddle's movement to move down the screen."""
        self.moving = MOVING_DOWN
    
    def begin_move_up(self):
        """Set the paddle's movement to move up the screen."""
        self.moving = MOVING_UP

    def end_movement(self):
        """Stop the paddle's movement"""
        self.moving = MOVING_NOT

    def move(self):
        """Move the paddle up or down depending on the paddle's current movement."""
        if self.moving == MOVING_DOWN:
            self.move_down()
        elif self.moving == MOVING_UP:
            self.move_up()

    def move_down(self):
        """Update the paddle's position to move down the screen."""
        self.rect.y = self.rect.y + MOVEMENT_RATE

    def move_up(self):
        """Update the paddle's position to move up the screen."""
        self.rect.y = self.rect.y - MOVEMENT_RATE
        