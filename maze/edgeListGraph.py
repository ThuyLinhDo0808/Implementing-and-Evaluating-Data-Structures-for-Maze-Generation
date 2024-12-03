# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.edges = []  # List to store edges
        self.vertices = set()  # Set to store unique vertices


        
    def addVertex(self, label:Coordinates):
        """Add a single vertex to the graph."""
        if label not in self.vertices:
            self.vertices.add(label)



    def addVertices(self, vertLabels:List[Coordinates]):
        """Add multiple vertices to the graph."""
        for label in vertLabels:
            self.addVertex(label)  # Reuse addVertex method for simplicity



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        """Add an edge between two vertices. Return True if successful."""
        if vert1 in self.vertices and vert2 in self.vertices and not self.hasEdge(vert1, vert2):
            self.edges.append((vert1, vert2, addWall))
            return True
        return False
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        """Update the wall status between two vertices. Return True if successful."""
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2):
                self.edges[i] = (v1, v2, wallStatus)
                return True
        return False



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """Remove the edge between two vertices. Return True if successful."""
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2):
                del self.edges[i]
                return True
        return False
        


    def hasVertex(self, label:Coordinates)->bool:
        """Check if the vertex exists in the graph."""
        return label in self.vertices



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """Check if an edge exists between two vertices."""
        return any((v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2) for v1, v2, _ in self.edges)



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """Get the wall status between two vertices. Return False if the edge does not exist."""
        for v1, v2, wall in self.edges:
            if (v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2):
                return wall
        return False
        


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        """Return a list of all vertices connected to the given vertex."""
        neighbours = []
        for v1, v2, _ in self.edges:
            if v1 == label:
                neighbours.append(v2)
            elif v2 == label:
                neighbours.append(v1)
        return neighbours
        