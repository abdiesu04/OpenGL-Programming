from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        def helper(divisor):
            counter = 0
            for i in range(len(nums)):
                counter  += ceil(nums[i] // divisor )
            return counter

        left , right  = 0 , max(nums)
        ans  = 1
        while left <= right:
            mid  = left + (right - left) // 2
            print(mid , helper(mid))
            if helper(mid) == threshold:
                return mid
            elif helper(mid) > threshold:
                left  = mid + 1
            else:
                right = mid - 1
        return ans
sol = Solution()
print(sol.smallestDivisor([1,2,5,9],6))