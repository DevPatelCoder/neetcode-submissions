class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]

            seen[nums[i]] = i