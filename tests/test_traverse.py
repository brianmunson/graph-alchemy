import pytest
from graph_alchemy import Edge, BaseGraph
from graph_alchemy.traverse import (
    all_paths,
    find_path,
    neighborhood,
    connected_component,
)

def test_neighborhood():
    edges = [Edge(0, 1)]
    g = BaseGraph(edges)
    assert neighborhood(g, 0) == g
    assert neighborhood(g, 1) == BaseGraph()

def test_connected_component():
    edge0 = Edge(0,1)
    edge1 = Edge(2,3)
    edges = [edge0, edge1]
    g = BaseGraph(edges)
    assert connected_component(g, 0) == BaseGraph([edge0])
    assert connected_component(g, 2) == BaseGraph([edge1])

