class Solution(object):
    def findMin(self, nums):
        min = nums[0]
        for i in nums:
            if ((i < i+1) & (i <= min)):
                min = i
        return min
sol = Solution()
result = sol.findMin([3,4,5,1,2])
