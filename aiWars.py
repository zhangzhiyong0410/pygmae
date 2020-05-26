import pygame, sys
from pygame.locals import *
import random
import time

pygame.init()

width = 400
hight = 800

ROW = 40    #行
CLO = 20    #列

#颜色

#战机颜色
warplaneColor = (221,0,0)
#敌机颜色
enemyPlaneColor = (0,0,0,0) 
#炮弹颜色
cannonballColor = (255,255,100)

starttime = time.time()

window = pygame.display.set_mode((width, hight))

anotherSurFace = window.convert_alpha()
pygame.display.set_caption('雷霆战机迷你版')

class Coordinate:

    row = 0
    clo = 0

    def __init__(self,row,clo):

        self.row = row
        self.clo = clo



#画图
def rect(coordinate, color):
    # 定位 画图需要left和top
    left = coordinate.clo * width / CLO
    top = coordinate.row * hight / ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, width / CLO, hight / ROW))

#战斗机初始位置
warplane = Coordinate(ROW-1,int(CLO/2))

#敌机
enemyPlaneList = []
#炮弹
cannonballList = []

# 设置帧频率
clock = pygame.time.Clock()

enemyPlaneNum = 0

while True:
    # 处理帧频 锁帧
    clock.tick(10)

    # pygame.event.get()获取当前事件的队列 可以同时发生很多事件
    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            sys.exit()

        #控制战机并且不让他超出窗口
        elif event.type == KEYDOWN:
            if event.key == K_w:
                if warplane.row > 1:                
                    warplane.row -= 1
            elif event.key == K_s:
                if warplane.row < ROW-1:
                    warplane.row += 1
            elif event.key == K_a:
                if warplane.clo > 1:
                    warplane.clo -= 1
            elif event.key == K_d:
                if warplane.clo < CLO-2:
                    warplane.clo += 1

    #背景画图
    window.fill((225,225,225))

    #战机绘制
    rect(warplane,warplaneColor)

    warplanes=[

    Coordinate(warplane.row,warplane.clo-1),
    Coordinate(warplane.row,warplane.clo+1),
    Coordinate(warplane.row-1,warplane.clo)

    ]
    
    for i in warplanes:

        rect(i,warplaneColor)

    #随机出现敌军
    enemyPlaneList.insert(enemyPlaneNum,Coordinate(0,random.randint(0, CLO)))

    cannonballList.insert(enemyPlaneNum,Coordinate(warplanes[2].row-1,warplanes[2].clo))        

    #敌机状态
    enemyPlaneState = True


    esum = 0
    enemyPlaneLen = len(enemyPlaneList)

    cannonballLen = len(cannonballList)
    

    #敌军冲锋
    while esum < enemyPlaneLen:
    
        enemyPlaneList[esum].row += 1 

        #判断炮弹有没有打中
        csum = 0
        while csum < cannonballLen:
            enemyPlaneState = True
            if (enemyPlaneList[esum].row == cannonballList[csum].row and enemyPlaneList[esum].clo == cannonballList[csum].clo) or (enemyPlaneList[esum].row+1 == cannonballList[csum].row and enemyPlaneList[esum].clo == cannonballList[csum].clo):
                
                del enemyPlaneList[esum]
                enemyPlaneLen = len(enemyPlaneList)
                
                del cannonballList[csum]
                cannonballLen = len(cannonballList)

                enemyPlaneState = False
                break

            csum += 1

        #判断有没有碰到敌军
        if enemyPlaneState:

            for w in warplanes:

                if enemyPlaneList[esum].row == w.row and enemyPlaneList[esum].clo == w.clo:

                    print("碰到你就没了~")
                    pygame.quit()
                    sys.exit()
        esum+=1


    #敌机绘制
    for e in enemyPlaneList:

        rect(e,enemyPlaneColor)

    #炮火轰鸣
    for c in cannonballList:
        
        c.row -= 1
    
    #炮弹绘制
    for c in cannonballList:
        
        rect(c,cannonballColor)
     

    pygame.display.update()

