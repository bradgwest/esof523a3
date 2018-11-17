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
    1. For all algorithms, reversing the edge directions should not change the output
    2. For all algorithms, adding an edge cannot make the number of items in the
       solution less (in the case of DFS and BFS, this is the number of nodes,
       traversed to find the target, for the MST algorithms this is the combined
       edge weight)
    3. For a complete graph, removing an edge should not make the solution for DFS and
       BFS longer, or the MST algos smaller.
"""

import unittest
import networkx as nx
import matplotlib.pyplot as plt

class TestMR1(unittest.TestCase):

    def setUp(self):
        self.g_forward = nx.DiGraph()
        self.g_backward = nx.DiGraph()
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


class TestMR2(unittest.TestCase):

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