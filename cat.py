import random, pygame
from utility import get_color, get_speedrate, position

class Cat:
    def __init__(self, X, Y):
        self.pos_x = random.randint(0, X)
        self.pos_y = random.randint(0, Y)
        self.color = get_color()
        self.X = X
        self.Y = Y
        self.speedrate = get_speedrate()
    
    def move(self):
        x,y=pygame.mouse.get_pos()
        self.pos_x,self.pos_y=position(self.pos_x,self.pos_y,x,y,self.speedrate)
    def set_position(self):
        self.pos_x = random.randint(0, 100)
        self.pos_y = random.randint(0, self.Y)

    def get(self):
        return [self.c_x, self.c_y, self.v_x, self.v_y]

    def get_pos(self):
        return [self.pos_x, self.pos_y]