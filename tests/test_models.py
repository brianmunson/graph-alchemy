import pytest
from graph_alchemy import Graph, Edge

def test_edge():
    source = "a"
    target = "b"
    edge = Edge(source=source, target=target)
    assert edge.source == source
    assert edge.target == target
    assert edge.edge == (source, target)


def test_unhashable_edge():
    source = {}
    target = "a"
    with pytest.raises(ValueError):
        Edge(source=source, target=target)


def test_unpicklable_edge():
    # TODO implement
    pass


def test_empty_graph():
    graph = Graph()
    assert graph.edges == set()
    # TODO test vertices


def test_nonempty_graph():
        edges = [Edge(i, i + i) for i in range(3)]
        graph = Graph(edges)
        assert graph.edges == set([(i, i+ i) for i in range(3)])
        assert graph.order == 4
        # TODO test vertices
        assert graph.order == 4
        assert graph.size == 3


def test_append():
    graph = Graph()
    edge = Edge("a","b")
    graph.append(edge)
    assert graph.edges == set(edge.edge)


def test_extend():
    graph = Graph()
    edges = [Edge(i, i + 1) for i in range(2)]
    graph.extend(edges)
    assert graph.edges == set([(i, i + 1) for i in range(2)])


def test_add():
    graph0 = Graph([Edge(0,1)])
    graph1 = Graph([Edge(1,2)])
    sum_graph = graph0 + graph1
    assert sum_graph.edges == set([Edge(i, i + 1) for i in range(2)])


def test_subtract():
    graph = Graph([Edge(0,1)])
    zero_graph = graph - graph
    assert zero_graph.edges == set()


def test_intersection():
    graph0 = Graph([Edge(i, i + 1) for i in range(2)])
    graph1 = Graph([Edge(0,1)])
    graph2 = Graph([Edge("a", "b")])
    graph01 = graph0 * graph1
    graph02 = graph0 * graph2
    assert graph01.edges == set((0,1))
    assert graph02.edges == set()


def test_contains():
    edge = Edge(0,1)
    non_edge = Edge("a", "b")
    graph = Graph([edge])
    assert edge in graph.edges
    assert non_edge not in graph.edges


def test_adjancency_matrix():
    # TODO implement
    pass


def test_disjoint():
    graph0 = Graph([Edge(0,1), Edge(2,3)])
    components = []
    for g in graph0.disjoint():
        components.append(g)
    assert len(components) == 2
