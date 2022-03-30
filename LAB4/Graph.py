from collections import defaultdict
import numpy as np

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def BFS(self, s):
       visited = [False] * (max(self.graph) + 1)
       queue = []

       queue.append(s)
       visited[s] = True

       while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


    def DFS_helper(self, v, visited):
        visited.add(v)
        print(v, end = " ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS_helper(neighbour, visited)


    def DFS(self, v):
        visited = set()
        self.DFS_helper(v, visited)

