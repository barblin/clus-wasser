class Cluster:
    def __init__(self, identity, sz, new_label, features, old_label):
        self.identity = identity
        self.sz = sz
        self.new_label = new_label
        self.costs = []
        self.features = []
        self.features.extend(features)
        self.old_label = old_label
        self.unified_ids = set([])
        self.unified_ids.add(identity)

    def merge(self, other):
        self.sz += other.sz
        self.costs.extend(other.costs)
        self.unified_ids.add(other.identity)
        self.unified_ids.update(other.unified_ids)
        self.features.extend(other.features)

    def clone(self):
        clone = Cluster(self.identity, self.sz, self.new_label, self.features.copy(), self.old_label)
        clone.costs = self.costs.copy()
        clone.unified_ids = self.unified_ids.copy()
        return clone


class UnionFind:
    def __init__(self, features, labels):
        size = len(features)
        self.feature_size = 0

        if 0 < size:
            self.feature_size = len(features[0])

        self.max_features = [0] * self.feature_size
        self.size = size
        self.num_components = size
        self.offset = 0

        self.clusters = [None] * size
        for i in range(0, size):
            for j in range(0, self.feature_size):
                if self.max_features[j] < features[i][j]:
                    self.max_features[j] = features[i][j]

            self.clusters[i] = Cluster(i, 1, -1, [features[i]], labels[i])

    def connected(self, p, q):
        return self.find_root_elem(p) == self.find_root_elem(q)

    def find_root_elem(self, p):
        root = p
        while root != self.clusters[root].id:
            root = self.clusters[root].id

        while p != root:
            next_el = self.clusters[p].id
            self.clusters[p].id = root
            p = next_el

        return root

    def unify(self, p, q, w_cost):
        root1 = self.find_root_elem(p)
        root2 = self.find_root_elem(q)

        if root1 == root2:
            return

        if self.clusters[root1].sz < self.clusters[root2].sz:
            self.clusters[root2].merge(self.clusters[root1])
            self.clusters[root2].costs.append(float(w_cost))

            self.clusters[root1].id = root2
        else:
            self.clusters[root1].merge(self.clusters[root2])
            self.clusters[root1].costs.append(float(w_cost))

            self.clusters[root2].id = root1

        self.num_components = self.num_components - 1
