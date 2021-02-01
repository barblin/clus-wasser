from collections import OrderedDict


def reduce_to_significant(uf, barrier=200):
    labels = uf.clusters.copy()
    labels.sort(key=lambda x: x.sz, reverse=True)

    j = 0
    cluster_dict = OrderedDict()
    for i in range(0, len(labels)):
        cluster = labels[i].clone()
        if cluster.identity not in cluster_dict.keys() and cluster.sz >= barrier:
            cluster.new_label = j
            cluster_dict[cluster.identity] = cluster
            j += 1

        if j == 8:
            break

    return cluster_dict
