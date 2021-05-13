import numpy as np
f = open("p1.in")

p = tuple(float(x) for x in f.readline().split())
q = tuple(float(x) for x in f.readline().split())
r = tuple(float(x) for x in f.readline().split())

a = np.array([[1, 1, 1], 
              [p[0], q[0], r[0]], 
              [p[1], q[1], r[1]]
              ]) 

det = np.linalg.det(a)

if det < 0:
    print("viraj la dreapta")
elif det == 0:
    print("puncte coliniare")
else:
    print("viraj la stanga")