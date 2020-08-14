from typing import Any, List
from . import BaseGraph, Edge

# TODO too much repetitive code here. needs some abstraction

def neighborhood(graph: BaseGraph, vertex: Any) -> BaseGraph:
    """
    Returns the neighbohood graph of a given vertex, which 
    is the subgraph generated by the set of edges which have
    the vertex as its source.
    """
    edges = []
    for edge in graph.edges:
        if edge[0] == vertex:
            edges.append(edge)
    return BaseGraph(edges)


def connected_component(graph: BaseGraph, vertex: Any) -> BaseGraph:
    # TODO this does not but should check if the vertex is
    # in the graph in the first place!
    """
    Breadth-first search. Returns set of vertices for which
    there exists a path from the given vertex. A path from v
    to w is an ordered list of edges {(s_i,t_i)}, i=0..n 
    such that s_0 = v, t_n = w, and t_i = s_{i+1} for i=0..n-1
    """
    visited_vertices = []
    component_edges = []
    queue = [vertex]
    while queue:
        current_vertex = queue.pop(0)
        if current_vertex not in visited_vertices:
            visited_vertices.append(current_vertex)
            neighborhood_graph = neighborhood(graph, current_vertex)
            neighbors = neighborhood_graph.vertices
            edges = neighborhood_graph.edges
            queue.extend(list(neighbors))
            component_edges.extend(edges)
    return BaseGraph(component_edges)


def find_path(graph: BaseGraph, start_vertex: Any, end_vertex: Any) -> BaseGraph:
    # TODO might reduce redundancy to make this a part of connected_component
    # by passing an optional ending vertex
    """
    Returns a graph whose edges comprise the path between two vertices,
    if one exists.

    By the nature of the algorithm this finds the shortest path
    between two vertices as measured by the number of edges. 
    However, for a weighted graph, we might define the weight of 
    a path to be the total weight of the subgraph it represents.
    """
    if start_vertex == end_vertex:
        loop = Edge(start_vertex, end_vertex)
        if loop in graph:
            return BaseGraph([loop])
        else:
            return BaseGraph()
    visited_vertices = []
    path_queue = [[start_vertex]]
    while path_queue:
        current_path = path_queue.pop(0)
        current_path_end = current_path[-1]
        if current_path_end not in visited_vertices:
            neighborhood_graph = neighborhood(graph, current_path_end)
            neighbors = neighborhood_graph.vertices
            for neighbor in neighbors:
                new_path = list(current_path)
                new_path.append(neighbor)
                path_queue.append(new_path)
                if neighbor == end_vertex:
                    return new_path
            visited_vertices.append(current_path_end)
    return BaseGraph()

def all_paths(graph: BaseGraph, start_vertex: Any, end_vertex: Any) -> List[BaseGraph]:
    """
    Returns a list of BaseGraph each of which represents a unique
    path from start_vertex to end_vertex. Used for finding the path
    of least weight between vertices in a weighted graph.

    Implementation: basically find path, only do not return and
    record those 
    """
    valid_paths = []
    if start_vertex == end_vertex:
        loop = Edge(start_vertex, end_vertex)
        if loop in graph:
            valid_paths.append(BaseGraph([loop]))
    visited_vertices = []
    path_queue = [[start_vertex]]
    while path_queue:
        current_path = path_queue.pop(0)
        current_path_end = current_path[-1]
        if current_path_end not in visited_vertices:
            neighborhood_graph = neighborhood(graph, current_path_end)
            neighbors = neighborhood_graph.vertices
            for neighbor in neighbors:
                new_path = list(current_path)
                new_path.append(neighbor)
                path_queue.append(new_path)
                if neighbor == end_vertex:
                    valid_paths.append(new_path)
            visited_vertices.append(current_path_end)
    return valid_paths
