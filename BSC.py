import pygame
import sys
import random


# Initialize Pygame
pygame.init()
# Set up the display
width, height = 400, 600
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bell State Collector")

# Load background image
background_image = pygame.image.load('background_image.jpg')
background_image = pygame.transform.scale(background_image, (width, height))

# Snake settings
snake_image = pygame.image.load('qubit.svg')
snake_image = pygame.transform.scale(snake_image, (cell_size, cell_size))
snake = [(snake_image, 100, 100), (snake_image, 90, 100), (snake_image, 80, 100)]
snake_direction = (1, 0)
i=0
snake_eaten = 0
high_score = 0

# Food settings
food_a_image = pygame.image.load('food_a.png')
food_a_image = pygame.transform.scale(food_a_image, (cell_size, cell_size))

food_b_image = pygame.image.load('food_b.png')
food_b_image = pygame.transform.scale(food_b_image, (cell_size, cell_size))

food_a = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)

food_b = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)

# Font for displaying the score
font = pygame.font.Font(None, 24)

# Start button settings
start_button_rect = pygame.Rect((width // 2 - 50, height // 2 - 25, 100, 50))
start_button_color = (255, 215, 0)
start_button_text = font.render("Let's start!", True, (0, 0, 0))
start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)

# Game loop
clock = pygame.time.Clock()

def reset_game():
    global snake, snake_direction, food_a, food_b, snake_eaten, game_over, display_message, high_score, i
    snake = [(snake_image, 100, 100), (snake_image, 90, 100), (snake_image, 80, 100)]
    snake_direction = (1, 0)
    snake_eaten = 0
    i+=1
    food_a = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)

    food_b = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)
    game_over = False
    display_message = False

# Variables to track game over state and message display
game_over = False
display_message = False
start_button_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button_rect.collidepoint(event.pos) and not start_button_pressed:
                start_button_pressed = True
                reset_game()

    keys = pygame.key.get_pressed()
    if not game_over and start_button_pressed:
        if keys[pygame.K_UP] and snake_direction != (0, 1):
            snake_direction = (0, -1)
        elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
            snake_direction = (0, 1)
        elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
            snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
            snake_direction = (1, 0)
    elif game_over and keys[pygame.K_SPACE]:
        reset_game()
        game_over = False
        display_message = False
        display_message2 = False
        

    if not game_over and start_button_pressed:
        # Update snake position
        head = (snake[0][0], snake[0][1] + snake_direction[0] * cell_size, snake[0][2] + snake_direction[1] * cell_size)
        snake.insert(0, head)

        # Check for collisions
        if head[1:] == food_a:
            snake_eaten += 1
            high_score = max(snake_eaten,high_score)
            food_a = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)
        elif head[1:] == food_b:
            snake_eaten += 1
            high_score = max(snake_eaten,high_score)
            food_b = (random.randrange(1, (width-20) // cell_size) * cell_size,
          random.randrange(1, (height-20) // cell_size) * cell_size)
        else:
            snake.pop()

        if (head[1] < 0 or head[1] >= width or
                head[2] < 0 or head[2] >= height or
                head[1:] in [segment[1:] for segment in snake[1:]]):
            # Game over
            game_over = True
            display_message = True

    # Draw to the screen
    screen.blit(background_image, (0, 0))

    for segment in snake:
        screen.blit(segment[0], (segment[1], segment[2]))

    screen.blit(food_a_image, (food_a[0], food_a[1]))
    screen.blit(food_b_image, (food_b[0], food_b[1]))

    if not start_button_pressed:
        pygame.draw.rect(screen, start_button_color, start_button_rect)
        screen.blit(start_button_text, start_button_text_rect)

    # Display the score
    score_text = font.render(f"Score: {snake_eaten}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    score_text = font.render(f"Highest Score: {high_score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 570))

    if high_score>=8:
        image = pygame.image.load('c.png')
        image = pygame.transform.scale(image, (2*cell_size, 2*cell_size))
        screen.blit(image, (150, 555))
        a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        screen.blit(a_image, (a[0], a[1]))
        screen.blit(b_image, (b[0], b[1]))
    if high_score>=16:
        image2 = pygame.image.load('b.png')
        image2 = pygame.transform.scale(image2, (2*cell_size, 2*cell_size))
        screen.blit(image2, (200, 555))
        a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        screen.blit(a_image, (a[0], a[1]))
        screen.blit(b_image, (b[0], b[1]))
    if high_score>=32:
        image3 = pygame.image.load('a.png')
        image3 = pygame.transform.scale(image3, (2*cell_size, 2*cell_size))
        screen.blit(image3, (250, 555))
        a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        screen.blit(a_image, (a[0], a[1]))
        screen.blit(b_image, (b[0], b[1]))
    if high_score>=64:
        image4 = pygame.image.load('ss.png')
        image4 = pygame.transform.scale(image4, (2*cell_size, 2*cell_size))
        screen.blit(image4, (300, 555))
        a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        screen.blit(a_image, (a[0], a[1]))
        screen.blit(b_image, (b[0], b[1]))
    if high_score>=128:
        image5 = pygame.image.load('sss.png')
        image5 = pygame.transform.scale(image5, (2*cell_size, 2*cell_size))
        screen.blit(image5, (350, 555))
        a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
        screen.blit(a_image, (a[0], a[1]))
        screen.blit(b_image, (b[0], b[1]))
        game_over = True
        game_over_text = font.render("Congratulations! You have got all rewards!", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, text_rect)
        
    if high_score<=2:
        score_text = font.render(f"Let's get your first reward!", True, (255, 0, 0))
        screen.blit(score_text, (150, 570))

    a_image = pygame.image.load('food_a.png')
    a_image = pygame.transform.scale(food_a_image, (cell_size, cell_size))
    b_image = pygame.image.load('food_b.png')
    b_image = pygame.transform.scale(food_b_image, (cell_size, cell_size))
    a = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
    b = (random.randrange(1, width // cell_size) * cell_size,
          random.randrange(1, height // cell_size) * cell_size)
    screen.blit(a_image, (a[0], a[1]))
    screen.blit(b_image, (b[0], b[1]))

    if display_message:
        game_over_text = font.render("Press SPACE to Try Again", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()

    # Control the speed of the game
    clock.tick(10)
