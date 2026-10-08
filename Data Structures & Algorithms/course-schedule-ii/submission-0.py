class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1

        queue = deque()

        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
        result = []
        while queue:
            course = queue.popleft()

            result.append(course)

            for next_course in graph[course]:
                indegree[next_course]-=1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        if len(result)!= numCourses:
            return[]
        return result