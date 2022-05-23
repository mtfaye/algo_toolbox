# using extra memory space:
# Space = O(n)
# Time = O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = []
        anchor = i = 0
        
        for i in range(len(prices)):
            if prices[i] - prices[anchor] <= 0:
                anchor = i
            ans.append(prices[i] - prices[anchor])
        return max(ans)


# Space = O(1)
# Time = O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        anchor = 0
        max_profit = 0
        
        for i in range(len(prices)):
            profit = prices[i] - prices[anchor]
            
            if profit <= 0:
                anchor = i
            max_profit = max(max_profit, profit)
            
        return max_profit
