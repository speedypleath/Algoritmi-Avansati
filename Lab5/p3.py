import numpy as np
f = open("p3.in")

def determina_viraj(p, q, r):
    a = np.array([[1, 1, 1], 
              [p[0], q[0], r[0]], 
              [p[1], q[1], r[1]]
              ]) 

    det = np.linalg.det(a)

    return np.sign(det)
    
punct = tuple(float(x) for x in f.readline().split())
poligon = [tuple(map(int, linie.split(' '))) for linie in f.read().split('\n')]

prev_pozitie = None

for x, y in zip(poligon[0::2], poligon[1::2]):
    if punct == x or punct == y:
        print("pe laturi")
        exit()
    
    pozitie = determina_viraj(punct, x, y)
    if pozitie == 0:
        print("pe laturi")
        exit()

    if prev_pozitie is not None and prev_pozitie != pozitie:
        print("inauntru")
        exit()
    
    prev_pozitie = pozitie

print("inafara")