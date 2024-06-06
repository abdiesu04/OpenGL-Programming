import sys

def input():
    return sys.stdin.readline().strip()

def split_to_int(s):
    return [int(x) for x in s.split()]

def transpose(mat):
    n = len(mat)
    t = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = mat[j][i]
    return t

def sol():
    n, m = map(int , input().split())
    grid1 = [split_to_int(input()) for _ in range(n)]
    grid2 = [split_to_int(input()) for _ in range(n)]

    if n == m:
        stt = set(tuple(sorted(row)) for row in grid1)
        # print(stt)
        for row in grid2:
            if tuple(sorted(row)) not in stt:
                print("NO")
                return
        grid1 = transpose(grid1)
        grid2 = transpose(grid2)
        stt = set(tuple(sorted(row)) for row in grid1)
        for row in grid2:
            if tuple(sorted(row)) not in stt:
                print("NO")
                return
        print("YES")
    else:
        stt = set(tuple(sorted(row)) for row in grid1)
        for row in grid2:
            if tuple(sorted(row)) not in stt:
                print("NO")
                return
        stt = set(tuple(sorted(col)) for col in zip(*grid1))
        for col in zip(*grid2):
            if tuple(sorted(col)) not in stt:
                print("NO")
                return
        print("YES")

t = int(input())
for _ in range(t):
    sol()


