class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] > n:
                return i
