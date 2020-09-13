n, m = map(int, input().split())
a = []
for _ in range(n):
  x = list(map(int, input().split()))
  a.append(x)

b = [int(input()) for i in range(m)]

for i in range(n):
  ans = 0
  for j in range(m):
    ans += a[i][j] * b[j]
  print(ans)