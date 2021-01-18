import math

a, b, C = map(float, input().split())

S = a * b * math.sin(math.radians(C)) / 2
L = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))) + a + b
h = b * math.sin(math.radians(C))
print(f"{S:.5f}")
print(f"{L:.5f}")
print(f"{h:.5f}")
