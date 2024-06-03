from typing import Counter


t = int(input())
for _ in range(t):
    n ,  m  = map(int , input().split())
    s = input()
    mapp = {"A":0,'B':0,'C':0,"D":0,"E":0,"F":0,"G":0}
    for char in s:
        mapp[char] += 1
    cnt = 0
    # print(mapp)
    for val in mapp.values():
        if m - val > 0:
            cnt += m - val
    print(cnt)

    