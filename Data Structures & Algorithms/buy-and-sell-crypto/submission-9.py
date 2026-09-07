class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximize prices[j] - prices[i] such that i < j
        
        profit = 0

        for i in range(1, len(prices)):
            buy = min(prices[:i])
            curprof = prices[i] - buy
            if curprof > profit:
                profit = curprof
        
        return profit



        