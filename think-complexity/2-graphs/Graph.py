#!/usr/bin/env python -tt

"""j stephens  -  think complexity ch2 - graphs - problem sets - 2014 Sept

Notes:

GRAPH: 
    A graph in this exercise is a dictionary of dictionaries.
    The outer dictionary's keys are vertices whose values are themselves dictionaries.
    The inner dictionary's keys are the secondary vertices whose values are the edges
    which point back to the out dictiorary, such that


Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
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
        return 'Edge(%s, %s)\n' % (repr(self[0]), repr(self[1]))

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
        """exercise 2-2.3
        Takes two vertices and returns the edge between them, if it exists.
        Otherwise, returns None
        """
        try: 
            return self[v][w]
        except:
            return None

    def remove_edge(self, e):
        """2-2.4
        Takes an edge and removes any reference of it from the graph
        """
        try:
            del self[e[0]][e[1]]
            del self[e[1]][e[0]]
        except:
            raise ValueError('No edge of that value')

    def vertices(self):
        """2-2.5
        Return a list of all vertices
        """
        return self.keys()

    def edges(self):
        """2-2.6. Return a list of edges (in both directions)"""
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
    print
    v = Vertex('v')
#    print v
    print 
    w = Vertex('w')
#    print w

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    edgeAB = Edge(a, b)
    print "edgeAB = ", edgeAB

    print
    e = Edge(v, w)
    print e
    print 
    print "FORMAT: Graph([v,w], [e])"
    print
    g = Graph([v,w,a,b,c], [e, edgeAB])
    #g = Graph([v,w], [e])
    print g

    #2-2.3 get_edge--------------------------
    #positive 
    edge = g.get_edge(v, w)
    print "\nedge(v, w) = ", edge
    #negative case
    edgeNone = g.get_edge(v, v)
    print "\nedge(v, v) = ", edgeNone
    #----------------------------------------


    #2-2.4 remove_edge-----------------------
    #g.remove_edge(edge)
    #edgeTest = g.get_edge(v, w)
    #print "\nedge(v, w) = ", edgeTest
    #----------------------------------------


    #2-2.5 list vertices--------------------
    verticesCount = g.vertices()
    print
    print "List of all vertices in graph G:"
    for vertex in verticesCount:
        print vertex
    #---------------------------------------



    #2-2.6 list of edges-------------------
    edgeCount = g.edges()
    print 
    print "List of Edges in graph G:"
    for edge in edgeCount:
        print edge
    #--------------------------------------



    


if __name__ == '__main__':
    import sys
    main(*sys.argv)