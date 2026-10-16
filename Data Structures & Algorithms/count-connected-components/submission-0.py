class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

            return True

        for a, b in edges:
            if union(a, b):
                res -= 1

        return res