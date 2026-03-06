class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for digit in nums:
            if digit not in temp:
                temp[digit] = 1
            else :  
                return True
        return False
sol = Solution()
result = sol.containsDuplicate([1,2,3,1])
print(result)
