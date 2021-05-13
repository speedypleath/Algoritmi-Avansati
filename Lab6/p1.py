import random
import numpy
from shapely.geometry import LineString

epsilon = 0.00001

def coliniar(a,b,c):
    return abs((c[1]-a[1]) * (b[0]-a[0]) - (b[1]-a[1]) * (c[0]-a[0])) < epsilon

def distanta(a,b):
    return numpy.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return coliniar(a,b,c) and abs(distanta(a, c) + distanta(c, b) - distanta(a, b)) > epsilon

def intersect(a,b,c,d):
    line1 = LineString([a,b])
    line2 = LineString([c,d])
    return line1.intersects(line2)

f = open("p1.in")

n = int(f.readline())
poligon = [None] * n
for i in range(n):
    poligon[i] = tuple(float(x) for x in f.readline().split(" "))
punct = tuple(float(x) for x in f.readline().split(" "))

x = min(poligon)[0]
y = min(poligon, key = lambda x: x[1])[1] 
martor = (random.uniform(x-110, x-10), random.uniform(y-110, y-10))
while martor[1] == punct[1]:
    martor = (random.uniform(x-110, x-10), random.uniform(y-110, y-10))
    
nr = 0
for x, y in zip(poligon[0::1], poligon[1::1]):
    if is_between(x,y,punct):
        print("pe laturi")
        exit()
        
    if intersect(x,y,martor,punct):
        nr += 1

if nr % 2 == 0:
    print("in exterior")
else:
    print("in interior")
