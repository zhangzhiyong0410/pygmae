import random
import sys
import time
import coordinate

import pygame
from pygame.locals import *

score           = 0
#constant
FPS             = 6
gamesWidth      = 200   #游戏口宽
windowsWidht    = 300
windowsHeight   = 500   #窗口高
row             = 25    #行
clo             = 10    #列



pygame.init()
DISPLAYSURF = pygame.display.set_mode((300,windowsHeight))
icon = pygame.image.load('a.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('tetris')
fpsClock = pygame.time.Clock()


#Color              R   G   B
colorbackground = ( 69, 69, 69)
colortian       = (128,  0,225)
colorshandian   = (  0,225,225)
colorfshandian  = (225,128,  0)
colorgouzi      = (225,  0,225)
colorfgouzi     = (225,225,  0)
colorbiandan    = (225,  0,  0)
colorfeiji      = (  0,  0,128)
colortext       = (  0,  0,  0)
colorscore      = (  0,128,192)

Coordinate = coordinate.Coordinate

pinchou = []
stop = False
xz = False
over = False
sjtx = []

def wenzihuizhi(content,left,top):
    fonObj = pygame.font.Font('ERASBD.TTF',20)
    textSurfaceObj = fonObj.render(content,True,colorbackground,colorscore)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (left,top)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)

def huizhi(color,left,top):
    lefts = gamesWidth / clo * left
    tops  = windowsHeight / row * top
    pygame.draw.rect(DISPLAYSURF,color,(lefts,tops,gamesWidth/clo,windowsHeight/row),5)

def suijituxing(randowGraphics,randomNumber):
    global sjtx
    if randowGraphics == 0:
        sjtx=[
            Coordinate(0,0+randomNumber,colortian),
            Coordinate(0,1+randomNumber,colortian),
            Coordinate(1,0+randomNumber,colortian),
            Coordinate(1,1+randomNumber,colortian)
        ]
    elif randowGraphics == 1:
        sjtx=[
            Coordinate(0,0+randomNumber,colorshandian),
            Coordinate(0,1+randomNumber,colorshandian),
            Coordinate(1,1+randomNumber,colorshandian),
            Coordinate(1,2+randomNumber,colorshandian)
        ]
    elif randowGraphics == 2:
        sjtx=[
            Coordinate(1,0+randomNumber,colorfshandian),
            Coordinate(1,1+randomNumber,colorfshandian),
            Coordinate(0,1+randomNumber,colorfshandian),
            Coordinate(0,2+randomNumber,colorfshandian)
        ]

    elif randowGraphics == 3:
        sjtx=[
            Coordinate(0,0+randomNumber,colorgouzi),
            Coordinate(0,1+randomNumber,colorgouzi),
            Coordinate(1,1+randomNumber,colorgouzi),
            Coordinate(2,1+randomNumber,colorgouzi)

]
    elif randowGraphics == 4:
        sjtx=[
            Coordinate(0,0+randomNumber,colorfgouzi),
            Coordinate(1,0+randomNumber,colorfgouzi),
            Coordinate(2,0+randomNumber,colorfgouzi),
            Coordinate(0,1+randomNumber,colorfgouzi)
            
        ]
    elif randowGraphics == 5:
        sjtx=[
            Coordinate(0,0+randomNumber,colorbiandan),
            Coordinate(1,0+randomNumber,colorbiandan),
            Coordinate(2,0+randomNumber,colorbiandan),
            Coordinate(3,0+randomNumber,colorbiandan)
            
        ]
    elif randowGraphics == 6:
        sjtx=[
            Coordinate(1,0+randomNumber,colorfeiji),
            Coordinate(0,1+randomNumber,colorfeiji),
            Coordinate(1,1+randomNumber,colorfeiji),
            Coordinate(1,2+randomNumber,colorfeiji)
            
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


#触碰判断
def chupen(row,clo):
    buer = True
    for l in pinchou:
        if l.row == row and l.clo == clo:
            buer = False
            break

    return buer

#左右移动
def move(zm):
    global sjtx
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

#旋转
def rotate():
    global sjtx
    if sjtx[0].color != colortian:
        zx = sjtx[2]

        jl = True

        #依次判断所有的块选择以后会不会越界
        for xz in sjtx:
            num1 = zx.clo - xz.clo
            num2 = zx.row - xz.row
            xiadiy = zx.row - num1
            yuejie = zx.clo + num2
            if yuejie < 0 or yuejie > clo - 1 or xiadiy > row - 1 or chupen(xiadiy,yuejie) == False:
                jl = False

        if jl:
            for xz in sjtx:
                num1 = zx.clo - xz.clo
                num2 = zx.row - xz.row
                xz.row = zx.row - num1
                xz.clo = zx.clo + num2

        #列表顺序调整
        min = sjtx[0]
        max = sjtx[0]
        for h in range(len(sjtx)):
            min = sjtx[0]
            max = sjtx[len(sjtx)-1]
            if sjtx[h].clo < sjtx[0].clo:
                sjtx[0] = sjtx[h]
                sjtx[h] = min
            if sjtx[h].clo > sjtx[len(sjtx)-1].clo:
                sjtx[len(sjtx)-1] = sjtx[h]
                sjtx[h] = max

#过滤重复列表
def odb():
    bt = []
    q = True
    for i in sjtx:
        if q:
            bt.append(i.row)
            q = False

        xt = True
        
        for j in bt:
            if i.row == j:
                xt=False
        if xt:
            bt.append(i.row)

    number = 0
    for wm in range(len(bt)):
        i = wm
        while i < len(bt):
            number = bt[wm]
            if bt[i]<bt[wm]:
                bt[wm] = bt[i]
                bt[i] = number
            i+=1


    return bt

def defen():
    fs = 0
    dfl = []
    for i in sjtx:
        fs = 0
        for pc in pinchou:
            fs = 0
            if pc.row == i.row:
                fs += 1
                if fs == 10:
                    dfl.append(pc)
                    fs = 0
    
    for sc in dfl:
        for pc in pinchou:
            if pc.row == sc.row:
                pc.row
while True:
    fpsClock.tick(FPS)
    DISPLAYSURF.fill(colorbackground)
    pygame.draw.rect(DISPLAYSURF,colorscore,(200,0,100,500))
    stringscore = 'score:'+str(score)
    wenzihuizhi(stringscore,gamesWidth+(windowsWidht-gamesWidth)/2,100)
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
                fs = 0
                for pd in odb():
                    fs = 0
                    for pc in pinchou:
                        if pc.row == 99:
                            continue
                        if pd == pc.row:
                            fs += 1
                            if fs == 10:
                                fs = 0
                                if over:
                                    pass
                                else:
                                    score += 1
                                for df in pinchou:
                                    if df.row == pd:
                                        df.row = 99
                                    elif df.row < pd:
                                        df.row += 1
                break

        for hz in sjtx:
            huizhi(hz.color,hz.clo,hz.row)
    else:
        randowGraphics = random.randint(0,6)
        randomNumber = suijiweizhi(randowGraphics)
        sjtx = suijituxing(randowGraphics,randomNumber)

        stop = True
    
    
    for pchz in pinchou:
        if(pchz.row == 0):
            wenzihuizhi('game over!!!',windowsWidht/2,windowsHeight/2)
            over = True
        else:
            huizhi(pchz.color,pchz.clo,pchz.row)

    pygame.display.update()
