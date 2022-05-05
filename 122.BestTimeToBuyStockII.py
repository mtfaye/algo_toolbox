class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        anchor, i = 0, 0
        
        for i in range(len(prices)):
            profit = prices[i] - prices[anchor]
            if  profit > 0:
                total += profit
            anchor = i 
  
        return total 
