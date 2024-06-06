t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res , cnt = 0 , 0
    for i in reversed(range(n)):
        if s[i] == "B":
            cnt += 1
        else:
            res += cnt
            cnt = min(1 , cnt)
    print(res)
