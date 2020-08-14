import pytest
from graph_alchemy import (
    Edge, 
    Graph, 
    WeightedGraph, 
    DirectedGraph
)


def test_adjancency_matrix():
    # TODO implement
    pass


def test_disjoint():
    graph0 = Graph([Edge(0,1), Edge(2,3)])
    components = []
    for g in graph0.disjoint():
        components.append(g)
    assert len(components) == 2
