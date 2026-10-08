class Solution:
    def rob(self, nums: list[int]) -> int:
        first = 0
        second = 0

        for money in nums:
            third = max(money + first, second)

            first = second
            second = third

        return second