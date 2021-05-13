import numpy

f = open("p3.in")
epsilon = 0.00001
def viraj(a,b,c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])

triunghi = [None] * 3
for i in range(3):
    triunghi[i] = tuple(float(x) for x in f.readline().split(" "))
punct = tuple(float(x) for x in f.readline().split(" "))

if viraj(*triunghi) > 0:
    a = numpy.array([[triunghi[0][0], triunghi[0][1], triunghi[0][0] ** 2 + triunghi[0][1] ** 2, 1],
                    [triunghi[1][0], triunghi[1][1], triunghi[1][0] ** 2 + triunghi[1][1] ** 2, 1],
                    [triunghi[2][0], triunghi[2][1], triunghi[2][0] ** 2 + triunghi[2][1] ** 2, 1],
                    [punct[0], punct[1], punct[0] ** 2 + punct[1] ** 2, 1]])
else:
    a = numpy.array([[triunghi[2][0], triunghi[2][1], triunghi[2][0] ** 2 + triunghi[2][1] ** 2, 1],
                [triunghi[1][0], triunghi[1][1], triunghi[1][0] ** 2 + triunghi[1][1] ** 2, 1],
                [triunghi[0][0], triunghi[0][1], triunghi[0][0] ** 2 + triunghi[0][1] ** 2, 1],
                [punct[0], punct[1], punct[0] ** 2 + punct[1] ** 2, 1]])

det = numpy.linalg.det(a)
if abs(det) < epsilon:
    print("pe cerc")
elif det > 0:
    print("in interior")
else:
    print("in exterior")