import pygame

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Star Defender")
icon = pygame.image.load('./images/project.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:

    # Screen colors
    screen.fill((128, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check a key stroke is been pressed & wehter its right or left arrow key
        if event.type == pygame.KEYDOWN:
            print("Keystroke is been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
                print("Left arrow is been pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
                print("Right arrow is been pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("arrow key is been released")




    # Calling for the player function
    playerX += playerX_change
    player(playerX, playerY)

    pygame.display.update()