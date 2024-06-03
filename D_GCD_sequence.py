from math import gcd

def valid(a):
    n = len(a)
    g = [0] * (n-1)
    for i in range(n-1):
        g[i] = gcd(a[i], a[i+1])
    for i in range(1, n-1):
        if g[i] < g[i-1]:
            return False
    return True

def solve(ttc):
    n = int(input())
    a = list(map(int, input().split()))
    g = [0] * (n-1)
    for i in range(n-1):
        g[i] = gcd(a[i], a[i+1])
    idx = -1
    for i in range(1, n-1):
        if g[i] < g[i-1]:
            idx = i
            break
    if idx == -1:
        print("YES")
        return
    for j in range(idx-1, idx+2):
        v = [a[i] for i in range(n) if i != j]
        if valid(v):
            print("YES")
            return
    print("NO")

ttc = int(input())
for _ in range(ttc):
    solve(_)