import sys
import pygame
from pygame.locals import *
import coordinate
import random
import time

pygame.init()

window_height = 500
window_width = 500

ROW = 20    
CLO = 20

FPS = 10

rect_width = window_width / CLO
rect_height = window_height / ROW

#Color definition
color_background = (150,150,150)
color_snake = (0,140,63)

window = pygame.display.set_mode((window_width, window_height))
anotherSurFace = window.convert_alpha()
pygame.display.set_caption('tan chi she')
clock = pygame.time.Clock()

Coordinate = coordinate.Coordinate

direction = {"up":K_w,"down":K_s,"left":K_a,"right":K_d}

orientation = direction["right"]

def rect(coordinate):
    left = coordinate.clo * rect_width
    top = coordinate.row * rect_height
    pygame.draw.rect(window, coordinate.color, (left, top, rect_width, rect_height))

def move(orientation):
    if orientation == direction["up"]:
        head.row -= 1
    elif orientation == direction["down"]:
        head.row += 1
    elif orientation == direction["left"]:
        head.clo -= 1
    elif orientation == direction["right"]:
        head.clo += 1

head = Coordinate(0,0,color_snake)
while True:
    clock.tick(FPS)
    window.fill(color_background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == direction["up"]:
                orientation = direction["up"]
            elif event.key == direction["down"]:
                orientation = direction["down"]
            elif event.key == direction["left"]:
                orientation = direction["left"]
            elif event.key == direction["right"]:
                orientation = direction["right"]
    move(orientation)
    rect(head)
    pygame.display.update()