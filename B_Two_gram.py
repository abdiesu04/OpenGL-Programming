from collections import defaultdict


n =int(input())
s = input()
mapp = defaultdict(int)
for i in range(n-1):
    mapp[s[i]+s[i+1]] += 1

res  = ''
mx = 0
for k , v in mapp.items():
    if v > mx:
        mx = v
        res = k
print(res)
