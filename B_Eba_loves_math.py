t = int(input())
for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))

    res = nums[0]

    for i in range(1, n):

        res &= nums[i]
        
    print(res)