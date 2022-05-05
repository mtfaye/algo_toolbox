class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = []
        anchor = i = 0
        
        for i in range(len(prices)):
            if prices[i] - prices[anchor] <= 0:
                anchor = i
            ans.append(prices[i] - prices[anchor])
        return max(ans)
