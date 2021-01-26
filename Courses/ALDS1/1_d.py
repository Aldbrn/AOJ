n = int(input())
R = [int(input()) for _ in range(n)]

maxv = R[1] - R[0]
minv = R[0]
for j in range(1, n):
    maxv = max(maxv, R[j] - minv)
    minv = min(minv, R[j])

print(maxv)
