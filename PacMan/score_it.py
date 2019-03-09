from global_vars import *

def message_display(gameDisplay,msg,x,y,color,size):
	
	fontt = pygame.font.Font('freesansbold.ttf',size)
	textSurface = fontt.render(msg,True,color)
	textRect = textSurface.get_rect()
	textRect.center = (x,y)
	
	gameDisplay.blit(textSurface,textRect)

def score_display(gameDisplay,score,lives):
	hrt_image = pygame.image.load("heart.png")#.convert()
	hrt_image = pygame.transform.scale(hrt_image,(35,35))
	#hrt_image.set_colorkey(white)
	
	for i in range(0,lives):
		gameDisplay.blit(hrt_image,(int(d_width*0.25)-45+35*i,20-15))

	#message_display(gameDisplay,str(lives),int(d_width*0.25),20,l_green,30)
	
	#coin_image = pygame.Surface((box_w-2*e,box_w-2*e))
	#coin_image_rect = coin_image.get_rect()
	#coin_image_rect.x = int(d_width*0.75)-20
	#coin_image_rect.y = 20
	pygame.draw.circle(gameDisplay,yellow,(int(d_width*0.80)-30,20),int(1.4*rad_of_coins))
	
	message_display(gameDisplay,str(score),int(d_width*0.80),20,l_green,30)
