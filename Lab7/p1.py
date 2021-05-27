f = open("p1.in")
n = int(f.readline())
semiplane = [None] * n
for i in range(n):
    semiplane[i] = tuple(float(x) for x in f.readline().split())
f.close()

y_min = float('-Inf')
x_min = float('-Inf')
y_max = float('Inf')
x_max = float('Inf')

for a, b, c in semiplane:
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

if x_min > x_max or y_min > y_max:
    print("intersectia este vida.")
elif x_min != float('-Inf') and y_min != float('-Inf') and x_max != float('Inf') and y_max != float('Inf'):
    print("intersectia este nevida, marginita.")
else:
    print("intersectia este nevida, nemarginita.")
