class Solution(object):
    def longestCommonPrefix(self, strs):
        arr = []
        if strs and len(strs) > 0:
            strs = sorted(strs)
            first, last = strs[0], strs[-1]
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    arr.append(last[i])
                else:
                    return "".join(arr)
        return "".join(arr)
ans = Solution()
result = ans.longestCommonPrefix(["flower","flow","flight"])
print(result)
