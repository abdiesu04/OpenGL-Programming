from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))

    error = defaultdict(int)
    correct = defaultdict(int)
    correct1 = defaultdict(int)

    for i in range(n):
        if a[i] != b[i]:
            error[b[i]] += 1
        else:
            correct1[b[i]] += 1

    for i in range(m):
        correct[d[i]] += 1

    flag = True
    total_error = 0
    for num, count in error.items():
        if count > correct[num]:
            flag = False
            break
        else:
            total_error += count

    if m - total_error > 0:
        for num, count in correct1.items():
            if not correct[num]:
                flag = False
                break

    print("YES" if flag else "NO")

t = int(input())
for _ in range(t):
    solve()