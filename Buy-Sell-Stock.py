class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in (prices):
            if i < buy_price:
                buy_price = i
            else :
                profit = max(profit, i - buy_price)
        return profit

sol = Solution()
result = sol.maxProfit([7,1,5,3,6,4])
print(result)
