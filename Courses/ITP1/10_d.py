n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d = [abs(x[i] - y[i]) for i in range(n)]

for p in range(1, 4):
    ans = 0
    for i in d:
        ans += i ** p
    print(f"{ans**(1/p):.5f}")

print(f"{max(d):.5f}")
