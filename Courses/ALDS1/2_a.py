def bubbleSort(a, n):
    ans = 0
    for _ in range(n):
        for i in range(n - 1, 0, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                ans += 1
    print(*a)
    print(ans)


n = int(input())
a = list(map(int, input().split()))

bubbleSort(a, n)
