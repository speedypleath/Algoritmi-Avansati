fin = open('inputP1', 'r')
k = int(fin.readline())
v = [int(x) for x in fin.readline().split()]
n = len(v) + 1
dp = [[0] * (k+1) for i in range(n)]

for i in range(n):
    dp[i][0] = 1


for i in range(1, n):
    for j in range(1, k+1):
        if j < v[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = 1 if dp[i-1][j-v[i-1]] == 1 else dp[i-1][j]

for i in range(k, 0, -1):
    if dp[n-1][i] == 1:
        print(i)
        break

