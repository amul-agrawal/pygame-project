import pygame

# initialize pygame
pygame.init()

# importing math to check distance
import math
from config import *

# Set the screen size
screen = pygame.display.set_mode((window_width_X, window_width_Y))


# ---------------------------------------------------------------------------------------
# function that shows score on coordinate (x,y)
# ---------------------------------------------------------------------------------------
def show_score(Score, x, y):
    if y > 100:
        score = font.render("Player2 Score : " + str(Score), True, (0, 0, 0))
    else:
        score = font.render("Player1 Score : " + str(Score), True, (0, 0, 0))
    screen.blit(score, (x, y))


# ---------------------------------------------------------------------------------------
# function to show text
# ---------------------------------------------------------------------------------------
def show(name, x, y):
    screen.blit(name, (x, y))


# ---------------------------------------------------------------------------------------
# function to check collision
# ---------------------------------------------------------------------------------------
def isCollision(playerX, playerY, obstacleX, obstacleY):
    distance = math.sqrt(math.pow(playerX - obstacleX, 2) + (math.pow(playerY - obstacleY, 2)))
    if distance < 45:
        return True
    else:
        return False


running = True
turn = 0
flag = [False] * 12
flag1 = [False] * 12
prev_Time = pygame.time.get_ticks()
speedFlag = 0
call = 0


