class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {i:[] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node):
            if node is visit:
                return
            
            visit.add(node)

            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        
        dfs(0)

        return len(visit) == n
                

           