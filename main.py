# GAME IMPORT AND CONFIG FILE
import pygame
from config import *

# GAME INTIALIZE HOGYI
pygame.init()

# GAME KA TITLE
pygame.display.set_caption("Dinesh ki Game")

# SCREEN KA SIZE
screen = pygame.display.set_mode((800, 600))

# FONT KA SIZE
font = pygame.font.Font(font_used, 64)
font2 = pygame.font.Font(font_used, 24)
font3 = pygame.font.Font(font_used, 64)
font4 = pygame.font.Font(font_used, 32)

# SPEED CHANGING FUNCTIONS


def speed():
    global boat1X_change
    global boat2X_change
    global boat3X_change
    global boat3aX_change
    global boat4X_change
    global boat5X_change

    boat1X_change += 0.3
    boat2X_change += 0.3
    boat3X_change += 0.3
    boat4X_change += 0.3
    boat5X_change += 0.3
    boat3aX_change += 0.3

# MERA PLAYER FUNCTION


def player(x, y):
    screen.blit(playerImg, (x, y))

# STARTING MESSAGE


def message():
    msg1 = font.render(text1, True, landcolor)
    screen.blit(msg1, (70, 200))
    msg = font.render(text2, True, (255, 255, 255))
    screen.blit(msg, (8, 300))

# CHANGES THE PLAYER


def reset():
    global count
    count += 1
    global playerX
    global playerY
    global playerImg
    if count % 2 == 1:
        playerX = 380
        playerY = 0
        playerImg = pygame.image.load('down.png')
        set0()
    if count % 2 == 0:
        playerX = 380
        playerY = 576
        playerImg = pygame.image.load('arrow.png')
        set0()

# SAARE OBSTACLES


def boat1(x, y):
    screen.blit(boatImage, (x, y))


def boat2(x, y):
    screen.blit(boati, (x, y))


def boat3(x, y):
    screen.blit(boatImage, (x, y))


def boat4(x, y):
    screen.blit(boati, (x, y))


def boat5(x, y):
    screen.blit(boatImage, (x, y))


def shark(x, y):
    screen.blit(sharkimg, (x, y))


def stone(x, y):
    screen.blit(stonei, (x, y))


def crab1(x, y):
    screen.blit(crabimg, (x, y))


def crab2(x, y):
    screen.blit(crabimg, (x, y))


def crab3(x, y):
    screen.blit(crabimg, (x, y))


def crab4(x, y):
    screen.blit(crabimg, (x, y))


def crab5(x, y):
    screen.blit(crabimg, (x, y))


def tree1(x, y):
    screen.blit(treeimg, (x, y))


def croc(x, y):
    screen.blit(crocimage, (x, y))


def tree2(x, y):
    screen.blit(treeimg, (x, y))

# STATIC COLLISION


def SCollision(playerX, playerY, SobstacleX, SobstacleY):
    if (SobstacleX <= playerX <= (SobstacleX+32) and SobstacleY <= playerY <= (SobstacleY + 32)):
        reset()
    elif (SobstacleX <= (playerX+24) <= (SobstacleX+32) and SobstacleY <= (playerY+24) <= (SobstacleY + 32)):
        reset()
    elif (SobstacleX <= (playerX+24) <= (SobstacleX+32) and SobstacleY <= (playerY) <= (SobstacleY + 32)):
        reset()
    elif (SobstacleX <= (playerX) <= (SobstacleX+32) and SobstacleY <= (playerY+24) <= (SobstacleY + 32)):
        reset()

# MOVING COLISSION


def MCollision(playerX, playerY, MobstacleX, MobstacleY):
    if (MobstacleX <= playerX <= (MobstacleX+64) and MobstacleY <= playerY <= (MobstacleY + 64)):
        reset()
    elif (MobstacleX <= (playerX+24) <= (MobstacleX+64) and MobstacleY <= (playerY+24) <= (MobstacleY + 64)):
        reset()
    elif (MobstacleX <= (playerX+24) <= (MobstacleX+64) and MobstacleY <= (playerY) <= (MobstacleY + 64)):
        reset()
    elif (MobstacleX <= (playerX) <= (MobstacleX+64) and MobstacleY <= (playerY+24) <= (MobstacleY + 64)):
        reset()

# SET ALL FLAGS T0 0


def set0():
    global player1_score
    global player2_score
    global surface_1_flag
    global water_1_flag
    global water_2_flag
    global water_3_flag
    global water_4_flag
    global water_5_flag
    global water_6_flag
    global surface_2_flag
    global surface_3_flag
    global surface_4_flag
    global surface_5_flag
    global surface_6_flag
    global surface_7_flag

    surface_1_flag = 0
    surface_2_flag = 0
    surface_3_flag = 0
    surface_4_flag = 0
    surface_5_flag = 0
    surface_6_flag = 0
    surface_7_flag = 0
    water_1_flag = 0
    water_2_flag = 0
    water_3_flag = 0
    water_4_flag = 0
    water_5_flag = 0
    water_6_flag = 0


