import pygame
from global_vars import *

class Coin(pygame.sprite.Sprite):
	def __init__(self,x,y,r,color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((box_w-2*e,box_w-2*e))
		#self.image.fill(yellow)
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y 
		self.rad = r
		pygame.draw.circle(self.image,color,((box_w-2*e)/2,(box_w-2*e)/2),r)
		all_sprites.add(self)
		coin_sprites.add(self)
	
	def update(self):
		#pygame.sprite.groupcollide(self,wall_sprites,True,False)
		pass
