import pygame, sys
from pygame.locals import *
import random
import time

#constant
FPS = 10
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
colortext       = (  0,  0,  0)

fonObj = pygame.font.Font('ERASBD.TTF',30)
textSurfaceObj = fonObj.render('game over !',True,colortext,colorbackground)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (windowsWidth / 2,windowsHeight / 2)

pinchou = []
stop = False
xz = False
sjtx = []
direction = 0

class Coordinate:
    row = 0
    clo = 0
    color = (0,0,0)
    def __init__(self,row,clo,color):
        self.row = row
        self.clo = clo
        self.color = color

def huizhi(color,left,top):
    lefts = windowsWidth / clo * left
    tops  = windowsHeight / row * top
    pygame.draw.rect(DISPLAYSURF,color,(lefts,tops,windowsWidth/clo,windowsHeight/row))

def suijituxing(randowGraphics):
    sjtx = []

    if randowGraphics == 0:
        sjtx=[
            Coordinate(0,0,colortian),
            Coordinate(0,1,colortian),
            Coordinate(1,0,colortian),
            Coordinate(1,1,colortian)
        ]
    elif randowGraphics == 1:
        sjtx=[
            Coordinate(1,0,colorfshandian),
            Coordinate(1,1,colorfshandian),
            Coordinate(0,1,colorfshandian),
            Coordinate(0,2,colorfshandian)
        ]
    elif randowGraphics == 2:
        sjtx=[
            Coordinate(1,0,colorfshandian),
            Coordinate(1,1,colorfshandian),
            Coordinate(0,1,colorfshandian),
            Coordinate(0,2,colorfshandian)
        ]

    elif randowGraphics == 3:
        sjtx=[
            Coordinate(0,0,colorgouzi),
            Coordinate(0,1,colorgouzi),
            Coordinate(1,1,colorgouzi),
            Coordinate(2,1,colorgouzi)

]
    elif randowGraphics == 4:
        sjtx=[
            Coordinate(0,0,colorfgouzi),
            Coordinate(0,1,colorfgouzi),
            Coordinate(1,0,colorfgouzi),
            Coordinate(2,0,colorfgouzi)
            
        ]
    elif randowGraphics == 5:
        sjtx=[
            Coordinate(0,0,colorbiandan),
            Coordinate(1,0,colorbiandan),
            Coordinate(2,0,colorbiandan),
            Coordinate(3,0,colorbiandan)
            
        ]
    elif randowGraphics == 6:
        sjtx=[
            Coordinate(0,1,colorfeiji),
            Coordinate(1,0,colorfeiji),
            Coordinate(1,1,colorfeiji),
            Coordinate(1,2,colorfeiji)
            
        ]

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

def chupen(row,clo):
    buer = True
    for l in pinchou:
        if l.row == row and l.clo == clo:
            buer = False
            break

    return buer

def move(zm):
    ydjl = []
    i = len(sjtx) - 1
    if zm == 'a':
        for z in range(len(sjtx)):
            if sjtx[z].clo == 0:
                break
            else:
                if chupen(sjtx[z].row,sjtx[z].clo-1):
                    sjtx[z].clo -= 1
                    ydjl.append(z)
                else:
                    for y in ydjl:
                        sjtx[y].clo += 1
                    break
    elif zm == 'd':
        if sjtx[i].clo == clo - 1:
            pass
        else:
            for z in range(len(sjtx)):
                if chupen(sjtx[z].row,sjtx[z].clo+1):
                    sjtx[z].clo += 1
                    ydjl.append(z)
                else:
                    for y in ydjl:
                        sjtx[y].clo -= 1
                    break
def rotate():
    global direction
    for dt in sjtx:
        if direction == 0:
            dt.row += dt.clo
            dt.clo -= dt.clo
            direction = 1
        elif direction == 1:
            dt.row -= dt.clo
            dt.clo -= dt.clo
            direction = 2
        elif direction == 2:
            dt.row -= dt.clo
            dt.clo += dt.clo
            direction = 3
        elif direction == 3:
            dt.clo += abs(dt.row)
            dt.row -= dt.clo
            direction = 0
            


while True:
    fpsClock.tick(FPS)
    DISPLAYSURF.fill(colorbackground)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif stop:
            if event.type == KEYDOWN:
                if event.key == K_a:
                    move('a')
                elif event.key == K_d:
                    move('d')
                elif event.key == K_w:
                    rotate()
    
    if stop:
        for hz in range(len(sjtx)):
            sjtx[hz].row += 1
            if (sjtx[hz].row < row) and chupen(sjtx[hz].row,sjtx[hz].clo):
                pass
            else:
                while hz >= 0:
                    sjtx[hz].row -= 1
                    hz -= 1
                stop = False
                
                for pc in sjtx:
                    pinchou.append(pc)

                break

        for hz in sjtx:
            huizhi(hz.color,hz.clo,hz.row)
    else:
        randowGraphics = random.randint(0,6)
        sjtx = suijituxing(randowGraphics)
        randomNumber = suijiweizhi(randowGraphics)

        stop = True
    
    for pchz in pinchou:
        if(pchz.row == 0):
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        else:
            huizhi(pchz.color,pchz.clo,pchz.row)

    pygame.display.update()
