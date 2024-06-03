t =  int(input())
for _ in range(t):
    n , c = map(int , input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()()))

    left , right = 1 , arr[-1]

    def helper(minDistance):
        cows = 1
        distance  = 0
        for i in range(1,len(arr)):
            if distance >= minDistance:
                cows += 1
                distance = 0
            else:
                distance += arr[i] - arr[i-1]
        return cows >= c


    while left <= right:
        mid = left + (right - left) // 2
        if helper(mid):
            left     = mid
        else:
            right = mid  - 1

    print(left)



