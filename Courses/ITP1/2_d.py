W, H, x, y, r = map(int, input().split())

if x < 0 or y < 0:
    print("No")
elif x+r > W:
    print("No")
elif y+r > H:
    print("No")
else:
    print("Yes")