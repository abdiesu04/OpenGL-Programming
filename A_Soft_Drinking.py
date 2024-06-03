class Solution:
    def floorSqrt(self, x,n):
        if x < 2:
            return x
        best  = -1
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid ** n == x:
                best = mid
                left = mid + 1
            else:
                right = mid

        return best
    
sol = Solution()
x , n = map(int , input().split())
print(sol.floorSqrt(x,n))