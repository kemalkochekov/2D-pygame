import math, random
from random import randint
pi = math.acos(-1)

def get_color():
    return (randint(0,255),randint(0,255),randint(0,255))

def get_speedrate():
    return random.uniform(0, 0.03)        

def position(pos_x,pos_y,x,y,speedrate):
    dx,dy=(x-pos_x), (y-pos_y)
    pos_x,pos_y=pos_x+dx*speedrate, pos_y+dy*speedrate
    return pos_x,pos_y

def norm(x):
    return math.sqrt(x[0]*x[0] + x[1]*x[1])

def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]

def get_angle(A_x, A_y, B_x, B_y):
    A = (B_x - A_x, B_y - A_y)
    B = (B_x - A_x, 0)
    assert A_x != B_x
    return math.acos(dot(A, B)/(norm(A)*norm(B)))*90


