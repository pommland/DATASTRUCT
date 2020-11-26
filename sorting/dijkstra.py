class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[ 0 for i in range(vertices) ] for j in range(vertices)]

    def minDistance(self, dist, checked):
        min = 99999

        for v in range(self.V):
            if dist[v] < min and not checked[v]:
                min = dist[v]
                min_i = v

        return min_i
        
    def dijkstra(self, src):
        dist = [99999] * self.V
        dist[src] = 0
        checked = [False] * self.V

        for p in range(self.V):
            p = self.minDistance(dist, checked)
            checked[p] = True
            
            for v in range(self.V):
                if self.graph[p][v] > 0 and not checked[v] and dist[v] > dist[p] + self.graph[p][v]:
                    dist[v] = dist[p] + self.graph[p][v]

        self.printSolution(dist)

    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node])

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
g.dijkstra(0)