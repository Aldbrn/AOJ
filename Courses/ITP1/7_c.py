r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]
ans = [[0] * (c + 1) for _ in range(r + 1)]

for i in range(r):
    for j in range(c):
        ans[i][j] = a[i][j]
        ans[i][j + 1] = sum(a[i])

for i in range(c + 1):
    for j in range(r):
        ans[r][i] += ans[j][i]

for i in ans:
    print(*i)
