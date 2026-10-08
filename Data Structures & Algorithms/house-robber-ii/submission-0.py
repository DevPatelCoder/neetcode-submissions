class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            first = 0
            second = 0

            for money in houses:
                third = max(money + first, second)

                first = second
                second = third

            return second

        # Case 1: Skip the first house
        case1 = rob_linear(nums[1:])

        # Case 2: Skip the last house
        case2 = rob_linear(nums[:-1])

        return max(case1, case2)