import pygame
pygame.init()            # importing modules
pygame.font.init()
from random import randint
import time
from threading import Thread

# variables for the game

score=0
score_increment=80
ships=5
screen_width=800
screen_height=800
black,white=(0,0,0),(255,255,255)
shoot_bullet=False
bullet_y_pos=-46
bullet_y_vel=-20
clock=pygame.time.Clock()
game=True

img1=pygame.image.load(r"blastar1.png")
enemy=pygame.image.load(r"enemy.PNG")
ship=pygame.image.load(r"ship.PNG")
bullet=pygame.image.load(r"bullet.PNG")

 #font for score
Font=pygame.font.SysFont("comicsans",30)
Game_Font_score=Font.render(f"Score : {score}",True,white)
Game_Font_ship=Font.render(f"Ships : {ships}",True,white)

enemy_width=enemy.get_width()
ship_width=ship.get_width()
bullet_width=bullet.get_width()
enemy_height=enemy.get_height()
ship_height=ship.get_height()
bullet_height=bullet.get_height()


x_pos=randint(100,600)
y_pos=randint(100,600)
x_speed,y_speed=0,0


# displaying screen
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Blastar")
pygame.display.set_icon(img1)




#enemy1 for ship
enemy_x_pos=randint(100,600)
enemy_y_pos=randint(100,600)
enemy_xvel,enemy_yvel=20,0

#enemy2 for ship
enemy2_x_pos=randint(100,600)
enemy2_y_pos=randint(100,600)
enemy2_xvel=-20


def f():  # function to display game over
    while 1:
        global ships,game
        if (abs(x_pos-enemy2_x_pos)<=enemy_width and abs(y_pos-enemy2_y_pos)<=ship_height) or (abs(x_pos-enemy_x_pos)<=enemy_width and abs(y_pos-enemy_y_pos)<=ship_height): 
            ships-=1
            Game_Font_ship=Font.render(f"Ships : {ships}",True,white)
            time.sleep(0.6) 

            if ships==0:
                global game
                game=False
                Game_Font=Font.render(f"Game Over",True,white)
                screen.blit(Game_Font,(375,375))

t1=Thread(target=f)
t1.start()

while ships>=0:
    # filling screen with white colour
    screen.fill(black)
  
    
 
    # making controls to move the ship and fire
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ships=-1

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x_speed=-10
                y_speed=0
                
            if event.key == pygame.K_RIGHT:
                y_speed=0
                x_speed=10
                
            if event.key == pygame.K_UP:
                x_speed=0
                y_speed=-10
            

            if event.key == pygame.K_DOWN:
                x_speed=0
                y_speed=10
                
                
            if event.key==pygame.K_SPACE:
                
                if not shoot_bullet:
                    shoot_bullet=True
                    bullet_x_pos=x_pos
                    bullet_y_pos=y_pos

    if game:
        screen.blit(ship,(x_pos,y_pos))
        screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
        screen.blit(enemy,(enemy2_x_pos,enemy2_y_pos))
    
        x_pos+=x_speed
        y_pos+=y_speed 
        enemy_x_pos+=enemy_xvel
        enemy2_x_pos+=enemy2_xvel

        if x_pos>=screen_width-ship.get_width():
            x_pos=screen_width-ship.get_width()
        elif x_pos<=0:
            x_pos=0
        if y_pos>=screen_height-ship.get_height():
            y_pos=screen_height-ship.get_height()
        elif y_pos<=0:
            y_pos=0

        if enemy_x_pos>=screen_width:
            enemy_x_pos=0
        elif enemy2_x_pos<=-ship.get_width():
            enemy2_x_pos=screen_width

        if shoot_bullet:
            if bullet_y_pos<-bullet.get_width():
                shoot_bullet=False
            if abs(bullet_x_pos-enemy2_x_pos)<=enemy_width and abs(bullet_y_pos-enemy2_y_pos)<=enemy_height or abs(bullet_x_pos-enemy_x_pos)<=enemy_width and abs(bullet_y_pos-enemy_y_pos)<=enemy_height:
                score+=score_increment
                shoot_bullet=False
                Game_Font_score=Font.render(f"Score : {score}",True,white)
                
            screen.blit(bullet,(bullet_x_pos,bullet_y_pos))
            bullet_y_pos+=bullet_y_vel

        screen.blit(Game_Font_ship,(150,150))
        screen.blit(Game_Font_score,(600,150))
        clock.tick(20)
        pygame.display.update()

pygame.quit()
