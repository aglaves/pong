""" Game class """

import pygame
import colors
from paddle import Paddle

ACTION_UNKNOWN = -1
ACTION_QUIT = 0
ACTION_PLAYER1_UP = 1
ACTION_PLAYER1_DOWN = 2
ACTION_PLAYER1_STOP = 3
ACTION_PLAYER2_UP = 4
ACTION_PLAYER2_DOWN = 5
ACTION_PLAYER2_STOP = 6

KEY_UNKNOWN = -1
KEY_PLAYER1_DOWN = pygame.K_z
KEY_PLAYER1_UP = pygame.K_a
KEY_PLAYER2_DOWN = pygame.K_DOWN
KEY_PLAYER2_UP = pygame.K_UP

class Game:
    """The basic game object which controls the running of the game."""

    def __init__(self):
        pygame.init()

        self.all_sprites_list = pygame.sprite.Group()
        self.paddle1 = init_paddle(colors.WHITE, 20, 200, 10, 100)
        self.paddle2 = init_paddle(colors.WHITE, 670, 200, 10, 100)
        self.all_sprites_list.add(self.paddle1)
        self.all_sprites_list.add(self.paddle2)
        self.init_screen()

        self.running = True

    def run(self):
        """The basic game loop"""

        clock = pygame.time.Clock()
        while self.running:
            self.process_events()
            self.paddle1.move()
            self.paddle2.move()
            self.all_sprites_list.update()
            self.draw_screen()
            clock.tick(60)

    def init_screen(self):
        """Initialize the home scren"""

        size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pong")

    def quit(self):
        """Stop the game and quit"""
        pygame.quit()

    def process_events(self):
        """Process the pygame events"""

        for event in pygame.event.get():
            action = check_event(event)
            if action == ACTION_QUIT:
                self.running = False
            if action == ACTION_PLAYER1_UP:
                self.paddle1.begin_move_up()
            if action == ACTION_PLAYER1_DOWN:
                self.paddle1.begin_move_down()
            if action == ACTION_PLAYER2_UP:
                self.paddle2.begin_move_up()
            if action == ACTION_PLAYER2_DOWN:
                self.paddle2.begin_move_down()
            if action == ACTION_PLAYER1_STOP:
                self.paddle1.end_movement()
            if action == ACTION_PLAYER2_STOP:
                self.paddle2.end_movement()

    def draw_screen(self):
        """ Draw the screen and sprites"""
        self.screen.fill(colors.BLACK)
        pygame.draw.line(self.screen, colors.WHITE, [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen)
        pygame.display.flip()

def check_event(event):
    """Checks the event type and returns the appropriate action to take"""

    if event.type == pygame.QUIT:
        return ACTION_QUIT
    if event.type == pygame.KEYDOWN:
        return check_pressed_key(event.key)
    if event.type == pygame.KEYUP:
        return check_released_key(event.key)
    return ACTION_UNKNOWN

def check_pressed_key(pressed_key):
    """Checks the key pressed and retuens the appropriate action to take"""

    if pressed_key == pygame.K_x:
        return ACTION_QUIT
    if pressed_key == KEY_PLAYER1_UP:
        return ACTION_PLAYER1_UP
    if pressed_key == KEY_PLAYER1_DOWN:
        return ACTION_PLAYER1_DOWN
    if pressed_key == KEY_PLAYER2_UP:
        return ACTION_PLAYER2_UP
    if pressed_key == KEY_PLAYER2_DOWN:
        return ACTION_PLAYER2_DOWN
    return KEY_UNKNOWN

def check_released_key(released_key):
    """Checks the key pressed and retuens the appropriate action to take"""

    if released_key == KEY_PLAYER1_UP:
        return ACTION_PLAYER1_STOP
    if released_key == KEY_PLAYER1_DOWN:
        return ACTION_PLAYER1_STOP
    if released_key == KEY_PLAYER2_UP:
        return ACTION_PLAYER2_STOP
    if released_key == KEY_PLAYER2_DOWN:
        return ACTION_PLAYER2_STOP
    return KEY_UNKNOWN

def init_paddle(color, x_position, y_position, width, height):
    """Create and position a new paddle"""

    paddle = Paddle(color, width, height)
    paddle.rect.x = x_position
    paddle.rect.y = y_position
    return paddle
