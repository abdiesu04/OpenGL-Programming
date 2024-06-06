def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Binary search to find the maximum number of cookies
    left, right = 0, sum(b) + k
    while left <= right:
        mid = (left + right) // 2
        can_bake = 0
        for i in range(n):
            can_bake += (b[i] + min(a[i] - 1, k)) // a[i]
        if can_bake >= mid:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(solve())