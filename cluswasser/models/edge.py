class Edge:
    def __init__(self, src, dest, cost, vertex1, vertex2, wasser_cost=0):
        self.src = src
        self.dest = dest
        self.cost = cost
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.wasser_cost = wasser_cost