# MOVE KARNE PE SCORE CHANGE
def scorep(playerY):
    global player1_score
    global player2_score
    global surface_1_flag
    global water_1_flag
    global water_2_flag
    global water_3_flag
    global water_4_flag
    global water_5_flag
    global water_6_flag
    global surface_2_flag
    global surface_3_flag
    global surface_4_flag
    global surface_5_flag
    global surface_6_flag
    global surface_7_flag
    global winp1
    global winp2

    if count % 2 == 0:
        if water_1_flag == 0:
            if playerY < 500:
                water_1_flag = 1
                player1_score += 10
        if surface_2_flag == 0:
            if playerY < 476:
                surface_2_flag = 1
                player1_score += 5
        if water_2_flag == 0:
            if playerY < 400:
                water_2_flag = 1
                player1_score += 10
        if water_3_flag == 0:
            if playerY < 300:
                water_3_flag = 1
                player1_score += 10
        if water_4_flag == 0:
            if playerY < 200:
                water_4_flag = 1
                player1_score += 10
        if water_5_flag == 0:
            if playerY < 100:
                water_5_flag = 1
                player1_score += 10
        if water_6_flag == 0:
            if playerY < 76:
                water_6_flag = 1
                player1_score += 10
        if surface_3_flag == 0:
            if playerY < 376:
                surface_3_flag = 1
                player1_score += 5
        if surface_4_flag == 0:
            if playerY < 276:
                surface_4_flag = 1
                player1_score += 5
        if surface_5_flag == 0:
            if playerY < 176:
                surface_5_flag = 1
                player1_score += 5
        if surface_6_flag == 0:
            if playerY < 76:
                surface_6_flag = 1
                player1_score += 5
        if surface_7_flag == 0:
            if playerY == 0:
                winp1 = 1
                reset()
    else:
        if water_1_flag == 0:
            if playerY > 52:
                water_1_flag = 1
                player2_score += 10
        if surface_2_flag == 0:
            if playerY > 76:
                surface_2_flag = 1
                player2_score += 5
        if water_2_flag == 0:
            if playerY > 152:
                water_2_flag = 1
                player2_score += 10
        if water_3_flag == 0:
            if playerY > 252:
                water_3_flag = 1
                player2_score += 10
        if water_4_flag == 0:
            if playerY > 352:
                water_4_flag = 1
                player2_score += 10
        if water_5_flag == 0:
            if playerY > 452:
                water_5_flag = 1
                player2_score += 10
        if water_6_flag == 0:
            if playerY > 552:
                water_6_flag = 1
                player2_score += 10
        if surface_3_flag == 0:
            if playerY > 176:
                surface_3_flag = 1
                player2_score += 5
        if surface_4_flag == 0:
            if playerY > 276:
                surface_4_flag = 1
                player2_score += 5
        if surface_5_flag == 0:
            if playerY > 376:
                surface_5_flag = 1
                player2_score += 5
        if surface_6_flag == 0:
            if playerY > 476:
                surface_6_flag = 1
                player2_score += 5
        if surface_7_flag == 0:
            if playerY == 576:
                winp2 = 1
                reset()


# WHILE LOOPS
running = False
press = True
while press:
    screen.blit(bgimg, (0, 0))
    for event in pygame.event.get():
        message()
        time = (int)((pygame.time.get_ticks()) / 1000)
        # key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
                press = False
        pygame.display.update()


