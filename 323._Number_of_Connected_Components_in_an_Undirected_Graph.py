class Solution:
    def dfs(self, i, adj_list, visited):
        visited[i] = True
        for neighbor in adj_list[i]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0
        visited = [False] * n
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj_list[u].append(v)
            adj_list[v].append(u)
        for i in range(n):
            if not visited[i]:
                cc += 1
                self.dfs(i, adj_list, visited)
        return cc
