import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#set up the windows
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

WHITE = (225,225,225)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10

direction = 'reight'

while True:
    #设置背景颜色
    DISPLAYSURF.fill(WHITE)

    if direction == 'reight':
        catx += 5
        if catx == 280:
            direction = 'down'

    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'

    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'reight'
    
    DISPLAYSURF.blit(catImg,(catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)
