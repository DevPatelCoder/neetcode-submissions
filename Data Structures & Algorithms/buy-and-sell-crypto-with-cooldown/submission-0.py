class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)

        memo = [[-1] * 2 for _ in range(n)]

        def dfs(i, canBuy):

            if i >= n:
                return 0

            if memo[i][canBuy] != -1:
                return memo[i][canBuy]

            if canBuy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)

                memo[i][canBuy] = max(buy, skip)

            else:
                sell = prices[i] + dfs(i + 2, True)
                hold = dfs(i + 1, False)

                memo[i][canBuy] = max(sell, hold)

            return memo[i][canBuy]

        return dfs(0, True)