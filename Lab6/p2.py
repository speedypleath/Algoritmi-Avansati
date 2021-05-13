f = open("p2.in")

n = int(f.readline())
poligon = [None] * n
for i in range(n):
    poligon[i] = tuple(float(x) for x in f.readline().split(" "))
    
x = poligon.index(min(poligon))
reverse = False
for i in range(x + 1, n + x):
    if not reverse and poligon[i % n][0] < poligon[(i - 1) % n][0]:
        reverse = True
    elif reverse and poligon[i % n][0] > poligon[(i - 1) % n][0]:
        print("Poligonul nu este x monoton")
        break
else:
    print("Poligonul este x monoton")
    
y = poligon.index(min(poligon, key = lambda x: x[1]))
reverse = False
for i in range(y + 1, n + y):
    if not reverse and poligon[i % n][1] < poligon[(i - 1) % n][1]:
        reverse = True
    elif reverse and poligon[i % n][1] > poligon[(i - 1) % n][1]:
        print("Poligonul nu este y monoton")
        break
else:
    print("Poligonul este y monoton")