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

#Color              R   G   B
colorbackground = (225,225,225)
colortian       = (128,  0,225)
colorshandian   = (  0,225,225)
colorfshandian  = (225,128,  0)
colorgouzi      = (225,  0,225)
colorfgouzi     = (225,225,  0)
colorbiandan    = (225,  0,  0)
colorfeiji      = (  0,  0,128)

DISPLAYSURF.fill(backgroundColor)


class Coordinate:
    row = 0
    clo = 0
    def __init__(self,row,clo):
        self.row = row
        self.clo = clo
#patterning
head = Coordinate(0,0)

patterningtian=[
    Coordinate(head.row+1,head.clo),
    Coordinate(head.row,head.clo+1),
    Coordinate(head.row+1,head.clo+1)
]
patterningshandian=[
    Coordinate(head.row,head.clo+1),
    Coordinate(head.row+1,head.clo+1),
    Coordinate(head.row+1,head.clo+1+1)
]
patterningfshandian=[
    Coordinate(head.row,head.clo-1),
    Coordinate(head.row+1,head.clo-1),
    Coordinate(head.row+1,head.clo-1-1)
]
patterninggouzi=[
    Coordinate(head.row+1,head.clo),
    Coordinate(head.row+1+1,head.clo),
    Coordinate(head.row+1+1,head.clo-1)
]
patterningfgouzi=[
    Coordinate(head.row+1,head.clo),
    Coordinate(head.row+1+1,head.clo),
    Coordinate(head.row+1+1,head.clo+1)
]
patterningbiandan=[
    Coordinate(head.row+1,head.clo),
    Coordinate(head.row+1+1,head.clo),
    Coordinate(head.row+1+1+1,head.clo),
]
patterningfeiji=[
    Coordinate(head.row+1,head.clo),
    Coordinate(head.row+1,head.clo+1),
    Coordinate(head.row+1,head.clo-1)
]

def drawing():
    unnecessaryL = 0
    unnecessaryR = 0

    unnecessary()
    
    for draw in patterning:
        pygame.draw.rect(DISPLAYSURF, color, (left, 0, windowsWidth / clo,windowsHeight / row))

def unnecessary():
    
    L = 0
    R = 0

    patterning = []    

    unnecessaryDict = {
        'color':(0,0,0),
        'left':'',
        'patterning':[]
    }

    patterningRandom = random.randint(0,6)
    if patterningRandom == 0:
        patterning = patterningtian
        unnecessaryDict['color'] = colortian
    elif patterningRandom == 1:
        patterning = patterningshandian
        unnecessaryDict['color'] = colorshandian
    elif patterningRandom == 2:
        patterning = patterningfshandian
        unnecessaryDict['color'] = colorfshandian
    elif patterningRandom == 3:
        patterning = patterninggouzi
        unnecessaryDict['color'] = colorgouzi
    elif patterningRandom == 4:
        patterning = patterningfgouzi
        unnecessaryDict['color'] = colorfgouzi
    elif patterningRandom == 5:
        patterning = patterningbiandan
        unnecessaryDict['color'] = colorbiandan
    elif patterningRandom == 6:
        patterning = patterningfeiji
        unnecessaryDict['color'] = colorfeiji

    for p in patterning:
        if(p.Coordinate.clo<=L):
            L = p.Coordinate.clo
        if(p.Coordinate.clo>=R):
            R = p.Coordinate.clo
    left = 
        
            

    


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()