d = {
  "S": [0]*13,
  "H": [0]*13,
  "C": [0]*13,
  "D": [0]*13
}
suit = ["S", "H", "C", "D"]

n = int(input())
for _ in range(n):
  s, r = input().split()
  d[s][int(r)-1] = 1

for i in suit:
  for j in range(13):
    if d[i][j] == 0:
      print(i, j+1)