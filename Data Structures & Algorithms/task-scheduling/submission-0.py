class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Step 1: Count frequency of each task
        count = {}

        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1

        # Step 2: Put frequencies into Max-Heap
        heap = []

        for frequency in count.values():
            heap.append(frequency)

        heapq.heapify_max(heap)

        # Step 3: Queue for tasks in cooldown
        # (remaining_frequency, available_time)
        queue = deque()

        time = 0

        # Continue while there are available or cooling tasks
        while heap or queue:

            time += 1

            # Step 4: Move cooled-down task back to heap
            if queue and queue[0][1] == time:
                frequency, available_time = queue.popleft()
                heapq.heappush_max(heap, frequency)

            # Step 5: Execute the most frequent available task
            if heap:
                frequency = heapq.heappop_max(heap)

                # One occurrence is completed
                frequency -= 1

                # If more occurrences remain,
                # put the task into cooldown
                if frequency > 0:
                    queue.append(
                        (frequency, time + n + 1)
                    )

        return time