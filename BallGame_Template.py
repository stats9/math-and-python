# Import pygame module
import pygame

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Ball Drop Game")

# Define a ball class
class Ball:
    # Constructor
    def __init__(self, x, y, radius, color):
        # Set the initial position, radius and color of the ball
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        # Set the initial speed and acceleration of the ball
        self.speed = 0
        self.acceleration = 0.5

    # Draw the ball on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # Update the position and speed of the ball
    def update(self):
        # Increase the speed by the acceleration
        self.speed += self.acceleration
        # Move the ball by the speed
        self.y += self.speed
        # Check if the ball hits the bottom of the screen
        if self.y + self.radius > SCREEN_HEIGHT:
            # Bounce the ball back
            self.y = SCREEN_HEIGHT - self.radius
            self.speed = -self.speed * 0.8

# Define a basket class
class Basket:
    # Constructor
    def __init__(self, x, y, width, height, color):
        # Set the initial position, size and color of the basket
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        # Set the initial speed and direction of the basket
        self.speed = 5
        self.direction = 1

    # Draw the basket on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    # Update the position and direction of the basket
    def update(self):
        # Move the basket by the speed and direction
        self.x += self.speed * self.direction
        # Check if the basket hits the left or right edge of the screen
        if self.x < 0 or self.x + self.width > SCREEN_WIDTH:
            # Change the direction of the basket
            self.direction = -self.direction

# Create a ball object
ball = Ball(SCREEN_WIDTH // 2, 0, 20, RED)

# Create a basket object
basket = Basket(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, 50, GREEN)

# Define the score and the font
score = 0
font = pygame.font.SysFont("Arial", 32)

# Define a flag for the game loop
running = True

# Start the game loop
while running:
    # Handle the events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game loop
        if event.type == pygame.QUIT:
            running = False
        # If the user presses a key
        if event.type == pygame.KEYDOWN:
            # If the user presses the space key
            if event.key == pygame.K_SPACE:
                # Reset the ball to the top of the screen
                ball.x = SCREEN_WIDTH // 2
                ball.y = 0
                ball.speed = 0

    # Update the game logic
    # Update the ball
    ball.update()
    # Update the basket
    basket.update()
    # Check if the ball is inside the basket
    if ball.x > basket.x and ball.x < basket.x + basket.width and ball.y + ball.radius > basket.y:
        # Increase the score by one
        score += 1
        # Reset the ball to the top of the screen
        ball.x = SCREEN_WIDTH // 2
        ball.y = 0
        ball.speed = 0
    # Check if the ball is below the basket
    elif ball.y + ball.radius > basket.y + basket.height:
        # Decrease the score by one
        score -= 1
        # Reset the ball to the top of the screen
        ball.x = SCREEN_WIDTH // 2
        ball.y = 0
        ball.speed = 0

    # Draw the game graphics
    # Fill the screen with black
    screen.fill(BLACK)
    # Draw the ball
    ball.draw(screen)
    # Draw the basket
    basket.draw(screen)
    # Draw the score
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
