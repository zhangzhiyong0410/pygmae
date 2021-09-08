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

color_background = (150,150,150)
color_snake = (0,140,63)
color_fruit = (255,0,0)

window = pygame.display.set_mode((window_width, window_height))
anotherSurFace = window.convert_alpha()
pygame.display.set_caption('tan chi she')
clock = pygame.time.Clock()

coordinates = coordinate.Coordinate

direction = {"up":K_w,"down":K_s,"left":K_a,"right":K_d}
orientation = direction["right"]
fruit_coordinate = coordinates(0,0,(0,0,0))
fruit_state = True

def rect(coordinate):
    left = coordinate.clo * rect_width
    top = coordinate.row * rect_height
    pygame.draw.rect(window, coordinate.color, (left, top, rect_width, rect_height))

def move(orientation):
    if orientation == direction["up"]:
        head[0].row -= 1
    elif orientation == direction["down"]:
        head[0].row += 1
    elif orientation == direction["left"]:
        head[0].clo -= 1
    elif orientation == direction["right"]:
        head[0].clo += 1

def overstep_the_boundary(list_snake):
    if list_snake[0].row >= 0 and list_snake[0].clo >= 0:
        if list_snake[0].row >= ROW or list_snake[0].clo >= CLO:
            return True
        else:
            for i in range(1,len(head)):
                if head[i].row == head[0].row and head[i].clo == head[0].clo:
            
                    return True
            return False
    else:
        return True

def fruit():
    random_row = random.randint(0,ROW - 1)
    random_clo = random.randint(0,CLO - 1)
    return coordinates(random_row,random_clo,color_fruit)

def grow_up():
    head.append(coordinates(0,0,color_snake))

head = [coordinates(0,0,color_snake)]
cishu = 0
while True:
    cishu+=1
    clock.tick(FPS)
    window.fill(color_background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == direction["up"]:
                if len(head) <= 1:
                    orientation = direction["up"]
                else:
                    if orientation != direction["down"]:
                        orientation = direction["up"]
                break
            elif event.key == direction["down"]:
                if len(head) <= 1:
                    orientation = direction["down"]
                else:
                    if orientation != direction["up"]:
                        orientation = direction["down"]
                break
            elif event.key == direction["left"]:
                if len(head) <= 1:
                    orientation = direction["left"]
                else:
                    if orientation != direction["right"]:
                        orientation = direction["left"]
                break
            elif event.key == direction["right"]:
                if len(head) <= 1:
                    orientation = direction["right"]
                else:
                    if orientation != direction["left"]:
                        orientation = direction["right"]
                break
                
    if fruit_state:
        fruit_coordinate = fruit()
        fruit_state = False
    
    if head[0].row == fruit_coordinate.row and head[0].clo == fruit_coordinate.clo:
        grow_up()
        fruit_state = True
    
    rect(fruit_coordinate)


    record_row = head[0].row
    record_clo = head[0].clo
    Intermediary_row = 0
    Intermediary_clo = 0
    move(orientation)
    rect(head[0])
    if overstep_the_boundary(head):
        pygame.quit()
        sys.exit()
    
    for r in range(1,len(head)):
        Intermediary_row = head[r].row
        Intermediary_clo = head[r].clo
        head[r].row = record_row
        head[r].clo = record_clo
        record_row = Intermediary_row
        record_clo = Intermediary_clo  
        rect(head[r])  

    pygame.display.update()