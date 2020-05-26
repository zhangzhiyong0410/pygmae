import pygame, sys
from pygame.locals import *
import random


#constant
FPS = 30
windowsWidth    = 200   #窗口宽
windowsHeight   = 500   #窗口高
row             = 25    #行
clo             = 10    #列



pygame.init()
DISPLAYSURF = pygame.display.set_mode((windowsWidth,windowsHeight))
pygame.display.set_caption('tetris')
fpsClock = pygame.time.Clock()

#Color              R   G   B
colorbackground = (225,225,225)
colortian       = (128,  0,225)
colorshandian   = (  0,225,225)
colorfshandian  = (225,128,  0)
colorgouzi      = (225,  0,225)
colorfgouzi     = (225,225,  0)
colorbiandan    = (225,  0,  0)
colorfeiji      = (  0,  0,128)


class Coordinate:
    row = 0
    clo = 0
    color = (0,0,0)
    def __init__(self,row,clo,color):
        self.row = row
        self.clo = clo
        self.color = color