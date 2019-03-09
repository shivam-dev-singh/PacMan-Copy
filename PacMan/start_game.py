import pygame
import time
import random
from global_vars import *
import global_vars
from player_ball1 import Ball
from map13 import map1
from put_coin import put_coin
from enemy3 import Enemy
from score_it import score_display
from exit_menu import exit_menu
#from wall import Wall
#from move_it import move_it


pygame.init()
gameDisplay = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()


def check_enemy_collision(ball):
	if ball.immune_t > 0:
		ball.immune_t += -1
		
	if ball.immune_t == 0:
		enemies = pygame.sprite.spritecollide(ball,enemy_sprites,True)
		for enemmy in enemies:
			ball.x_inc = 0
			ball.y_inc = 0
			crash_sound.play()
			time.sleep(2)
			j = random.randrange(0,9)
			i = random.randrange(0,10) 
			#print "death = i :",(enemmy.rect.y-y00-e-2)/box_w,"j :",(enemmy.rect.x-x00-e-2)/box_w
			#print "birth = i :",i,"j :",j
		
			
			if (i == 4 and ( j == 0 or j == 1 or j == 8 or j == 9)) or (i == 6 and ( j == 0 or j == 1 or j == 8 or j == 9)) or   (i == 5 and ( j == 4 or j == 5)) or (i == 1 and (j == 1 or j == 3 or j == 6 or j == 8)):
				i += 1
			#ghost = Enemy(x00+e+2+j*box_w,y00+e+2+i*box_w)	
			ghost = Enemy(x00+e+2+j*box_w,y00+e+2+i*box_w,enemmy.immage)
			#for enemyy in enemies:
			#	ghost = Enemy(x00+e+2+j*box_w,y00+e+2+i*box_w,enemyy.color)
		
		if enemies :
			ball.lifes += -1
			ball.immune_t = 40
			if(ball.lifes == 0):
				time.sleep(2)
				pygame.quit()
				quit()
		
def gameLoop():
	#player_x
	#player_y
	
	map1(gameDisplay)
	put_coin()
	ball = Ball(x00+e+2,y00+e+2)	
	
	#if enemy is imported from enemy1
	ghost1 = Enemy(x00+e+2+9*box_w,y00+e+2,'images3.jpeg')
	ghost2 = Enemy(x00+e+2+9*box_w,y00+e+2+10*box_w,'images4.png')
	ghost3 = Enemy(x00+e+2,y00+e+2+10*box_w,'images6.png')
	
	#if enemy is imported from enemy 
	#ghost1 = Enemy(x00+e+2+9*box_w,y00+e+2,l_green)
	#ghost2 = Enemy(x00+e+2+9*box_w,y00+e+2+10*box_w,l_red)
	#ghost3 = Enemy(x00+e+2,y00+e+2+10*box_w,white)	
		
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
				
					#pygame.quit()
					#quit()
					exit_menu(gameDisplay)
					time.sleep(1)
				
				#else :
				#	ball.move(event.key)	
		
			#elif event.type == pygame.KEYUP:
			#	ball.move(event.key)
		
		ball.move(event)
		
		global_vars.player_x = (ball.rect.x )
		global_vars.player_y = (ball.rect.y )
		
		all_sprites.update()
			
		gameDisplay.fill(bg_color)
		
		score_display(gameDisplay,ball.score,ball.lifes)
		all_sprites.draw(gameDisplay)
		pygame.display.update()
	
		check_enemy_collision(ball)
									
		clock.tick(30)
	
gameLoop()
pygame.quit()
quit()
	
