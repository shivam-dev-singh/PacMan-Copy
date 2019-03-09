import pygame
from global_vars import *

class Wall(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h,color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w,h))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		pygame.draw.rect(self.image,color,self.rect)
		all_sprites.add(self)
		wall_sprites.add(self)
		
	def update(self):
		pass	
