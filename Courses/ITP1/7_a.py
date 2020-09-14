while True:
  m, f, r = map(int, input().split())
  if m == -1 and f == -1 and r == -1:
    break
  n = m + f
  if m == -1 or f == -1:
    print("F")
  elif n >= 80:
    print("A")
  elif 65 <= n < 80:
    print("B")
  elif 50 <= n < 65 or r >= 50:
    print("C")
  elif 30 <= n < 50:
    print("D")
  else:
    print("F")