class Solution(object):
    def isPalindrome(self, x):
        arr = ""
        rev = (str(x))[::-1]
        for digit in str(rev):
            arr += digit
        if str(arr) == str(x):
            return True
        else:
            return False
        
col = Solution()
result = col.isPalindrome(121)
print(result)
