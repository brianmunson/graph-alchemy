# graph-alchemy

Coding exercise in building a package to encode basic algebraic 
operations on graphs (undirected, directed, and weighted) which 
are defined by sets of edges.

Let S be a set. For the purpose of this exercise, S is the set of 
all hashable and pickleable objects in Python.

Definition: For a set X, let X* be the quotient of X x X by the 
action (a, b) -> (b, a).

Note: X* is the set of all subsets of X of size at most 2. The 
subsets of size 1 are the diagonal, which is canonically
identifiable with X.

Definition: A _graph over S_ is a pair (V, E) where E is a
subset of S* and V is the set of all elements v of S where v is in
e for some e in E.

Note: Traditionally V is a subset of S and E is a subset of V*.
The current definition does not, for example, allow for a graph
with a single vertex but no edges. This definition is used to 
honor the spirit of this exercise, which is to implement graphs 
defined by edges.

Definition: A _directed graph over S_ is a pair (V, E) where
E is a subset of S x S, and V is the set of all elements v of S 
such that v is in the image of one of the projection maps 
S x S -> S.

Definition: A _weighted graph over S_ is a graph G = (V, E) 
together with a map w : E --> R (the real numbers). The target 
of w can be any totally ordered set with addition.

Definition: A _path_ in a graph G is a sequence of edges 
e_i = (s_i, t_i) i=0..n of G such that t_i = s_{i+1} for 
i=0..n-1. For a weighted graph with weight function w, we define
the _weight_ of the path to be the sum of w(e_i) for i=0..n.

Note: A path has an underlying graph defined by its set of edges.

# Requirements

## General

- [ ] demonstrate use of continuous integration pipeline
- [ ] installable via pip
- [ ] documented API
- [/] have tests
- [/] follow PEP8

## API

### All graphs

- [x] represent data via edges
- [ ] use a database to hold graph data using at most three tables
- [ ] use SQLAlchemy ORM model to abstract interactions with the 
database
- [/] valid vertices are any Python objects which are *hashable* 
and *pickelable*
- [ ] library objects should be persistable and recoverable 
between sessions
- [x] `order` (number of vertices) and `size` (number of edges) 
properties
- [x] support `append` and `extend` to add edges to a graph
- [x] support graph union through `+` operator
- [x] support graph difference through `-` operator
- [x] support graph intersection through `*` operator
- [x] `vertices` property to return vertices as a generator
- [x] `disjoint` property to return disjoint subgraphs as a 
generator
- [x] `repr` method
- [x] support for `in` (inclusion) to check if an edge is in a 
graph
- [x] support for iteration over edges
- [ ] preserve vertex type on extraction
- [x] `adjacency_matrix` property to return list of vertices and 
numpy matrix 
- [x] `connects` method to determine if a graph connects two (or 
more) vertices

### Directed graphs

### Weighted graphs

- [x] graph union should have edge weight equal to sum of edge 
weights
- [x] `weight` property to return overall weight of the graph
- [x] method to compute weight between two connected vertices

## Notes/TODOs

- docs make target requires `raml2html`, `raml2md`, and 
`markdown-pdf` to generate API docs from raml.

- it would be nice to define an Edge class and use that to
type check (hashability, pickleability) and enforce structure.
However, it needs to implement `__eq__`, but this makes the class 
unhashable and therefore we would not be able to use sets to store
edges for graphs. current workaround is to validate edges on
instantiation of graph, which feels slightly incorrect.

- unclear on preservation of vertex type on extraction

- disjoint and connected components: currently incorrectly
implemented. the notion of a path generates an equivalence
relation that effectively forces bidirectionality in the graph
to define connected components. that is, "disjoint" for any 
given graph is the same as the (undirected) graph it generates.

- computing weight between two connected vertices is not 
well-defined except in a tree. instead we can talk about the
weight of a path connecting two vertices. then the "weight" 
between two vertices in a graph might be the path(s) of least
weight.


- Disjoint: is there a cute way to compute these with the 
adjacency matrix by thinking about Markov procsses?

- [ ] rewrite tests given refactor
- [ ] do as much db stuff as possible