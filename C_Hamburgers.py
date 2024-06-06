def solve():
    s = input()
    s_c  = [s.count("B"),s.count("S") , s.count("C")]
    al  = list(map(int , input().split()))
    pr  = list(map(int , input().split()))
    su = int(input())

    left  = 0
    right = 10 ** 166
    while left < right:
        v = 0
        mid = left + (right - left) // 2
        for i in range(3):
            v += max(0 , (mid * s_c[i] - al[i]) * pr[i])
        if v > su:
            right  = mid
        else:
            left = mid + 1
    print(left-1)
solve()
        