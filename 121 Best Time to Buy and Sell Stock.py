class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        CN = prices[0]
        CS = 0
        for i in range(len(prices)):
            if prices[i] - CN > CS:
                CS = prices[i] - CN
            if prices[i] < CN:
                CN = prices[i]
        return CS