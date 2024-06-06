t = int(input())
for _ in range(t):
    s  = input()
    res = ''
    for i in range(len(s)):
        res += s[i]*2
    ans = ['']* len(res)
    l , r = 0 , len(res) -1
    for i in range(0,len(res),2):
        ans[l] = res[i]
        ans[r] = res[i+1]
        l += 1
        r -= 1
    print(''.join(ans))
