import math
import sys

from scipy.spatial.qhull import Delaunay
from scipy.stats import wasserstein_distance
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import RobustScaler

from cluswasser.models.edge import Edge
from cluswasser.models.vertex import Vertex


class DistanceTree:
    def __init__(self, features, edges=[]):
        self.features = features
        self.edges = []
        self.neighbours = {}
        self.number_vertices = len(features)
        self.min_wasser = sys.maxsize
        self.max_wasser = 0

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge):
        if edge.src == edge.dest:
            return

        if edge.wasser_cost < self.min_wasser:
            self.min_wasser = edge.wasser_cost

        if self.max_wasser < edge.wasser_cost:
            self.max_wasser = edge.wasser_cost

        self.edges.append(edge)

    def calc_neighbours(self, neighs=200):
        scaled_data = RobustScaler().fit_transform(self.features)

        knn = NearestNeighbors(n_neighbors=neighs, algorithm='ball_tree').fit(scaled_data)
        distances, indices = knn.kneighbors(scaled_data)

        for i in range(0, len(distances)):
            self.neighbours[i] = distances[i].tolist()

    def sort(self):
        self.edges.sort(key=lambda x: x.cost)

    def sort_wasser(self):
        self.edges.sort(key=lambda x: x.wasser_cost)

    def wasser_cost_calc(self):
        for edge in self.edges:
            self.__calc_wasser_dist(edge)

    def __calc_wasser_dist(self, edge):
        if not self.neighbours[edge.src] or not self.neighbours[edge.dest]:
            edge.wasser_cost = -1
        else:
            edge.wasser_cost = wasserstein_distance(self.neighbours[edge.src],
                                                    self.neighbours[edge.dest])

            if edge.wasser_cost < self.min_wasser:
                self.min_wasser = edge.wasser_cost

            if self.max_wasser < edge.wasser_cost:
                self.max_wasser = edge.wasser_cost


def create_tree(features, neighs=200):
    tri = Delaunay(features)
    tree = DistanceTree(features)

    for entries in tri.simplices:
        row = []
        for entry in entries:
            row.append(features[entry].tolist())

        dist1 = math.dist(row[0], row[1])
        dist2 = math.dist(row[0], row[2])
        dist3 = math.dist(row[1], row[2])

        edge1 = Edge(entries[0], entries[1], dist1, Vertex(row[0]), Vertex(row[1]))
        edge2 = Edge(entries[0], entries[2], dist2, Vertex(row[0]), Vertex(row[2]))
        edge3 = Edge(entries[1], entries[2], dist3, Vertex(row[1]), Vertex(row[2]))

        tree.add_edge(edge1)
        tree.add_edge(edge2)
        tree.add_edge(edge3)

    tree.calc_neighbours(neighs)

    return tree
