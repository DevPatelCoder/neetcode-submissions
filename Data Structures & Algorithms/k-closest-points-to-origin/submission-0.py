class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = x*x + y*y
            heap.append((distance,x,y))

        heapq.heapify_max(heap)

        while len(heap)>k:
            heapq.heappop_max(heap)

        result =[]
        
        for distance,x,y in heap:
            result.append([x,y])

        return result