

import pygame
import random

pygame.init()

# Create the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# Snake settings
size = 20
speed = 20

# Snake body
snake = [(200, 200), (180, 200), (160, 200)]

# Starting direction
dx = speed
dy = 0

# Create food at a random position
food_x = random.randrange(0, 400, size)
food_y = random.randrange(0, 400, size)

# Make sure food does not appear on the snake
while (food_x, food_y) in snake:
    food_x = random.randrange(0, 400, size)
    food_y = random.randrange(0, 400, size)

running = True
game_over = False

while running:

    # Check keyboard and window events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if dy == 0:
                    dx = 0
                    dy = -speed

            elif event.key == pygame.K_DOWN:
                if dy == 0:
                    dx = 0
                    dy = speed

            elif event.key == pygame.K_LEFT:
                if dx == 0:
                    dx = -speed
                    dy = 0

            elif event.key == pygame.K_RIGHT:
                if dx == 0:
                    dx = speed
                    dy = 0

            

    # Find the head's position
    head_x = snake[0][0]
    head_y = snake[0][1]

    # Calculate the new head position
    new_x = head_x + dx
    new_y = head_y + dy


    # Check if the snake hits itself
    if (new_x, new_y) in snake[1:]:
        game_over= True
        running = False


    # Keep the snake inside the window
    if new_x < 0:
        new_x = 0
    if new_x > 380:
        new_x = 380
    if new_y < 0:
        new_y = 0
    if new_y > 380:
        new_y = 380

    # Add the new head
    snake.insert(0, (new_x, new_y))

    # Check if the snake eats the food
    if new_x == food_x and new_y == food_y:

        # Create new food
        food_x = random.randrange(0, 400, size)
        food_y = random.randrange(0, 400, size)

        # Do not place food on the snake
        while (food_x, food_y) in snake:
            food_x = random.randrange(0, 400, size)
            food_y = random.randrange(0, 400, size)

    else:
        # Remove the last square only if food was not eaten
        snake.pop()

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the food in red
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (food_x, food_y, size, size)
    )

    # Draw the snake in green
    for part in snake:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (part[0], part[1], size, size)
        )

    pygame.display.update()

    pygame.time.delay(150)


# Show Game Over message
if game_over:
    screen.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 50)

    text = font.render(
        "GAME OVER!",
        True,
        (255, 0, 0)
    )

    screen.blit(text, (85, 175))
    pygame.display.update()

    # Keep the window open until it is closed
    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

pygame.quit()


  