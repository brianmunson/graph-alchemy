from __future__ import annotations
from pickle import PicklingError
from collections.abc import Hashable
from collections import Counter, namedtuple
from typing import Any, Set, List, Tuple, Iterable

# TODO no clean way to enforce hashability/pickleability of initializing objects
Edge = namedtuple("Edge", ("source", "target", "weight"), defaults=(None, None, 0.0))

# class Edge(object):
#     """
#     Edges are initialized by a source and a target
#     """
#     source: Any
#     target: Any
#     edge: Tuple

#     def __init__(self, source: Any, target: Any):
#         for vertex in (source, target):
#             if not isinstance(vertex, Hashable):
#                 # TODO more helpful way than str(object)?
#                 raise ValueError(f"Vertices must be hashable objects: {str(vertex)} is not hashable")
#         # TODO implement pickleability
#         # perhaps a try / except pickling in memory is enough, although
#         # if the try succeeds we do not want to persist the pickling in memory
#         self.source = source
#         self.target = target
#         # self.edge = (source, target) #TODO necessary convenience? danger in changing this without reinitializing

#     def reflect(self) -> Edge:
#         source = self.target
#         target = self.source
#         return Edge(source, target)
        
#     def __eq__(self, E: Edge) -> bool:
#         #TODO implementing this is necessary but makes it unhashable and 
#         # therefore unable to be added to a set of edges in a graph
#         return (self.source == E.source) and (self.target == E.target)

#     # TODO needs work
#     @property
#     def repr(self):
#         return (self.source, self.target)


class BaseGraph(object):
    """
    Graphs are initialized by an iterable of edges,
    vertices are defined by edges
    """
    edges: Set[Edge]

    def __init__(self, edges_iter: Iterable[Edge]=()):
        edges = set()
        for edge in edges_iter:
            edges.add(edge)
        self.edges = edges

    @property
    def vertices(self) -> Iterable:
        # TODO this feels less than optimal
        counter = Counter()
        for edge in self.edges:
            if not counter[edge.source]:
                counter[edge.source] += 1
                yield edge.source
            if not counter[edge.target]:
                counter[edge.target] += 1
                yield edge.target

    @property
    def order(self) -> int:
        count = 0
        for _ in self.vertices:
            count += 1
        return count

    @property
    def size(self) -> int:
        edge_set_list = [frozenset(edge) for edge in self.edges]
        edge_set_set = frozenset(edge_set_list)
        return len(edge_set_set)

    def append(self, edge: Edge):
        self.edges.add(edge)

    def extend(self, edge_iter: Iterable[Edge]):
        for edge in edge_iter:
            self.append(edge)

    def __add__(self, G: BaseGraph) -> BaseGraph:
        edges = self.edges.union(G.edges)
        return BaseGraph(edges)

    def __sub__(self, G: BaseGraph) -> BaseGraph:
        edges = self.edges.difference(G.edges)
        return BaseGraph(list(edges))

    def __mul__(self, G: BaseGraph) -> BaseGraph:
        edges = self.edges.intersection(G.edges)
        return BaseGraph(list(edges))

    def __contains__(self, E: Edge) -> bool:
        return E.edge in self.edges
    
    def __eq__(self, G: BaseGraph) -> bool:
        return self.edges == G.edges

    def repr(self):
        return f"{self.__class__.__name__}({self.edges})"

    