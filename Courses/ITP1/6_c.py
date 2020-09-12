n = int(input())
d = {
  1: [[0] * 10, [0] * 10, [0] * 10],
  2: [[0] * 10, [0] * 10, [0] * 10],
  3: [[0] * 10, [0] * 10, [0] * 10],
  4: [[0] * 10, [0] * 10, [0] * 10]
}

for i in range(n):
  b, f, r, v = map(int, input().split())
  d[b][f-1][r-1] += v
  if d[b][f-1][r-1] < 0:
    d[b][f-1][r-1] = 0

for i in range(1, 5):
  print(" " + " ".join(map(str, d[i][0])), " " + " ".join(map(str, d[i][1])), " " + " ".join(map(str, d[i][2])), sep="\n")
  if i == 4:
    break
  print("#" * 20)