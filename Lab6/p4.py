import numpy

f = open("p4.in")
epsilon = 0.00001
def viraj(a,b,c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])

puncte = [None] * 4
for i in range(4):
    puncte[i] = tuple(float(x) for x in f.readline().split(" "))
    
if viraj(*puncte[:3]) > 0:
    a = numpy.array([[puncte[0][0], puncte[0][1], puncte[0][0] ** 2 + puncte[0][1] ** 2, 1],
                    [puncte[1][0], puncte[1][1], puncte[1][0] ** 2 + puncte[1][1] ** 2, 1],
                    [puncte[2][0], puncte[2][1], puncte[2][0] ** 2 + puncte[2][1] ** 2, 1],
                    [puncte[3][0], puncte[3][1], puncte[3][0] ** 2 + puncte[3][1] ** 2, 1]])
else:
    a = numpy.array([[puncte[2][0], puncte[2][1], puncte[2][0] ** 2 + puncte[2][1] ** 2, 1],
                [puncte[1][0], puncte[1][1], puncte[1][0] ** 2 + puncte[1][1] ** 2, 1],
                [puncte[0][0], puncte[0][1], puncte[0][0] ** 2 + puncte[0][1] ** 2, 1],
                [puncte[3][0], puncte[3][1], puncte[3][0] ** 2 + puncte[3][1] ** 2, 1]])

det = numpy.linalg.det(a)
if abs(det) < epsilon:
    print("ambele triangulari sunt legale")
    exit()
elif det > 0:
    print("muchia AC este ilegala")
else:
    print("muchia AC este legala")
    
if viraj(*puncte[1:]) > 0:
    a = numpy.array([[puncte[3][0], puncte[3][1], puncte[3][0] ** 2 + puncte[3][1] ** 2, 1],
                    [puncte[0][0], puncte[0][1], puncte[0][0] ** 2 + puncte[0][1] ** 2, 1],
                    [puncte[1][0], puncte[1][1], puncte[1][0] ** 2 + puncte[1][1] ** 2, 1],
                    [puncte[2][0], puncte[2][1], puncte[2][0] ** 2 + puncte[2][1] ** 2, 1]])
else:
    a = numpy.array([[puncte[1][0], puncte[1][1], puncte[1][0] ** 2 + puncte[1][1] ** 2, 1],
                    [puncte[0][0], puncte[0][1], puncte[0][0] ** 2 + puncte[0][1] ** 2, 1],
                    [puncte[3][0], puncte[3][1], puncte[3][0] ** 2 + puncte[3][1] ** 2, 1]
                    [puncte[2][0], puncte[2][1], puncte[2][0] ** 2 + puncte[2][1] ** 2, 1]])

det = numpy.linalg.det(a)
if abs(det) < epsilon:
    print("ambele triangulari sunt legale")
    exit()
elif det > 0:
    print("muchia BD este ilegala")
else:
    print("muchia BD este legala")