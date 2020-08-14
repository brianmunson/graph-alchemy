import pytest
from graph_alchemy import Edge, BaseGraph

# TODO load fixtures from conftest to reduce redundancy

def test_edge():
    source = "a"
    target = "b"
    edge = Edge(source=source, target=target)
    assert edge.source == source
    assert edge.target == target
    assert edge.weight == 0.0


def test_weighted_edge():
    source = "a"
    target = "b"
    weight = 2.1
    edge = Edge(source=source, target=target, weight=weight)
    assert edge.source == source
    assert edge.target == target
    assert edge.weight == weight


def test_empty_graph():
    graph = BaseGraph()
    assert graph.edges == set()


def test_unhashable_edge():
    source = set()
    target = "b"
    edge = Edge(source=source, target=target)
    with pytest.raises(ValueError):
        BaseGraph([edge])


def test_unpickleable_edge():
    # FIXME
    pass


def test_nonempty_graph():
    edges = [Edge(i, i + 1) for i in range(3)]
    graph = BaseGraph(edges)
    assert graph.edges == set([Edge(i, i+ 1) for i in range(3)])


def test_vertices():
    edges = [Edge(i, i + 1) for i in range(3)]
    graph = BaseGraph(edges)
    vertices = []
    for i in graph.vertices:
        vertices.append(i)
    assert len(vertices) == 4


def test_order():
    edges = [Edge(i, i + 1) for i in range(3)]
    graph = BaseGraph(edges)
    assert graph.order == 4


def test_size():
    edges = [Edge(i, i + 1) for i in range(3)]
    graph = BaseGraph(edges)
    assert graph.size == 3


def test_append():
    graph = BaseGraph()
    edge = Edge(source="a",target="b")
    graph.append(edge)
    assert graph.edges == set([edge])


def test_extend():
    graph = BaseGraph()
    edges = [Edge(i, i + 1) for i in range(2)]
    graph.extend(edges)
    assert graph.edges == set([Edge(i, i + 1) for i in range(2)])


def test_add():
    graph0 = BaseGraph([Edge(0,1)])
    graph1 = BaseGraph([Edge(1,2)])
    sum_graph = graph0 + graph1
    assert sum_graph.edges == set([Edge(i, i + 1) for i in range(2)])


def test_subtract():
    graph = BaseGraph([Edge(0,1)])
    zero_graph = graph - graph
    assert zero_graph.edges == set()


def test_intersection():
    graph0 = BaseGraph([Edge(i, i + 1) for i in range(2)])
    graph1 = BaseGraph([Edge(0,1)])
    graph2 = BaseGraph([Edge("a", "b")])
    graph01 = graph0 * graph1
    graph02 = graph0 * graph2
    assert graph01.edges == set([Edge(0,1)])
    assert graph02.edges == set()


def test_contains():
    edge = Edge(0,1)
    non_edge = Edge("a", "b")
    graph = BaseGraph([edge])
    assert edge in graph.edges
    assert non_edge not in graph.edges


def test_equals():
    g = BaseGraph([Edge("a", "b")])
    h = BaseGraph([Edge("a", "b")])
    assert g == h


def test_not_equals():
    g = BaseGraph()
    h = BaseGraph([Edge("a", "b")])
    assert g != h

