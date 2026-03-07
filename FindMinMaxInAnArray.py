class Solution:
    def minmax(self, arr):
        if len(arr) < 2:
            return 0

        if len(arr) == 2:
            return min(arr[0], arr[1]), max(arr[0], arr[1])

        minn, maxx = float('inf'), float('-inf')
        for e in arr:
            if e > maxx:
                maxx = e
            if e < minn:
                minn = e

        return minn, maxx


class Tests:
    def __init__(self):
        arr = []
        s = Solution()
        assert s.minmax(arr) == 0
        arr = [1, 2, 3, 4]
        assert s.minmax(arr) == (1, 4)


t = Tests()
