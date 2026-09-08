class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = 100
        best_profit = 0

        for i in range(len(prices)):
            lowest_price = min(lowest_price, prices[i])
            best_profit = max(prices[i] - lowest_price, best_profit)
        
        return best_profit




        