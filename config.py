import pygame

# FONT USED
font_used = 'freesansbold.ttf'

# SAARI IMAGES USED
playerImg = pygame.image.load('arrow.png')
boatImage = pygame.image.load('ship.png')
sharkimg = pygame.image.load('shark.png')
crabimg = pygame.image.load('crab.png')
boati = pygame.image.load('45.png')
stonei = pygame.image.load('wellness.png')
treeimg = pygame.image.load('tree.png')
bgimg = pygame.image.load('bg.jpg')
crocimage = pygame.image.load('croc.png')


# TEXT
text1 = "CROSS THE RIVER"
text2 = "PRESS SPACE TO START"
text3 = "Player1_Score: "
text4 = "Player2_Score: "
text5 = "START"
text6 = "END"
text7 = "PLAYER 1 WINS"
text8 = "GAME TIED"
text9 = "PLAYER 2 WINS"
# SAARE COLORS USED
landcolor = (249, 209, 153)
watercolor = (0, 119, 190)
woodcolor = (193, 154, 107)


# COUNT OF ROUND
count = 0

t1p1 = 0
t1p2 = 0
t2p1 = 0
t2p2 = 0

time = 0

playerX = 380
playerY = 576
playerX_change = 0
playerY_change = 0

# staring of boat and change
boat1X = 700
boat1Y = 505
boat1X_change = 0.5
boat1Y_change = 0

boat2X = 400
boat2Y = 405
boat2X_change = 0.5
boat2Y_change = 0

boat3X = 600
boat3Y = 305
boat3X_change = 0.5
boat3Y_change = 0

boat3aX = 200
boat3aY = 305
boat3aX_change = 0.5
boat3aY_change = 0


boat4X = 300
boat4Y = 205
boat4X_change = 0.5
boat4Y_change = 0

boat5X = 500
boat5Y = 105
boat5X_change = 0.5
boat5Y_change = 0

sharkX = 100
sharkY = 30
sharkX_change = 1.5
sharkY_change = 0

crab1X = 200
crab1Y = 470

stone2X = 700
stone2Y = 370

crab3X = 400
crab3Y = 270

stone4X = 100
stone4Y = 170

crab5X = 600
crab5Y = 70

tree1X = 20
tree1Y = 70

tree2X = 600
tree2Y = 470

crocX = 20
crocY = 350

speed_f1 = 0
speed_f2 = 0

winp1 = 0
winp2 = 0


player1_score = 0
player2_score = 0

game_mode = False

# player ka logo


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
