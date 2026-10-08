class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [-1] * len(s)

        def dfs(i):

            # Reached the end
            if i == len(s):
                return 1

            # 0 cannot be decoded by itself
            if s[i] == "0":
                return 0

            # Already calculated
            if memo[i] != -1:
                return memo[i]

            # Take one digit
            ways = dfs(i + 1)

            # Take two digits
            if i + 1 < len(s):
                number = int(s[i:i + 2])

                if 10 <= number <= 26:
                    ways += dfs(i + 2)

            memo[i] = ways

            return ways

        return dfs(0)