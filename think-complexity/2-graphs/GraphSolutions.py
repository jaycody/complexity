#!/usr/bin/env python -tt

""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

"""
Modified by: Cesar de la Vega
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Gets edge from the graph given two vertices.

        If it doesn't exist returns None
        """
        try:
            return self[v][w]
        except:
            return None

    def remove_edge(self, e):
        """Removes all references to a given edge in the graph
        """
        try:
            del self[e[0]][e[1]]
            del self[e[1]][e[0]]
        except:
            raise ValueError, 'No edge like that was found.'

    def vertices(self):
        """Returns a list with all the vertices
        """
        return self.keys()

    def edges(self):
        """Returns a list with all the edges
        """
        es = set()
        for v in self.vertices():
            for w in self[v]:
                e = self.get_edge(v, w)
                if e not in es:
                    es.add(e)
        
        return list(es)

    def out_vertices(self, v):
        """Takes a vertex and returns a list of the adjacent vertices
        """
        connected_to = self[v]
        return list(connected_to.keys())

    def out_edges(self, v):
        """Takes a vertex and returns a list of the edges connected to it
        """
        es = set()
        connected_to = self[v]
        for w in connected_to:
            e = self.get_edge(v, w)
            if e not in es:
                es.add(e)

        return list(es)

    def add_all_edges(self):
        """Takes all vertices and adds edges between all pairs of them
        """
        from itertools import combinations
 
        vs = self.vertices()
        pairs = [list(x) for x in combinations(vs, 2)]
        for p in pairs:
            e = Edge(p[0], p[1])
            self.add_edge(e)



def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g

    print "Edges: %s" % g.edges()
    e = g.get_edge(v, w)
    print e
    g.remove_edge(e)
    print "Edges: %s" % g.edges()
    print g.get_edge(v, w)
    print g.vertices()

    g.add_edge(e)
    z = Vertex('z')
    g.add_vertex(z)
    print g
    e2 = Edge(v, z)
    g.add_edge(e2)
    print e2
    print g
    print "Nodes connected to v: %s" % g.out_vertices(v)
    print "Edges connected to v: %s" % g.out_edges(v)
    g.remove_edge(e)
    g.remove_edge(e2)
    print g
    g.add_all_edges()
    print g

if __name__ == '__main__':
    import sys
    main(*sys.argv)
