def selectionSort(a, n):
    ans = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if a[i] > a[minj]:
            a[i], a[minj] = a[minj], a[i]
            ans += 1
    print(*a)
    print(ans)


n = int(input())
a = list(map(int, input().split()))

selectionSort(a, n)
