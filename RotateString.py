class Solution(object):
    def rotateString(self, s, goal):
        dummy = ""
        if (len(s) != len(goal)):
            return False
        else:
            dummy = s + s
            if goal in dummy:
                return True
            else:
                return False
ans = Solution()
result = ans.rotateString("abcde", "cdeab")
print(result)  
