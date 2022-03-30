from Graph import Graph
from networkx.generators.random_graphs import erdos_renyi_graph

class Test:
    def __init__(self, Graph):
        self.Graph = Graph

    def compute_time(self, n, p):

        for _ in range(1, 4):
            V = erdos_renyi_graph(n, p)
            G = self.Graph
            
            for edge in V.edges:
                print(edge)
                G.add_edge(edge[0], edge[1])
            
            print(G.BFS(0))


MyGraph = Graph()
MyTest = Test(MyGraph)

MyTest.compute_time(8, 0.5)
