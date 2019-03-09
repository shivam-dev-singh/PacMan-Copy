import pygame
from global_vars import *
import global_vars
import random
from player_ball1 import Ball
from move_it1 import move_it

class Enemy(Ball):
	def __init__(self,x,y,immage):
		Ball.__init__(self,x,y)
		#self.image = pygame.image.load('ball6.png')
		self.immage = immage
		self.image = pygame.image.load(immage)
		self.image.set_colorkey(white)
		self.image = pygame.transform.scale(self.image,(33,33))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.timme = 0
		self.try_dir = None
		
		#decision time 
		self.rndm = random.randrange(4,8)
		
		#self.x_speed = random.randrange(b_unit/2,b_unit-2)
		#self.y_speed = random.randrange(b_unit/2,b_unit-2)
		self.x_speed = int(b_unit*0.5)
		self.y_speed = int(b_unit*0.5)
		
		enemy_sprites.add(self)
		
	def move(self):
	
		self.timme = (self.timme + 1)%self.rndm
		if self.timme == 0:
			
			x_move = 3
			if (global_vars.player_x - self.rect.x) < 0:
				x_move = 2
			y_move = 1
			if(global_vars.player_y - self.rect.y)<0:
				y_move = 0
			
			i = random.choice([x_move,y_move])
			self.try_dir = directns[i]
			move_it(self,self.try_dir)
			#print player_x,player_y,"\t",global_vars.player_x,global_vars.player_y 

	def update(self):
		self.move()
		
		self.rect.x += self.x_inc
		self.rect.y += self.y_inc
		if pygame.sprite.spritecollide(self,wall_sprites,False):
			self.rect.x += -self.x_inc
			self.rect.y += -self.y_inc
			self.x_inc = 0
			self.y_inc = 0
		#print self.rect.x,self.rect.y
		#if pygame.sprite.spritecollide(self,coin_sprites,True):
		#	boom_sound.play()
			
		collided_worms = pygame.sprite.spritecollide(self,wormhole_sprites,False)
		if (collided_worms):
			for worm in collided_worms:
				worm.reaction(self)
		

