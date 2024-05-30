grid = []
for i in range(5):
    arr = list(map(int , input().split()))
    grid.append(arr)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            print(abs(2-i) + abs(2-j))
            break