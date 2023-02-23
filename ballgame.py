import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_pos = [400, 300]
ball_radius = 20
ball_color = (255, 0, 0)
ball_speed = [5, 5]

# Set up the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls
    if ball_pos[0] + ball_radius > 800 or ball_pos[0] - ball_radius < 0:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] + ball_radius > 600 or ball_pos[1] - ball_radius < 0:
        ball_speed[1] = -ball_speed[1]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()

