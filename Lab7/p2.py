f = open("p2.in")
x, y = map(float, f.readline().split())
n = int(f.readline())
semiplane = [None] * n
for i in range(n):
    semiplane[i] = tuple(float(k) for k in f.readline().split())
f.close()

def is_inside(semiplan):
    a, b, c = semiplan
    if a == 0:
        if b < 0:
            return y > -c/b 
        else:
            return y < -c/b
    else:
        if a < 0:
            return x > -c/a 
        else:
            return x < -c/a

filtered = filter(is_inside, semiplane)


y_min = float('-Inf')
x_min = float('-Inf')
y_max = float('Inf')
x_max = float('Inf')

for a, b, c in filtered:
    if a == 0:
        if b < 0:
            y_min = max(y_min, -c/b)
        else:
            y_max = min(y_max, -c/b)
    else:
        if a < 0:
            x_min = max(x_min, -c/a)
        else:
            x_max = min(x_max, -c/a)
            
if x_min == float('-Inf') or y_min == float('-Inf') or x_max == float('Inf') or y_max == float('Inf'):
    print("(a) nu exista un dreptunghi cu proprietatea ceruta.")
else:
    print("(a) exista un dreptunghi cu proprietatea ceruta, (b) valoarea minima a ariilor dreptunghiurilor cu proprietatea ceruta este {arie}."
          .format(arie = (x_max - x_min) * (y_max - y_min)))