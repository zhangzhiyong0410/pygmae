import pygame,sys
from pygame.locals import *
import pymysql

#constant
FPS             = 1
windowsWidth      = 200   #窗口宽度
windowsHeight   = 500   #窗口高度
row             = 25    #行
clo             = 10    #列

pygame.init()
DISPLAYSURF = pygame.display.set_mode((windowsWidth,windowsHeight))
icon = pygame.image.load('a.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('Jacob\'s ladder')
fpsClock = pygame.time.Clock()

db = pymysql.connect("localhost","root","123456","tetris" )
cursor = db.cursor()

sql = "SELECT * FROM highscorelist"

#color
colorbeijing    = (192,192,192)
colorziti       = (255,  0,  0)
coloranniu      = (255,255,  0)

sql = "SELECT * FROM highscorelist"
cursor.execute(sql)
results = cursor.fetchall()

def wenzihuizhi(content,left,top):
    fonObj = pygame.font.Font('ERASBD.TTF',20)
    textSurfaceObj = fonObj.render(content,True,colorziti,colorbeijing)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (left,top)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)

while True:
    DISPLAYSURF.fill(colorbeijing)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    wenzihuizhi('Jacob\'s ladder',windowsWidth/2,20)
    hanweihzi = 40
    for row in results:
        id = row[0]
        name = row[1]
        score = row[2]
        # 打印结果
        zifu = name+'----------'+str(score)
        wenzihuizhi(zifu,windowsWidth/2,hanweihzi)
        hanweihzi += 20

    pygame.display.update()