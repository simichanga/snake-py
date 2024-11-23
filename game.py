import pygame
from settings import *
from utils import *

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.score_font = pygame.font.SysFont("Arial", 35)

        self.reset_game()
    
    def reset_game(self):
        self.game_over = False
        self.game_close = False

        self.x1 = WINDOW_WIDTH // 2
        self.y1 = WINDOW_HEIGHT // 2
        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.snake_length = 1

        self.foodx, self.foody = generate_food_position(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_BLOCK)
