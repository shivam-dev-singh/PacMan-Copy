import pygame
from global_vars import *
from move_it1 import move_it

balls = []
for i in range(0,4):
	image_name = 'pac{}.png'.format(i)
	img = pygame.image.load(image_name)
	img.set_colorkey(black)
	img = pygame.transform.scale(img,(33,33))
	balls.append(img)

class Ball(pygame.sprite.Sprite):

	def __init__(self,x,y):
	    	pygame.sprite.Sprite.__init__(self)
		self.x_inc = 0
		self.y_inc = 0
		self.x_speed = b_unit
		self.y_speed = b_unit
		
		self.indx = 0
		self.frame_rate = 2
		self.frames = 1
		self.rot = 0
		#self.image = pygame.image.load("ball6.png")#.convert()
		self.image = balls[self.indx]
		
		#self.image = pygame.image.load("ball5.png")#.convert()
		#self.image = pygame.transform.scale(self.image,(33,33))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.last_key = None
		self.key_time = 0
		self.lifes = 3
		self.immune_t = 0
		self.score = -1
		#self.last_key_h = None
		#self.last_key_v = None
		all_sprites.add(self)
	

	def move(self,event):	
		#if event.type == pygame.KEYDOWN:
		#	move_it(self,event.key)
		self.key_time += -1
		if self.key_time == 0:
			self.last_key = None
			self.key_time = 100
		if event.type == pygame.KEYDOWN:
			self.last_key = event.key
			self.key_time = 14
			
		move_it(self,self.last_key)
		
	def update(self):
		global score
		
		self.rect.x += self.x_inc
		self.rect.y += self.y_inc
		if pygame.sprite.spritecollide(self,wall_sprites,False):
			self.rect.x += -self.x_inc
			self.rect.y += -self.y_inc
			self.x_inc = 0
			self.y_inc = 0
			self.last_key = None
		#print self.rect.x,self.rect.y
		if pygame.sprite.spritecollide(self,coin_sprites,True):
			boom_sound.play()
			self.score += 1
						
		collided_worms = pygame.sprite.spritecollide(self,wormhole_sprites,False)
		if (collided_worms):
			for worm in collided_worms:
				worm.reaction(self) 
		
		
		self.frames = (self.frames+1)%self.frame_rate
		if self.frames == 0:
			self.indx += 1
			self.indx = self.indx%4
			#print self.indx
		
		self.image = balls[self.indx]
		self.image = pygame.transform.rotate(self.image,self.rot)
		
		
	"""		
	def draw(self,gameDisplay):
		gameDisplay.blit(self.image,self.rect)
	"""
