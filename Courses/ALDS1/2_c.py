def bubbleSort(c, n):
    for _ in range(n):
        for i in range(n - 1, 0, -1):
            if int(c[i][1]) < int(c[i - 1][1]):
                c[i], c[i - 1] = c[i - 1], c[i]


def selectionSort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        if int(c[i][1]) > int(c[minj][1]):
            c[i], c[minj] = c[minj], c[i]


n = int(input())
c1 = input().split()
c2 = c1[:]

bubbleSort(c1, n)
selectionSort(c2, n)
print(*c1)
print("Stable")
print(*c2)
if c1 == c2:
    print("Stable")
else:
    print("Not stable")
