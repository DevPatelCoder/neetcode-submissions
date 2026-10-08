class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequency
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into their frequency bucket
        for num, frequency in count.items():
            buckets[frequency].append(num)

        # Get top k
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result