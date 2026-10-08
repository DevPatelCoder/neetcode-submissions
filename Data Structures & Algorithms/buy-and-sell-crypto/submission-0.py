class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        a = 0  # Index of the best buy day so far
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[a]:
                a = i  # Found a cheaper day to buy
            else:
                current_profit = prices[i] - prices[a]
                if current_profit > max_profit:
                    max_profit = current_profit

        return max_profit