import pygame

def generate_food_position(screen_width, screen_height, block_size):
    import random
    x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
    return x, y

def display_message(screen, font, message, color, position):
    text = font.render(message, True, color)
    screen.blit(text, position)

def draw_snake(screen, color, snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, color, [segment[0], segment[1], snake_block, snake_block])