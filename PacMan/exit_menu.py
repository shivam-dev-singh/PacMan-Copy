import pygame
from global_vars import *

exit_flag = True

def message_display(msg,x,y,color,size,gameDisplay):
	fontt = pygame.font.Font('freesansbold.ttf',size)
	textSurface = fontt.render(msg,True,color)
	textRect = textSurface.get_rect()
	textRect.center = (x,y)
	
	gameDisplay.blit(textSurface,textRect)
				
def button(gameDisplay,msg,x,y,w,h,i,a,txt_color,choice,action = None):
	#mouse_positn = pygame.mouse.get_pos()
	#pygame.draw.rect(game_display,i,(x,y,w,h),10)
	pygame.draw.rect(gameDisplay,i,(x,y,w,h))
	
	#click = pygame.mouse.get_pressed()
	wid = 10
	#if (x+w > mouse_positn[0] > x) and (y+h > mouse_positn[1] > y):
	if choice == 1:	
		pygame.draw.rect(gameDisplay,a,(x,y,w,h))
		pygame.draw.rect(gameDisplay,i,(x,y,w,h),wid)
		
		pygame.draw.rect(gameDisplay,i,(x-wid/2,y-wid/2,wid/2,wid/2))
		pygame.draw.rect(gameDisplay,i,(x-wid/2,y+h,wid/2,wid/2))
		pygame.draw.rect(gameDisplay,i,(x+w,y-wid/2,wid/2,wid/2))
		pygame.draw.rect(gameDisplay,i,(x+w,y+h,wid/2,wid/2))
		
		
		keyy = pygame.key.get_pressed()
		if keyy[pygame.K_RETURN]:
			action()
		#print keyy		
	message_display(msg,x+w/2,y+h/2,txt_color,50,gameDisplay)

def exit_it():
	global exit_flag
	exit_flag = False

def quit_it():
	pygame.quit()
	quit()

def exit_menu(gameDisplay):
	global exit_flag
	exit_flag = True
	
	clock = pygame.time.Clock()
	
	#button(msg,x,y,w,h,i,a,action = None)
	w = 140
	h = 80
	choice = 1
	
	while exit_flag == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					choice = 1
				if event.key == pygame.K_LEFT:
					choice = 0 	
	
		#gameDisplay.fill((0,0,0))
		choiceY = 0
		choiceN = 1
		if choice == 0:
			choiceY = 1
			choiceN = 0
		message_display("Want to Exit ?",d_width/2,d_height/4,white,50,gameDisplay)
		button(gameDisplay,'Yes',d_width/2 - (3*w)/2,d_height/2,w,h,red,l_red,white,choiceY,quit_it)
		button(gameDisplay,'No',d_width/2+w/2,d_height/2,w,h,green,l_green,white,choiceN,exit_it)
		
		pygame.display.update()
		clock.tick(30)
