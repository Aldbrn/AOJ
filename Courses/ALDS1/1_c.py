def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i <= (x ** 0.5):
        if x % i == 0:
            return False
        i += 2
    return True


n = int(input())

l = []
for _ in range(n):
    x = int(input())
    l.append(isPrime(x))
print(l.count(True))
