import time

import numpy as np

from cluswasser.cluster_wasser import cluster
from cluswasser.models.range import WasserIncrement
from cluswasser.tree import create_tree, DistanceTree
from cluswasser.union_find import UnionFind


def wasser_range(features, range_from, range_until, range_step, labels=[], neighs=200, edges=[]):
    tree = __compute_tree(features, neighs, edges)
    union_find = UnionFind(features, labels)
    return __wasser_range(tree, union_find, range_from, range_until, range_step)


def __wasser_range(tree, union_find, range_from, range_until, range_step):
    overall_time = time.time()
    start_time = overall_time

    samples = np.arange(range_from, range_until, range_step)
    increments = [None] * len(samples)
    cur = 0

    for i in samples:
        cluster_data = cluster(union_find, tree, i)

        time_inc = time.time() - start_time
        full_time_inc = time.time() - overall_time
        increments[cur] = WasserIncrement(i, cluster_data, time_inc, full_time_inc)
        start_time = time.time()
        cur += 1

    return increments


def wasser(features, wasser_margin, labels=[], neighs=200, edges=[]):
    start_time = time.time()
    tree = __compute_tree(features, neighs, edges)
    union_find = UnionFind(features, labels)
    cluster_data = cluster(union_find, tree, wasser_margin)
    time_inc = time.time() - start_time

    return WasserIncrement(wasser_margin, cluster_data, time_inc, time_inc)


def __compute_tree(features, neighs=200, edges=[]):
    if 0 < len(edges):
        return DistanceTree(features, edges)

    return create_tree(features, neighs)
