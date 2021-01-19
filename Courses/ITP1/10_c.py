import math

while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s) / n
    ans = 0
    for i in s:
        ans += (i - m) ** 2 / n
    print(f"{math.sqrt(ans):.5f}")
