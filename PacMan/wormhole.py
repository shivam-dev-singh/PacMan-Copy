import pygame
from global_vars import *

class Wormhole(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h,new_x,new_y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w,h))
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.new_x = new_x
		self.new_y = new_y
		all_sprites.add(self)
		wormhole_sprites.add(self)
		
	def reaction(self,obj):
		obj.rect.x = self.new_x
		obj.rect.y = self.new_y
		
	def update(self):
		pass
