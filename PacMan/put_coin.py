import pygame
from global_vars import *
from coin import Coin
import random

def put_coin():
	x0 = (d_width - 10*box_w)/2
	y0 = (d_height - 11*box_w)/2
	for i in range(0,11):
	  	for j in range(0,10):
	  		if (i == 4 and ( j == 0 or j == 1 or j == 8 or j == 9)) or (i == 6 and ( j == 0 or j == 1 or j == 8 or j == 9)) or   (i == 5 and ( j == 4 or j == 5)):
	  			continue 
  			x = x0 + j*box_w + e
  			y = y0 + i*box_w + e
  			
  			coinn = Coin(x,y,rad_of_coins,yellow)
  	pygame.sprite.groupcollide(coin_sprites,wall_sprites,True,False)
