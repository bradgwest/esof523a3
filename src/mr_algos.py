"""
AUTHOR: Brad West
---
DESCRIPTION: Metamorphic testing of 4 graph algorithms. The algorithms are:

    1. Depth First Search
    2. Breadth First Search
    3. Minimum Spanning Tree (Prim's Algorithm)
    4. Minimum Spanning Tree (Kruskal's Algorithm)

For each algorithm, metamorphic relations are developed and tested using the python
unittest library.

Metamorphic Relations:
    1. For all algorithms, adding the same edges in reverse cannot make the solution
       longer for MST, and cannot make the solution shorter for DFS and BFS.
    2. For all algorithms, adding a single edge cannot make the number of items in the
       solution less (in the case of DFS and BFS, this is the number of nodes,
       traversed to find the target, for the MST algorithms this is the combined
       edge weight)
    3. For a complete graph, removing an edge should not make the solution for DFS and
       BFS longer, or the MST algos smaller.
"""

import unittest
import networkx as nx
from random import randint, seed
import copy


def add_random_edge_weights(graph):
    wt_range = (1, 100)
    for edge in list(graph.edges):
        wt = randint(wt_range[0], wt_range[1])
        graph.add_edge(edge[0], edge[1], weight=wt)


class TestMR1(unittest.TestCase):

    def add_reverse_edges(self, graph):
        for edge in list(graph.edges):
            graph.add_edge(
                edge[1], edge[0],
                weight=graph.get_edge_data(edge[0], edge[1])["weight"])

    def setUp(self):
        """
        Generate random sized directed graphs. Size varies from 2 to 1000
        :return:
        """
        seed(23)
        n_node_range = (2, 100)
        n_graphs = 20
        self.primary = [None for _ in range(0, n_graphs)]
        self.followup = [None for _ in range(0, n_graphs)]
        for i in range(0, n_graphs):
            n_nodes = randint(n_node_range[0], n_node_range[1])
            self.primary[i] = nx.generators.directed.gn_graph(n_nodes)
            add_random_edge_weights(self.primary[i])
            self.followup[i] = copy.deepcopy(self.primary[i])
            self.add_reverse_edges(self.followup[i])


    def test_dfs(self):
        """
        Run DFS and verify that the list of edges returned for the followup
        case is not longer than the primary case.

        :return:
        """
        for i in range(0, len(self.primary)):
            src = list(self.primary[i].out_edges)[0][0] # Choose a node that has at least degree one
            primary = list(nx.dfs_edges(self.primary[i], source=src))
            followup = list(nx.dfs_edges(self.followup[i], source=src))
            self.assertGreaterEqual(len(list(followup)), len(list(primary)))

    def test_bfs(self):
        for i in range(0, len(self.primary)):
            src = list(self.primary[i].out_edges)[0][0] # Choose a node that has at least degree one
            primary = list(nx.bfs_edges(self.primary[i], source=src))
            followup = list(nx.bfs_edges(self.followup[i], source=src))
            self.assertGreaterEqual(len(list(followup)), len(list(primary)))

    def test_prim(self):
        """
        MST does not work for undirected graph

        :return:
        """
        for i in range(0, len(self.primary)):
            primary = nx.algorithms.tree.minimum_spanning_edges(
                self.primary[i].to_undirected(), algorithm='prim', data=False)
            followup = nx.algorithms.tree.minimum_spanning_edges(
                self.followup[i].to_undirected(), algorithm='prim', data=False)
            self.assertGreaterEqual(len(list(primary)), len(list(followup)))

    def test__kruskal(self):
        """
        Must make the graph undirected, first

        :return:
        """
        for i in range(0, len(self.primary)):
            primary = nx.algorithms.tree.minimum_spanning_edges(
                self.primary[i].to_undirected(), algorithm='kruskal', data=False)
            followup = nx.algorithms.tree.minimum_spanning_edges(
                self.followup[i].to_undirected(), algorithm='kruskal', data=False)
            self.assertGreaterEqual(len(list(primary)), len(list(followup)))


class TestMR2(unittest.TestCase):

    def setUp(self):
        seed(23)
        self.n_node_range = (2, 100)
        n_graphs = 20
        self.primary = [None for _ in range(0, n_graphs)]
        self.followup = [None for _ in range(0, n_graphs)]
        for i in range(0, n_graphs):
            n_nodes = randint(self.n_node_range[0], self.n_node_range[1])
            self.primary[i] = nx.complete_graph(n_nodes)
            add_random_edge_weights(self.primary[i])
            self.followup[i] = copy.deepcopy(self.primary[i])
            # Add edge to node zero. Node is one more than range
            self.followup[i].add_edge(self.n_node_range[1] + 1, 0, weigth=1)

    def test_dfs(self):
        for i in range(0, len(self.primary)):
            primary = list(nx.dfs_edges(self.primary[i], source=0))
            followup = list(nx.dfs_edges(self.followup[i], source=self.n_node_range[1] + 1))
            self.assertGreaterEqual(len(list(followup)), len(list(primary)))

    def test_bfs(self):
        for i in range(0, len(self.primary)):
            primary = list(nx.bfs_edges(self.primary[i], source=0))
            followup = list(nx.bfs_edges(self.followup[i], source=self.n_node_range[1] + 1))
            self.assertGreaterEqual(len(list(followup)), len(list(primary)))

    def test_prim(self):
        for i in range(0, len(self.primary)):
            primary = nx.algorithms.tree.minimum_spanning_edges(
                self.primary[i], algorithm='prim', data=False)
            followup = nx.algorithms.tree.minimum_spanning_edges(
                self.followup[i], algorithm='prim', data=False)
            self.assertEqual(len(list(followup)) + 1, len(list(primary)))

    def test__kruskal(self):
        for i in range(0, len(self.primary)):
            primary = nx.algorithms.tree.minimum_spanning_edges(
                self.primary[i], algorithm='kruskal', data=False)
            followup = nx.algorithms.tree.minimum_spanning_edges(
                self.followup[i], algorithm='kruskal', data=False)
            self.assertEqual(len(list(followup)) + 1, len(list(primary)))


class TestMR3(unittest.TestCase):

    def setUp(self):
        pass

    def test_dfs(self):
        # Run dfs primary, reverse edge directions, run dfs secondary, assert that output is the same
        pass

    def test_bfs(self):
        pass

    def test_prim(self):
        pass

    def test__kruskal(self):
        pass