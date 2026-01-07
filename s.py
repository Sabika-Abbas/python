import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
black = (0, 0, 0)

# Snake and food size
block_size = 20
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 50)

# Clock to control the game's speed
clock = pygame.time.Clock()

# Snake attributes
snake_block = 20
snake_list = []
snake_length = 1

# Initial position of the snake
x1, y1 = width / 2, height / 2
snake_list.append((x1, y1))

# Direction variables
x1_change, y1_change = 0, 0

# Food position
foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
foody = round(random.randrange(0, height - block_size) / block_size) * block_size

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# Main game loop
game_over = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -block_size
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = block_size
                x1_change = 0

    # Update snake position
    x1 += x1_change
    y1 += y1_change

    # Check if the snake eats the food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
        foody = round(random.randrange(0, height - block_size) / block_size) * block_size
        snake_length += 1

    # Update snake length
    snake_head = (x1, y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collisions with walls or itself
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0 or snake_head in snake_list[:-1]:
        game_over = True

    # Refresh the display
    display.fill(white)
    pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
    our_snake(block_size, snake_list)
    pygame.display.update()

    # Set the speed of the game
    clock.tick(snake_speed)

# Display game over message
message = font_style.render("Game Over!", True, black)
display.blit(message, [width / 3, height / 3])
pygame.display.update()
time.sleep(2)

# Quit Pygame
pygame.quit()
quit()
