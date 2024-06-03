
t = int(input())
for _ in range(t):
    l , r = map(int , input().split())
    cnt  = 0
    while r >= 1:
        r /= 2
        cnt += 1
    print(cnt-1)
