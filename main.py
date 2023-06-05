import pygame
import random
import math

# Initialize the Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Star Defender")
icon = pygame.image.load('./images/project.png')
pygame.display.set_icon(icon)

# Background image
background = pygame.image.load('./images/bgimage3.jpg')

# Player
playerImg = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('./images/battleship.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.4
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('./images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
# When the bullet is in the
# Ready state - we can't see the bullet on the screen
# Fire state - we can see the bullet on the screen
bullet_state = "ready"

# game score
score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, bulletX, enemyY, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:

    # Screen colors
    screen.fill((128, 128, 128))
    # Background image added
    screen.blit(background, (0, 0))

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

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
                    print("Right arrow is been pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("arrow key is been released")

    # Calling for the player function
    playerX += playerX_change
    # setup some boundaries for the spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)

    # Calling for the enemy function
    enemyX += enemyX_change
    # setup some boundaries for the enemy ship
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
        enemyX = 0
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
        enemyX = 736
    enemy(enemyX, enemyY)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, bulletX, enemyY, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print("score: " + str(score))

    pygame.display.update()
