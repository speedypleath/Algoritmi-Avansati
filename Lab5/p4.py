import numpy as np
f = open("p2.in")

def determina_viraj_stanga(p, q, r):
    a = np.array([[1, 1, 1], 
              [p[0], q[0], r[0]], 
              [p[1], q[1], r[1]]
              ]) 

    det = np.linalg.det(a)

    if det > 0:
        return True
    else:
        return False

def determina_acoperire(puncte, n):
    li = [puncte[0], puncte[1]]
    ls = [puncte[0], puncte[1]]
    for i in range(2, n):
        while len(li) >= 2 and not determina_viraj_stanga(li[-2], li[-1], puncte[i]):
            li.pop()
        while len(ls) >= 2 and determina_viraj_stanga(ls[-2], ls[-1], puncte[i]):
            ls.pop()
        li.append(puncte[i])
        ls.append(puncte[i])
        
    rez = li
    rez.extend(ls[1:-1])
    return rez


n = int(f.readline())
puncte = [tuple(map(int, linie.split(' '))) for linie in f.read().split('\n')]

acoperire = determina_acoperire(puncte, n)
set_acoperire = set(acoperire)
set_puncte = set(puncte)
for punct in set_puncte - set_acoperire:
    for i in range(len(acoperire)):
        min = 0
        j = (i + 1) % (len(acoperire) - 1)
        

    