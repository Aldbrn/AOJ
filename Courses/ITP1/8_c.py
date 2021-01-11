import sys

s = sys.stdin.read().lower()
letters = "abcdefghijklmnopqrstuvwxyz"

for c in letters:
    n = s.count(c)
    print(f"{c} : {n}")
