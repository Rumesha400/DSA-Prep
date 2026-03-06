class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        temp = {}
        for char in s:
            if char not in temp:
                temp[char] = 1
            else :
                temp[char] += 1
        for char in t:
            if char not in temp :
                return False
            else :
                temp[char] -= 1
                if temp[char] < 0:
                    return False
        return True

        
sol = Solution()
result = sol.isAnagram("anagram", "nagaram")
print(result)
