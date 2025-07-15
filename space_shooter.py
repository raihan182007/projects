import pygame
import random
import math

pygame.init()

#screen:
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space shooter")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player:
player_img = pygame.image.load("spaceship.png")
playerX = 360
playerY = 500
playerX_change = 0

#enemy:
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

def create_enemies():
    for i in range(num_of_enemy):
        enemy_img.append(pygame.image.load("enemy.png"))
        enemyX.append(random.randint(0,736))
        enemyY.append(random.randint(50,150))
        enemyX_change.append(3)
        enemyY_change.append(50)
create_enemies()

#bullet:
bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 500
bulletY_change = 5
bullet_stage = "ready"

background = pygame.image.load("bg.png")

font = pygame.font.Font(None,32)

over_font = pygame.font.Font(None,70)

def game_over_text():
    text = over_font.render("GAME OVER!",True,(255,255,255))
    screen.blit(text,(260,240))
    again_text = font.render("Press enter to restart",True,(255,255,255))
    screen.blit(again_text,(300,300))

def show_score():
    score = font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(10,10))

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_stage
    bullet_stage = "fire"
    screen.blit(bullet_img,(x+16,y))

def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance < 32:
        return True
    else:
        return False

score_value = 0


running = True
game_over = False

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5

            if event.key == pygame.K_SPACE and bullet_stage == "ready":
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
                
            if event.key == pygame.K_RETURN and game_over:
                # Reset Game
                game_over = False
                score_value = 0
                playerX = 360
                bulletY = 500
                bullet_stage = "ready"
                enemy_img.clear()
                enemyX.clear()
                enemyY.clear()
                enemyX_change.clear()
                enemyY_change.clear()
                create_enemies()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0           

    #player_movement:
    playerX += playerX_change
    if playerX <= 0:
        playerX = 735
    if playerX >= 736:
        playerX = 0

    if not game_over:   
        for i in range(num_of_enemy):
            if enemyY[i] >= 450:
                game_over = True
                for j in range(num_of_enemy):
                    enemyY[j] = 2000
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                if score_value <= 15:
                    enemyX_change[i] = 3
                elif score_value <= 30:
                    enemyX_change[i] = 5
                else:
                    enemyX_change[i] = 8

                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -3
                enemyY[i] += enemyY_change[i] 

            collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                score_value += 1
                bulletY = 500
                bullet_stage = "ready"
                enemyX[i] = random.randint(0,736)
                enemyY[i] = random.randint(50,150)

            enemy(enemyX[i],enemyY[i],i)
    
    if bullet_stage == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = 500
            bullet_stage = "ready"  

    show_score()
    player(playerX,playerY)
    if game_over:
        game_over_text()
    pygame.display.update()
    