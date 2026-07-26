import pygame
import random
import os

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Define Colours (RGB)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Create Game Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game by Rushant")

# Load and Resize Background Image
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert()

# Create Clock and Font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


# Function: Display Text on the Screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


# Function: Draw Snake
# Draws each block of the snake using rectangles.
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Function: Welcome Screen
# Displays the start screen and waits until the
# player presses SPACE to begin the game.
def welcome():
    while True:
        gameWindow.fill((233, 210, 229))

        text_screen("Welcome to Snake Game by Rushant!", red, 100, 220)
        text_screen("Press SPACE BAR to Play", black, 200, 290)

        for event in pygame.event.get():

            # Close the game window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Start game when SPACE is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    # Play background music in loop
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play(-1)

                    # Restart game after Game Over
                    while gameloop():
                        pygame.mixer.music.load("background.mp3")
                        pygame.mixer.music.play(-1)

        pygame.display.update()
        clock.tick(60)


# Function: Main Game Loop
# Controls gameplay, movement, scoring, collision,
# and restart functionality.
def gameloop():

    exit_game = False
    game_over = False

    # Initial snake position
    snake_x = 45
    snake_y = 55

    # Initial movement
    velocity_x = 0
    velocity_y = 0

    # Snake settings
    snake_size = 30
    init_velocity = 5
    fps = 60

    # Initial score
    score = 0

    # Snake body list
    snk_list = []
    snk_length = 1

    # Create High Score file if it doesn't exist
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    # Read high score from file
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = int(f.read().strip() or 0)
    except ValueError:
        hiscore = 0

    # Generate first food position
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)

    # Main Game Loop
    while not exit_game:

        # Game Over Screen
        if game_over:

            # Save high score
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game Over!", red, 330, 220)
            text_screen("Press ENTER to Restart", black, 220, 290)

            pygame.display.update()

            for event in pygame.event.get():

                # Exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Restart game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True

        else:

            # Handle Keyboard Input
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    # Move Right
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    # Move Left
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    # Move Up
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    # Move Down
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat Key (adds 10 points)
                    elif event.key == pygame.K_q:
                        score += 10

            # Update snake position
            snake_x += velocity_x
            snake_y += velocity_y

            # Food Collision
            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:

                # Increase score
                score += 10

                # Generate new food position
                food_x = random.randint(20, screen_width - snake_size)
                food_y = random.randint(20, screen_height - snake_size)

                # Increase snake length
                snk_length += 5

                # Update high score
                if score > hiscore:
                    hiscore = score

            # Draw Background
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))

            # Display score
            text_screen(
                f"Score: {score}  Hiscore: {hiscore}",
                red,
                5,
                5,
            )

            # Draw food
            pygame.draw.rect(
                gameWindow,
                red,
                [food_x, food_y, snake_size, snake_size],
            )

            # Snake Body Management
            head = [snake_x, snake_y]
            snk_list.append(head)

            # Remove oldest block to maintain length
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Self Collision Detection
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            # Boundary Collision Detection
            if (
                snake_x < 0
                or snake_x > screen_width - snake_size
                or snake_y < 0
                or snake_y > screen_height - snake_size
            ):
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            # Draw snake
            plot_snake(gameWindow, black, snk_list, snake_size)

            # Update display
            pygame.display.update()

            # Control frame rate
            clock.tick(fps)


# Program Entry Point
# Starts the game by showing the welcome screen.
welcome()