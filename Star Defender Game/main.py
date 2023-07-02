import pygame
import random
import math
from pygame import mixer

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

# Background music
mixer.music.load('./Sounds/background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('./images/battleship.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('./images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
# When the bullet is in the
# Ready state - we can't see the bullet on the screen
# Fire state - we can see the bullet on the screen
bullet_state = "ready"

# game score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


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

        # check a keystroke is being pressed & whether its right or left arrow key
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
                    bullet_sound = mixer.Sound("./Sounds/laser.wav")
                    bullet_sound.play()
                    # Get the current X coordinates of the Spcaceship
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

    # Calling for the enemy function
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 600:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        # setup some boundaries for the enemy ship
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
            # enemyX[i] = 0
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
            # enemyX[i] = 736
        # enemy(enemyX[i], enemyY[i], i)

        # Collision
        collision = isCollision(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision:
            explosion_sound = mixer.Sound("./Sounds/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print("score: " + str(score))
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        # enemyX[i] = 736
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
