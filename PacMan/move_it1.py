import pygame
from global_vars import *

def move_it(self,key):
	
	old_x = self.rect.x
	old_y = self.rect.y
	
	if key == pygame.K_UP:
		
		self.rect.y += -self.y_speed
		if not pygame.sprite.spritecollide(self,wall_sprites,False):
			self.y_inc = -self.y_speed
			self.x_inc = 0
			self.rot = 90
			
	elif key == pygame.K_DOWN:
		
		self.rect.y += self.y_speed
		if not pygame.sprite.spritecollide(self,wall_sprites,False):
			self.y_inc = self.y_speed
			self.x_inc = 0
			self.rot = -90
		
	elif key == pygame.K_LEFT:
		
		self.rect.x += -self.x_speed
		if not pygame.sprite.spritecollide(self,wall_sprites,False):
			self.x_inc = -self.x_speed
			self.y_inc = 0
			self.rot = 180
		
	elif key == pygame.K_RIGHT:
		
		self.rect.x += self.x_speed
		if not pygame.sprite.spritecollide(self,wall_sprites,False):
			self.x_inc = self.x_speed
			self.y_inc = 0
			self.rot = 0
	self.rect.x = old_x
	self.rect.y = old_y
		
	"""
	else:
		if key == pygame.K_UP and key == self.last_key_v :
			self.y_inc = 0
			#self.x_inc = 0
		elif key == pygame.K_DOWN and key == self.last_key_v:
			self.y_inc = 0
			#self.x_inc = 0
		elif key == pygame.K_LEFT and key == self.last_key_h:
			self.x_inc = 0
			#self.y_inc = 0
		elif key == pygame.K_RIGHT and key == self.last_key_h:
			self.x_inc = 0
			#self.y_inc = 0
	"""