# ---------------------------------------------------------------------------------------
# creates a black window which in necessary for the trasitons in the game
# ---------------------------------------------------------------------------------------
def window():
    global running
    global playerX_change
    global playerY_change
    global boatX_change
    global cruiseX_change
    global cavewomanX_change
    global rhinoX_change
    global call
    global speedFlag
    # call variable keeps a track of how many times the funtion has been called
    call = call + 1
    font1 = pygame.font.Font('freesansbold.ttf', 50)
    score = ""
    player1score = ""
    player2Score = ""
    if call == 1:
        score = font1.render("WELCOME press ENTER to continue", True, (255, 255, 255))
    elif call == 2:
        score = font1.render("  PLAYER 2 TURN   press ENTER  ", True, (255, 255, 255))
    elif call == 3:
        score = font1.render("      ROUND 2    press ENTER   ", True, (255, 255, 255))
        player1score = font1.render("Player1 Score: " + str(score_value_player[0]), True, (255, 255, 255))
        player2Score = font1.render("Player2 Score: " + str(score_value_player[1]), True, (255, 255, 255))
        if score_value_player[0] > score_value_player[1]:
            # speedflag goes 1 if player1 wins the game
            speedFlag = 1
        if score_value_player[0] < score_value_player[1]:
            # speedflag goes 2 if player2 wins the game
            speedFlag = 2
    elif call == 4:
        score = font1.render("  PLAYER 2 TURN   press ENTER  ", True, (255, 255, 255))
    elif call == 5:
        if score_value_player[0] > score_value_player[1]:
            score = font1.render("PLAYER 1 WINS  press ENTER to exit", True, (255, 255, 255))
        elif score_value_player[0] == score_value_player[1]:
            score = font1.render("  TIE  press enter to exit ", True, (255, 255, 255))
        else:
            score = font1.render("PLAYER 2 WINS press ENTER to exit", True, (255, 255, 255))
    while running:
        screen.fill((0, 0, 0))
        if call == 3:
            screen.blit(score, (250, 300))
            screen.blit(player1score, (350, 400))
            screen.blit(player2Score, (350, 500))
        else:
            screen.blit(score, (350, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                call = 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    running = False
                if event.key == pygame.K_RETURN:
                    running = False
        pygame.display.update()
    running = True
    boatX_change = 2
    cruiseX_change = -2
    cavewomanX_change = []
    cavewomanX_change.append(1)
    cavewomanX_change.append(1)
    rhinoX_change = -1
    if call == 5:
        running = False
    #
    if call == 3 and speedFlag == 1:
        boatX_change = 3
        cruiseX_change = -3
        cavewomanX_change = []
        cavewomanX_change.append(1.5)
        cavewomanX_change.append(1.5)
        rhinoX_change = -1.5
    if call == 4 and speedFlag == 2:
        boatX_change = 3
        cruiseX_change = -3
        cavewomanX_change = []
        cavewomanX_change.append(1.5)
        cavewomanX_change.append(1.5)
        rhinoX_change = -1.5
    playerY_change = 0
    playerX_change = 0


# calling window function to welcome player to play the game
window()
while running:
    # ---------------------------------------------------------------------------------------
    #    SETUP THE GAME WINDOW AND PLAYER MOVEMENTS
    # ---------------------------------------------------------------------------------------
    screen.fill((77, 184, 255))
    pygame.draw.rect(screen, (64, 255, 0), (0, 0, 1600, 75))
    pygame.draw.rect(screen, (64, 255, 0), (0, 165, 1600, 75))
    pygame.draw.rect(screen, (64, 255, 0), (0, 330, 1600, 75))
    pygame.draw.rect(screen, (64, 255, 0), (0, 495, 1600, 75))
    pygame.draw.rect(screen, (64, 255, 0), (0, 660, 1600, 75))
    pygame.draw.rect(screen, (64, 255, 0), (0, 825, 1600, 75))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ---------------------------------------------------------------------------------------
        #       changing player position on the basis of arrow key pressed
        # ---------------------------------------------------------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    playerY += playerY_change
    playerX += playerX_change
    # ---------------------------------------------------------------------------------------
    #   checking the player bound
    # ---------------------------------------------------------------------------------------
    if playerX <= 0:
        playerX = 1536
    elif playerX >= 1536:
        playerX = 0
    if playerY <= 0:
        playerY = 0
    elif playerY >= 836:
        playerY = 836
    # ---------------------------------------------------------------------------------------
    #   displaying all the obstacles in every frame based on their updated position
    # ---------------------------------------------------------------------------------------
    show(playerImg, playerX, playerY)
    for i in range(num_of_cruises):
        cruiseX[i] += cruiseX_change
        if cruiseX[i] <= 0:
            cruiseX[i] = 1536
        elif cruiseX[i] >= 1536:
            cruiseX[i] = 0
        show(cruiseImg, cruiseX[i], cruiseY[i])
    for i in range(num_of_boats):
        boatX[i] += boatX_change
        if boatX[i] <= 0:
            boatX[i] = 1536
        elif boatX[i] >= 1536:
            boatX[i] = 0
        show(boatImg, boatX[i], boatY[i])
    for i in range(num_of_rocks):
        show(rockImg, rockX[i], rockY[i])
    for i in range(num_of_bonfires):
        show(bonfireImg, bonfireX[i], bonfireY[i])
    for i in range(num_of_volcanoes):
        show(volcanoImg, volcanoX[i], volcanoY[i])
    for i in range(num_of_cavewomen):
        cavewomanX[i] += cavewomanX_change[i]
    if cavewomanX[0] <= 0:
        cavewomanX[0] = 0
        cavewomanX_change[0] = 1.5
    elif cavewomanX[0] >= 600:
        cavewomanX[0] = 600
        cavewomanX_change[0] = -1.5
    if cavewomanX[1] <= 550:
        cavewomanX[1] = 550
        cavewomanX_change[1] = 1.5
    elif cavewomanX[1] >= 1200:
        cavewomanX[1] = 1200
        cavewomanX_change[1] = -1.5
    for i in range(num_of_cavewomen):
        show(cavewomanImg, cavewomanX[i], cavewomanY[i])
    for i in range(num_of_rhinos):
        rhinoX[i] += rhinoX_change
    if rhinoX[0] <= 700:
        rhinoX[0] = 700
        rhinoX_change = 1.5
    elif rhinoX[0] >= 1300:
        rhinoX[0] = 1300
        rhinoX_change = -1.5
    if rhinoX[1] <= 500:
        rhinoX[1] = 500
        rhinoX_change = 1.5
    elif rhinoX[1] >= 1100:
        rhinoX[1] = 1100
        rhinoX_change = -1.5
    for i in range(num_of_rhinos):
        show(rhinoImg, rhinoX[i], rhinoY[i])
    # ---------------------------------------------------------------------------------------
    #   collision detection
    # ---------------------------------------------------------------------------------------
    collision = False
    for i in range(num_of_cruises):
        if (collision):
            break
        collision = isCollision(playerX, playerY, cruiseX[i], cruiseY[i])
    for i in range(num_of_boats):
        if collision:
            break
        collision = isCollision(playerX, playerY, boatX[i], boatY[i])
    for i in range(num_of_cavewomen):
        if collision:
            break
        collision = isCollision(playerX, playerY, cavewomanX[i], cavewomanY[i])
    for i in range(num_of_rhinos):
        if collision:
            break
        collision = isCollision(playerX, playerY, rhinoX[i], rhinoY[i])
    for i in range(num_of_rocks):
        if collision:
            break
        collision = isCollision(playerX, playerY, rockX[i], rockY[i])
    for i in range(num_of_volcanoes):
        if collision:
            break
        collision = isCollision(playerX, playerY, volcanoX[i], volcanoY[i])
    for i in range(num_of_bonfires):
        if collision:
            break
        collision = isCollision(playerX, playerY, bonfireX[i], bonfireY[i])
    if collision:
        playerX = 720
        if turn == 0:
            playerY = 5
            turn = 1
            playerImg = snorlaxImg
        elif turn == 1:
            playerY = 835
            turn = 0
            playerImg = pikachuImg
        window()
    # ---------------------------------------------------------------------------------------
    # updating player score based on his position on the screen and time spent playing the game
    # ---------------------------------------------------------------------------------------
    if turn == 0:
        flag1 = [False] * 12
        if playerY < 761:
            if not flag[0]:
                score_value_player[0] += 5
                flag[0] = True
        if playerY < 671:
            if flag[1] is False:
                score_value_player[0] += 20
                flag[1] = True
        if playerY < 596:
            if flag[2] is False:
                score_value_player[0] += 15
                flag[2] = True
        if playerY < 506:
            if flag[3] is False:
                score_value_player[0] += 20
                flag[3] = True
        if playerY < 431:
            if flag[4] is False:
                score_value_player[0] += 20
                flag[4] = True
        if playerY < 341:
            if flag[5] is False:
                score_value_player[0] += 20
                flag[5] = True
        if playerY < 266:
            if flag[6] is False:
                score_value_player[0] += 15
                flag[6] = True
        if playerY < 176:
            if flag[7] is False:
                score_value_player[0] += 20
                flag[7] = True
        if playerY < 101:
            if flag[8] is False:
                score_value_player[0] += 15
                flag[8] = True
        if playerY < 11:
            if flag[9] is False:
                score_value_player[0] += 20
                flag[9] = True
                playerX = 720
                playerY = 5
                turn = 1
                playerImg = snorlaxImg
                window()
        cur_Time = pygame.time.get_ticks()
        if cur_Time - prev_Time >= 2000:
            score_value_player[0] -= 1
            prev_Time = cur_Time
    else:
        flag = [False] * 12
        if playerY > 75:
            if flag1[0] is False:
                score_value_player[1] += 5
                flag1[0] = True
        if playerY > 165:
            if flag1[1] is False:
                score_value_player[1] += 20
                flag1[1] = True
        if playerY > 240:
            if flag1[2] is False:
                score_value_player[1] += 15
                flag1[2] = True
        if playerY > 330:
            if flag1[3] is False:
                score_value_player[1] += 20
                flag1[3] = True
        if playerY > 405:
            if flag1[4] is False:
                score_value_player[1] += 15
                flag1[4] = True
        if playerY > 495:
            if flag1[5] is False:
                score_value_player[1] += 20
                flag1[5] = True
        if playerY > 570:
            if flag1[6] is False:
                score_value_player[1] += 20
                flag1[6] = True
        if playerY > 660:
            if flag1[7] is False:
                score_value_player[1] += 20
                flag1[7] = True
        if playerY > 735:
            if flag1[8] is False:
                score_value_player[1] += 15
                flag1[8] = True
        if playerY > 825:
            if flag1[9] is False:
                score_value_player[1] += 20
                flag1[9] = True
                playerX = 720
                playerY = 835
                turn = 0
                playerImg = pikachuImg
                window()
        cur_Time = pygame.time.get_ticks()
        if cur_Time - prev_Time >= 2000:
            score_value_player[1] -= 1
            prev_Time = cur_Time
    show_score(score_value_player[0], textX, testY)
    show_score(score_value_player[1], text1X, test1Y)
    pygame.display.update()
