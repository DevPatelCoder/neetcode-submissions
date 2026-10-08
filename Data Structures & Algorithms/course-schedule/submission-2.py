from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course, path):
            if course in path:
                return False

            if not graph[course]:
                return True

            path.add(course)

            for next_course in graph[course]:
                if not dfs(next_course, path):
                    return False

            path.remove(course)

            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True