#important 
#1. image.rect.x + b_unit( or x_speed ) > unit
# need to find relation between unit,e,image.rect and b_unit to make the game playable ?

import pygame
from os import path

d_width = 600
d_height = 600

all_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
wormhole_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

#game sounds
snd_dir = path.join(path.dirname(__file__),'sounds')
pygame.mixer.init()
boom_sound = pygame.mixer.Sound(path.join(snd_dir,'06.wav'))
crash_sound = pygame.mixer.Sound(path.join(snd_dir,'pacman_death.wav'))

unit = 40
e = 5

box_w = unit + e

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
l_red = (255,0,0)
green = (0,200,0)
l_green = (0,255,0)
blue = (0,0,200)
l_blue = (0,0,255)
yellow = (255,255,0)

bg_color = black

#solid_sprites = pygame.sprite.Group()
b_unit = 10

x00 = (d_width - 10*box_w)/2
y00 = (d_height - 11*box_w)/2

#checked playable values:
#unit = 40
#e = 5
#b_unit = 10
#image_rect = (32,32)	(33,33) is also good
#clock.tick(30)

rad_of_coins = int(unit*0.15)

#coin_grp = []

#enemy
directns = [273,274,276,275]
player_x = x00+e+2
player_y = y00+e+2

