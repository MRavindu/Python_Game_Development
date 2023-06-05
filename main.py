import pygame

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Star Defender")
icon = pygame.image.load('./images/project.png')
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen colors
    screen.fill((128, 128, 128))
    pygame.display.update()