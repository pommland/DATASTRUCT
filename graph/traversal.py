class ListGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[] for node in nodes]

    def getIdx(self, node):
        return self.nodes.index(node)

    def addPath(self, start, end):
        self.graph[self.getIdx(start)].append(end)

    def BFT(self):
        q = []
        out = []
        q.append(self.nodes[0])
        visited = []

        while q:
            s = q.pop(0)
            out.append(s)

            for neigh in self.graph[self.getIdx(s)]:
                if not neigh in visited:
                    q.append(neigh)
                    visited.append(neigh)

        return out

    def DFTutil(self, v, visited):
        visited.append(v)
        for neigh in self.graph[self.getIdx(v)]:
            if not neigh in visited:
                visited = self.DFTutil(neigh, visited)
        return visited

    def DFT(self):
        return self.DFTutil(self.nodes[0], [])

if __name__ == '__main__':
    g = ListGraph(['A', 'B', 'C', 'D', 'E', 'F'])
    g.addPath('A', 'B')
    g.addPath('A', 'C')
    g.addPath('A', 'E')
    g.addPath('B', 'D')
    g.addPath('B', 'E')
    g.addPath('B', 'F')
    g.addPath('C', 'F')
    print(g.BFT())
    print(g.DFT())