# MAIN LOOP
while running:
    # BG COLOR
    screen.fill(watercolor)
    for event in pygame.event.get():
        # CROSS BUTTON
        if event.type == pygame.QUIT:
            running = False
        # KEY CONTROLS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    # CHANGES
    playerX += playerX_change
    playerY += playerY_change

    # BOUNDARIES
    if playerX <= 0:
        playerX = 0
    elif playerX >= 776:
        playerX = 776

    if playerY <= 0:
        playerY = 0
    elif playerY >= 576:
        playerY = 576

    # BOAT CHANGES
    boat1X += boat1X_change
    boat2X += boat2X_change
    boat3X += boat3X_change
    boat3aX += boat3aX_change
    boat4X += boat4X_change
    boat5X += boat5X_change

    if boat1X > 800:
        boat1X = 0
    if boat2X > 800:
        boat2X = 0
    if boat3X > 800:
        boat3X = 0
    if boat3aX > 800:
        boat3aX = 0
    if boat4X > 800:
        boat4X = 0
    if boat5X > 800:
        boat5X = 0

    # SHARK CHANGE
    sharkX += sharkX_change
    if sharkX <= 0:
        sharkX = 0
        sharkX_change = 1.5
    elif sharkX >= 736:
        sharkX = 736
        sharkX_change = -1.5

    # RECTANGLES DRAWN
    pygame.draw.rect(screen, landcolor, (0, 576, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 476, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 376, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 276, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 176, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 76, 800, 24), 0)
    pygame.draw.rect(screen, landcolor, (0, 0, 800, 24), 0)

    # STATIC COLLISSION
    SCollision(playerX, playerY, crab1X, crab1Y)
    SCollision(playerX, playerY, stone2X, stone2Y)
    SCollision(playerX, playerY, crab3X, crab3Y)
    SCollision(playerX, playerY, stone4X, stone4Y)
    SCollision(playerX, playerY, crab5X, crab5Y)
    SCollision(playerX, playerY, tree1X, tree1Y)
    SCollision(playerX, playerY, tree2X, tree2Y)

    # MOVING COLLISSION
    MCollision(playerX, playerY, boat1X, boat1Y)
    MCollision(playerX, playerY, boat2X, boat2Y)
    MCollision(playerX, playerY, boat3X, boat3Y)
    MCollision(playerX, playerY, boat4X, boat4Y)
    MCollision(playerX, playerY, boat5X, boat5Y)
    MCollision(playerX, playerY, boat3aX, boat3aY)
    SCollision(playerX, playerY, sharkX, sharkY)
    MCollision(playerX, playerY, crocX, crocY)

    # BOAT SHOWING
    boat1(boat1X, boat1Y)
    boat2(boat2X, boat2Y)
    boat3(boat3X, boat3Y)
    boat3(boat3aX, boat3aY)
    boat4(boat4X, boat4Y)
    boat5(boat5X, boat5Y)

    # SHARK MOVING
    shark(sharkX, sharkY)

    # SCORE DISPLAY
    scorep(playerY)

    # SCORE CHANGES WITH TIME
    if count == 0:
        t1p1 = (int)((pygame.time.get_ticks()) / 1000 - time)
    if count == 1:
        t1p2 = (int)((pygame.time.get_ticks())/1000 - t1p1)
    if count == 2:
        t2p1 = (int)((pygame.time.get_ticks())/1000 - t1p1 - t1p2)
    if count == 3:
        t2p2 = (int)((pygame.time.get_ticks())/1000 - t1p1 - t1p2 - t2p1)

    msg = font2.render(text3 +
                       str(player1_score - t1p1 - t2p1), True, (0, 0, 0))
    screen.blit(msg, (0, 0))

    msg = font2.render(text4 +
                       str(player2_score - t1p2 - t2p2), True, (0, 0, 0))
    screen.blit(msg, (575, 575))

    # START AUR END DISPLAY
    if count % 2 == 0:
        msg = font2.render(text5, True, (0, 0, 0))
        screen.blit(msg, (300, 575))
        msg = font2.render(text6, True, (0, 0, 0))
        screen.blit(msg, (380, 0))

    if count % 2 == 1:
        msg = font2.render(text6, True, (0, 0, 0))
        screen.blit(msg, (380, 575))
        msg = font2.render(text5, True, (0, 0, 0))
        screen.blit(msg, (300, 0))

    # SPEED CONTROL
    if count == 2:
        if speed_f1 == 0:
            speed_f1 = 1
            speed()
    if count == 4:
        if speed_f2 == 0:
            speed_f2 = 1
            speed()
    if count == 4:
        running = False
        press = True

    # STATIC OBSTACLE
    crab1(crab1X, crab1Y)
    stone(stone2X, stone2Y)
    crab3(crab3X, crab3Y)
    stone(stone4X, stone4Y)
    crab5(crab5X, crab5Y)
    tree1(tree1X, tree1Y)
    tree2(tree2X, tree2Y)
    croc(crocX, crocY)

    player(playerX, playerY)

    pygame.display.update()

while press:

    screen.fill((0, 119, 190))
    for event in pygame.event.get():

        # QUIT BUTTON
        if event.type == pygame.QUIT:
            press = False
        if player1_score >= player2_score:
            msg = font3.render(text7, True, (255, 255, 255))
            screen.blit(msg, (100, 250))
        elif player1_score == player2_score:
            msg = font3.render(text8, True, (255, 255, 255))
            screen.blit(msg, (100, 250))
        else:
            msg = font3.render(text9, True, (255, 255, 255))
            screen.blit(msg, (100, 250))

        pygame.display.update()
