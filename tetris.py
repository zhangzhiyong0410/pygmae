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

txT=[

    Coordinate(0,0,colortian),
    Coordinate(0,1,colortian),
    Coordinate(1,0,colortian),
    Coordinate(1,1,colortian)
    
]

txSd=[

    Coordinate(0,0,colorshandian),
    Coordinate(0,1,colorshandian),
    Coordinate(1,1,colorshandian),
    Coordinate(1,2,colorshandian)
]

txFsd=[

    Coordinate(1,0,colorfshandian),
    Coordinate(1,1,colorfshandian),
    Coordinate(0,1,colorfshandian),
    Coordinate(0,2,colorfshandian)
]

txGz=[

    Coordinate(0,0,colorgouzi),
    Coordinate(0,1,colorgouzi),
    Coordinate(1,1,colorgouzi),
    Coordinate(2,1,colorgouzi)

]

txFgz=[

    Coordinate(0,0,colorfgouzi),
    Coordinate(0,1,colorfgouzi),
    Coordinate(1,0,colorfgouzi),
    Coordinate(2,0,colorfgouzi)
    
]

txBd=[

    Coordinate(0,0,colorbiandan),
    Coordinate(1,0,colorbiandan),
    Coordinate(2,0,colorbiandan),
    Coordinate(3,0,colorbiandan)
    
]

txFj=[

    Coordinate(0,1,colorfeiji),
    Coordinate(1,0,colorfeiji),
    Coordinate(1,1,colorfeiji),
    Coordinate(1,2,colorfeiji)
    
]

def huizhi(color,left,top):
    lefts = windowsWidth / clo * left
    tops  = windowsHeight / row * top
    pygame.draw.rect(DISPLAYSURF,color,(lefts,tops,windowsWidth/clo,windowsHeight/row))



def suijituxing(randowGraphics):

    sjtx = []

    if randowGraphics == 0:
        sjtx = txT
    elif randowGraphics == 1:
        sjtx = txSd
    elif randowGraphics == 2:
        sjtx = txFsd
    elif randowGraphics == 3:
        sjtx = txGz
    elif randowGraphics == 4:
        sjtx = txFgz
    elif randowGraphics == 5:
        sjtx = txBd
    elif randowGraphics == 6:
        sjtx = txFj

    return sjtx


def suijiweizhi(randowGraphics):

    if randowGraphics == 0:
        randomNumber = random.randint(0,8)
    elif randowGraphics == 1:
        randomNumber = random.randint(0,7)
    elif randowGraphics == 2:
        randomNumber = random.randint(0,7)
    elif randowGraphics == 3:
        randomNumber = random.randint(0,8)
    elif randowGraphics == 4:
        randomNumber = random.randint(0,8)
    elif randowGraphics == 5:
        randomNumber = random.randint(0,9)
    elif randowGraphics == 6:
        randomNumber = random.randint(0,7)

    return randomNumber

def chupen(lst,row,clo):
    buer = True
    for l in lst:
        if l.row == row and l.clo == clo:
            buer = False
            break
    return buer



pinchou = []
stop = False
xz = False

while True:
    fpsClock.tick(FPS)
    DISPLAYSURF.fill(colorbackground)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if stop:
        for hz in range(len(sjtx)):
            sjtx[hz].row += 1
            if (sjtx[hz].row < row) and chupen(pinchou,sjtx[hz].row,sjtx[hz].clo):
                huizhi(sjtx[hz].color,sjtx[hz].clo,sjtx[hz].row)
            else:
                while hz >= 0:
                    sjtx[hz].row -= 1
                    hz -= 1
                stop = False
                xz = True
                break
    else:
        randowGraphics = random.randint(0,6)
        sjtx = suijituxing(randowGraphics)
        randomNumber = suijiweizhi(randowGraphics)

        stop = True
        xz = False

    if xz:
        for pc in sjtx:
            pinchou.append(pc)
    
    for pchz in pinchou:
        huizhi(pchz.color,pchz.clo,pchz.row)
    pygame.display.update()