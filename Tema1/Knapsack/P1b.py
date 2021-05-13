import operator

fin = open('inputP1', 'r')
k = int(fin.readline())

mx = 0

for x in fin.readline().split():
    x = int(x)

    mx += x
    if mx < k:
        mx -= x

    mx = max(mx, x)
print(mx)
