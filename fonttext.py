import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello Word!')


WHITE = (225,225,225)
GREEN = (0,225,0)
BLUE = (0,0,128)

fonObj = pygame.font.Font('ERASBD.TTF',32)
textSurfaceObj = fonObj.render('Hello World!',True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True:
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(textSurfaceObj,textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
            
