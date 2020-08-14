from __future__ import annotations
from typing import Any, Set, List, Tuple, Iterable, Dict
from collections import defaultdict
import numpy as np
from graph_alchemy.traverse import connected_component, find_path, all_paths
from . import Edge, BaseGraph


# TODO unhashable due to __eq__ implementation
# class WeightedEdge(Edge):
#     edge: Edge
#     weight: float

#     def __init__(self, source: Any, target: Any, weight: float):
#         super().__init__(source, target)
#         self.weight = weight

#     @property
#     def repr(self):
#         return (self.source, self.target, self.weight)

#     def __eq__(self, E: WeightedEdge) -> bool:
#         return (self.source == E.source) and (self.target == E.target) and (self.weight == E.weight)


class DirectedGraph(BaseGraph):
    # TODO possibly Graph inherits from this?
    # then the init for Graph would look like adding all reflections of edges
    edges: Set[Tuple]

    def __init__(self, edges_iter: Iterable[Edge]=()):
        super().__init__(edges_iter)

    def disjoint(self):
        visited_edges = []
        for edge in self.edges:
            if edge not in visited_edges:
                visited_edges.append(edge)
                yield connected_component(self, edge.source)

    def adjacency_matrix(self) -> (Dict[Any, int], np.ndarray):
        # FIXME requirements says return list of vertices
        # we return vertex hash instead because it gives a way
        # to index into the adjacency matrix by vertex
        vertex_hash = {}
        for i, vertex in enumerate(self.vertices):
            vertex_hash[vertex] = i
        # vertices = list(vertex_hash.keys())
        order = self.order
        adjacency_matrix = np.zeros((order, order))
        for edge in self.edges:
            source_ix = vertex_hash[edge.source]
            target_ix = vertex_hash[edge.target]
            adjacency_matrix[source_ix, target_ix] = 1
        return vertex_hash, adjacency_matrix

    def connects(self, start_vertex: Any, end_vertex: Any) -> bool:
        g = find_path(self, start_vertex, end_vertex)
        if len(g.edges) == 0:
            return False
        return True


class Graph(DirectedGraph):
    # TODO would be nicer to inherit from BaseGraph
    # perhaps implementing more methods on BaseGraph to turn it 
    # into DirectedGraph and then go from there
    edges: Set[Tuple]

    def __init__(self, edges_iter: Iterable[Edge]=()):
        # TODO inelegant: need cleaner way to force edge reflection
        new_iter = []
        for edge in edges_iter:
            new_iter.append(edge)
            new_iter.append(Edge(edge.target, edge.source))
        super().__init__(new_iter)

    
class WeightedGraph(Graph):
    # TODO again with too much inheritance

    def __init__(self, edges_iter: Iterable[Edge]=()):
        super().__init__(edges_iter)

    def __add__(self, G: WeightedGraph) -> WeightedGraph:
        #TODO feels kludgy and opaque
        weight_dict = defaultdict(float)
        for edge_set in [self.edges, G.edges]:
            for edge in edge_set:
                weight = edge.weight
                base_edge = Edge(source=edge.source, target=edge.target)
                weight_dict[base_edge] += weight
        new_edges = []
        for edge, weight in weight_dict.items():
            new_edges.append(Edge(edge.source, edge.target, weight))
        return WeightedGraph(new_edges)

    def weight(self):
        total = 0
        for edge in self.edges:
            total += edge.weight
        return total

    def least_weight_path(self, start_vertex: Any, end_vertex: Any) -> WeightedGraph:
        valid_paths = all_paths(self, start_vertex, end_vertex)
        valid_paths = sorted(valid_paths, key=lambda x: x.weight)
        return valid_paths[0]