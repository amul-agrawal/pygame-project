import pygame
pygame.init()

# create the screen
window_width_X=1600
window_width_Y=900
# Score

score_value_player = [0]*2
font = pygame.font.Font('freesansbold.ttf', 25)
textX = 10      #position of score of player 1
testY = 10      #position of score of player 1
text1X = 1300   #position of score of player 2
test1Y = 850    #position of score of player 2


# Caption and Icon
pygame.display.set_caption("River Battle")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)


# Player
pikachuImg = pygame.image.load('pikachu.png')
snorlaxImg = pygame.image.load('snorlax.png')
playerImg = pikachuImg
playerX = 720
playerY = 835
playerX_change = 0
playerY_change = 0


# rock obastacle
rockImg = pygame.image.load('rocks.png')
rockX = []
rockY = []
rockX.append(1500)
rockX.append(300)
rockX.append(250)
rockX.append(30)
rockY.append(4)
rockY.append(334)
rockY.append(664)
rockY.append(831)
num_of_rocks = 4

# bonfire obastacle
bonfireImg = pygame.image.load('bonfire.png')
bonfireX = []
bonfireY = []
bonfireX.append(1100)
bonfireX.append(50)
bonfireY.append(169)
bonfireY.append(499)
num_of_bonfires = 2

# volcano obastacle
volcanoImg = pygame.image.load('volcano.png')
volcanoX = []
volcanoY = []
volcanoX.append(1450)
volcanoY.append(499)
num_of_volcanoes = 1

# boat obastacle
boatImg = pygame.image.load('boat.png')
boatX = []
boatY = []
boatX.append(400)
boatX.append(1300)
boatX.append(800)
boatX.append(50)
boatX.append(400)
boatX.append(1100)
boatY.append(85)
boatY.append(85)
boatY.append(415)
boatY.append(415)
boatY.append(745)
boatY.append(745)
boatX_change = 2
num_of_boats = 6

# cruise obastacle
cruiseImg = pygame.image.load('cruise.png')
cruiseX = []
cruiseY = []
cruiseX.append(1300)
cruiseX.append(500)
cruiseX.append(1500)
cruiseX.append(900)
cruiseY.append(250)
cruiseY.append(250)
cruiseY.append(580)
cruiseY.append(580)
cruiseX_change = -2
num_of_cruises = 4


# cavewoman obastacle
cavewomanImg = pygame.image.load('cavewoman.png')
cavewomanX = []
cavewomanY = []
cavewomanX.append(300)
cavewomanX.append(900)
cavewomanY.append(170)
cavewomanY.append(500)
cavewomanX_change = []
cavewomanX_change.append(1)
cavewomanX_change.append(1)
cavewomanY_change = 0
num_of_cavewomen = 2


#rhino obastacle
rhinoImg = pygame.image.load('rhino.png')
rhinoX = []
rhinoY = []
rhinoX.append(1000)
rhinoX.append(800)
rhinoY.append(335)
rhinoY.append(664)
rhinoX_change = -1
rhinoY_change = 0
num_of_rhinos = 2
