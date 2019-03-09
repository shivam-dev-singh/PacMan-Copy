import pygame
from global_vars import *
from wall import Wall
from wormhole import Wormhole

def map1(screen):
	x = (d_width - 10*box_w)/2
	y = (d_height - 11*box_w)/2
	
	wall1 = Wall(x+0,y+0,10*box_w+e,e,l_blue)
	wall2 = Wall(x+0,y+0,e,4*box_w+e,l_blue) 
	wall3 = Wall(x+0,y+4*box_w,2*box_w,e,l_blue)
	wall4 = Wall(x+2*box_w,y+4*box_w,e,1*box_w+e,l_blue)
	wall5 = Wall(x+0,y+5*box_w,2*box_w,e,l_blue)
	wall6 = Wall(x+0,y+6*box_w,2*box_w,e,l_blue)
	wall7 = Wall(x+2*box_w,y+6*box_w,e,1*box_w+e,l_blue)
	wall8 = Wall(x+0,y+7*box_w,2*box_w,e,l_blue)
	wall9 = Wall(x+0,y+7*box_w,e,4*box_w+e,l_blue)
	wall10 = Wall(x+0,y+9*box_w,1*box_w+e,e,l_blue)
	wall11 = Wall(x+0,y+11*box_w,10*box_w+e,e,l_blue)
	wall12 = Wall(x+10*box_w,y+7*box_w,e,4*box_w,l_blue)
	wall13 = Wall(x+9*box_w,y+9*box_w,1*box_w,e,l_blue)
	wall14 = Wall(x+8*box_w,y+7*box_w,2*box_w,e,l_blue)
	wall15 = Wall(x+8*box_w,y+6*box_w,e,1*box_w,l_blue)
	wall16 = Wall(x+8*box_w,y+6*box_w,2*box_w,e,l_blue)
	wall17 = Wall(x+8*box_w,y+5*box_w,2*box_w,e,l_blue)
	wall18 = Wall(x+8*box_w,y+4*box_w,e,1*box_w,l_blue)
	wall19 = Wall(x+8*box_w,y+4*box_w,2*box_w,e,l_blue)
	wall20 = Wall(x+10*box_w,y+0,e,4*box_w+e,l_blue)
	wall21 = Wall(x+5*box_w,y+0,e,2*box_w+e,l_blue)
	
	wall22 = Wall(x+1*box_w,y+1*box_w,1*box_w+e,1*box_w+e,l_blue)
	wall23 = Wall(x+1*box_w,y+3*box_w,1*box_w+e,e,l_blue)
	wall24 = Wall(x+1*box_w,y+8*box_w,1*box_w,e,l_blue)
	wall25 = Wall(x+1*box_w,y+10*box_w,3*box_w+e,e,l_blue)
	
	wall26 = Wall(x+2*box_w,y+8*box_w,e,1*box_w+e,l_blue)
	
	wall27 = Wall(x+3*box_w,y+1*box_w,1*box_w+e,1*box_w+e,l_blue)
	wall28 = Wall(x+3*box_w,y+3*box_w,e,2*box_w+e,l_blue)
	wall29 = Wall(x+3*box_w,y+6*box_w,e,1*box_w+e,l_blue)
	wall30 = Wall(x+3*box_w,y+8*box_w,1*box_w+e,e,l_blue)
	wall31 = Wall(x+3*box_w,y+9*box_w,e,1*box_w+e,l_blue)
	
	wall32 = Wall(x+4*box_w,y+3*box_w,2*box_w+e,e,l_blue)
	wall33 = Wall(x+4*box_w,y+5*box_w,0.7*box_w,e,l_blue)
	wall34 = Wall(x+4*box_w,y+5*box_w,e,1*box_w+e,l_blue)
	wall35 = Wall(x+4*box_w,y+6*box_w,2*box_w+e,e,l_blue)
	wall36 = Wall(x+4*box_w,y+7*box_w,2*box_w+e,e,l_blue)
	wall37 = Wall(x+4*box_w,y+9*box_w,2*box_w+e,e,l_blue)
	
	wall38 = Wall(x+5*box_w,y+3*box_w,e,1*box_w+e,l_blue)
	wall39 = Wall(x+5*box_w,y+7*box_w,e,1*box_w+e,l_blue)
	wall40 = Wall(x+5*box_w,y+9*box_w,e,1*box_w+e,l_blue)
	
	wall41 = Wall(x+6*box_w,y+1*box_w,1*box_w+e,1*box_w+e,l_blue)
	wall42 = Wall(x+6*box_w,y+4*box_w,1*box_w,e,l_blue)
	wall43 = Wall(x+5.3*box_w,y+5*box_w,0.7*box_w+e,e,l_blue)
	wall44 = Wall(x+6*box_w,y+5*box_w,e,1*box_w+e,l_blue)
	wall45 = Wall(x+6*box_w,y+8*box_w,1*box_w+e,e,l_blue)
	wall46 = Wall(x+6*box_w,y+10*box_w,3*box_w+e,e,l_blue)
	
	wall47 = Wall(x+7*box_w,y+3*box_w,e,2*box_w+e,l_blue)
	wall48 = Wall(x+7*box_w,y+6*box_w,e,1*box_w+e,l_blue)
	wall49 = Wall(x+7*box_w,y+9*box_w,e,1*box_w,l_blue)
	
	wall50 = Wall(x+8*box_w,y+1*box_w,1*box_w+e,1*box_w+e,l_blue)
	wall51 = Wall(x+8*box_w,y+3*box_w,1*box_w+e,e,l_blue)
	wall52 = Wall(x+8*box_w,y+8*box_w,1*box_w+e,e,l_blue)
	wall53 = Wall(x+8*box_w,y+8*box_w,e,1*box_w+e,l_blue)
	wall54 = Wall(x+3*box_w,y+4*box_w,1*box_w+e,e,l_blue)
	
	
	""" to create wormholes to teleport the ball from left end to right end and vice versa """
	
	wormhole_left = Wormhole(x00 ,y00 + 5*box_w,e,box_w,x00+9*box_w+e+2,y00+5*box_w+e+2)
	wormhole_right = Wormhole(x00 +10*box_w,y00 + 5*box_w,e,box_w,x00+e+2,y00+5*box_w+e+2) 
	
	#wormhole_left = Wormhole(x00 - box_w,y00 + 5*box_w,e,box_w,x00+9*box_w+e+2 + 2*b_unit,y00+5*box_w+e+2)
	#wormhole_right = Wormhole(x00 +10*box_w+ box_w,y00 + 5*box_w,e,box_w,x00+e+2 - 2*b_unit,y00+5*box_w+e+2) 	
		
	"""
	pygame.draw.rect(screen,bg_color,[x+1*box_w+e,y+1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[x+3*box_w+e,y+1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[x+6*box_w+e,y+1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[x+8*box_w+e,y+1*box_w+e,unit,unit])
	
	pygame.draw.rect(screen,bg_color,[1*box_w+e,1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[3*box_w+e,1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[6*box_w+e,1*box_w+e,unit,unit])
	pygame.draw.rect(screen,bg_color,[8*box_w+e,1*box_w+e,unit,unit])
	"""
	
