import pygame
from sys import exit
from cat import Cat
import random
from utility import get_angle

pygame.init()


X, Y = 1300, 800
screen = pygame.display.set_mode((X,Y))
clock = pygame.time.Clock()

c_r = 15

cat = 10
cats = []

catpc = pygame.image.load("cat.png").convert_alpha()
catpc = pygame.transform.scale(catpc, (150, 150))

clew = pygame.image.load("clew.png").convert_alpha()
clew = pygame.transform.scale(clew, (70, 60))

grass = pygame.image.load("grass.jpg").convert_alpha()
grass = pygame.transform.scale(grass, (X, Y))

    
for i in range(cat):
    cats.append(Cat(X, Y))

while True:
    screen.blit(grass, (0,0))
    x, y = pygame.mouse.get_pos()
    screen.blit(clew, (x-20, y-30))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print("click")
            for i in range(cat):
                cats[i].set_position()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(cat):
        cats[i].move()
        pos_x, pos_y = cats[i].get_pos()
        alpha = get_angle(pos_x, pos_y, x, y)
        rotated_cat = pygame.transform.rotate(catpc, alpha)
        rotated_cat = pygame.transform.flip(rotated_cat, (x < pos_x), (pos_y +60< y))
        screen.blit(rotated_cat, (pos_x-70, pos_y-60))
        #pygame.draw.circle(screen, color, (c_x, c_y), c_r)
    
    clock.tick(30) #FPS

    pygame.display.update()
