
class MyTestCase(unittest.TestCase):
    def test_tree_is_sorted_in_right_order(self):
        tree = DistanceTree([[1, 2], [3, 2], [7, 8]])
        edge1 = Edge(1, 2, 10, [], [])
        edge2 = Edge(2, 1, 4, [], [])
        edge3 = Edge(2, 3, 1, [], [])
        edge4 = Edge(1, 3, 99, [], [])

        tree.add_edge(edge1)
        tree.add_edge(edge2)
        tree.add_edge(edge3)
        tree.add_edge(edge4)

        tree.sort()

        self.assertEqual([edge3, edge2, edge1, edge4], tree.edges, "Is supposed to be sorted")

    def test_tree_is_sorted_in_right_order_pass_edges(self):
        edge1 = Edge(1, 2, 10, [], [])
        edge2 = Edge(2, 1, 4, [], [])
        edge3 = Edge(2, 3, 1, [], [])
        edge4 = Edge(1, 3, 99, [], [])

        tree = DistanceTree([[1, 2], [3, 2], [7, 8]], [edge1, edge2, edge3, edge4])
        tree.sort()

        self.assertEqual([edge3, edge2, edge1, edge4], tree.edges, "Is supposed to be sorted")

    def test_create_tree(self):
        features = load_file("skinnyDipData_0.csv")
        tree = create_tree(features)
        tree.wasser_cost_calc()

        self.assertEqual(3000, tree.number_vertices, "Tree is supposed to have all data points")
        self.assertEqual(15849, len(tree.edges), "Tree is supposed to contain all edges")
        self.assertEqual(0, tree.min_wasser, "Min wasser is supposed to be updated")
        self.assertEqual(0.6324680244383981, tree.max_wasser, "Max wasser is supposed to be updated")

    def test_sorted_by_wasser_cost(self):
        features = load_file("skinnyDipData_0.csv")
        tree = create_tree(features)
        tree.wasser_cost_calc()
        tree.sort_wasser()

        last = 0

        for edge in tree.edges:
            self.assertTrue(last <= edge.wasser_cost, "Tree is supposed to be sorted by wasser cost")
            last = edge.wasser_cost

    def test_sorted_by_eucledian_cost(self):
        features = load_file("skinnyDipData_0.csv")
        tree = create_tree(features)
        tree.sort()

        last = 0
        for edge in tree.edges:
            self.assertTrue(last <= edge.cost, "Tree is supposed to be sorted by wasser cost")
            last = edge.cost

    def test_same_amount_of_neighbours(self):
        features = load_file("skinnyDipData_0.csv")
        tree = create_tree(features)

        for edge in tree.edges:
            self.assertEqual(200, len(tree.neighbours[edge.src]), "All vertices should have same amount of neighbours")
            self.assertEqual(200, len(tree.neighbours[edge.dest]), "All vertices should have same amount of neighbours")


if __name__ == '__main__':
    unittest.main()
