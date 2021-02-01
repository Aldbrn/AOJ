s = input().split()

st = []
for c in s:
    if c in "+-*":
        a = st.pop()
        b = st.pop()
        st.append(str(eval(b + c + a)))
    else:
        st.append(c)

print(st[0])
