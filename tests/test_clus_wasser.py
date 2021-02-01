import unittest

from cluswasser.cluster import wasser_range, wasser
from tests.test_provider import load_file_features, load_file_labels


class MyTestCase(unittest.TestCase):
    def test_cluster_range_with_labels(self):
        features = load_file_features("skinnyDipData_0.csv")
        labels = load_file_labels("skinnyDipData_0.csv")
        increments = wasser_range(features, 0.0185, 0.02, 0.0003, labels, 5)

        self.assertEqual(6, len(increments), "Wasser_range should produce expected amounts of increments")

        clusters = increments[-1].clusters
        cluster = clusters[1941]

        noise_cluster = clusters[-1]
        self.assertEqual(414, cluster.sz, "Cluster size should be of correct size")
        self.assertEqual(2586, noise_cluster.sz, "Noise cluster should be of correct size")

        total_sz = 0

        for key in clusters.keys():
            total_sz += clusters[key].sz

        self.assertEqual(3000, total_sz, "The total amount of vertices should remain 3000")

    def test_cluster_with_margin(self):
        features = load_file_features("skinnyDipData_0.csv")
        labels = load_file_labels("skinnyDipData_0.csv")

        increment = wasser(features, 0.018500000000000003, labels, 5)
        clusters = increment.clusters
        cluster = clusters[1941]
        noise_cluster = clusters[-1]
        self.assertEqual(382, cluster.sz, "Cluster size should be of correct size")
        self.assertEqual(2618, noise_cluster.sz, "Noise cluster should be of correct size")

        total_sz = 0

        for key in clusters.keys():
            total_sz += clusters[key].sz

        self.assertEqual(3000, total_sz, "The total amount of vertices should remain 3000")


if __name__ == '__main__':
    unittest.main()
