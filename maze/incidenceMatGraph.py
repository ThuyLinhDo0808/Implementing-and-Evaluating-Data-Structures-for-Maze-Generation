# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        """Initialize the incidence matrix graph."""
        self.vertices = []
        self.edges = []
        self.incidence_matrix = []



    def addVertex(self, label:Coordinates):
        """Add a vertex to the graph."""
        if label not in self.vertices:
            self.vertices.append(label)
            for row in self.incidence_matrix:
                row.append(0)  # Add a new column for the new vertex



    def addVertices(self, vertLabels:List[Coordinates]):
        """Add multiple vertices to the graph."""
        for label in vertLabels:
            self.addVertex(label)



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        """Add an edge between two vertices. Return True if successful."""
        if vert1 in self.vertices and vert2 in self.vertices:
            v1_index = self.vertices.index(vert1)
            v2_index = self.vertices.index(vert2)
            new_edge = [0] * len(self.vertices)
            new_edge[v1_index] = 1
            new_edge[v2_index] = 1
            self.edges.append((vert1, vert2, addWall))
            self.incidence_matrix.append(new_edge)
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
                del self.incidence_matrix[i]
                return True
        return False
        


    def hasVertex(self, label:Coordinates)->bool:
        """Check if a vertex exists in the graph."""
        return label in self.vertices



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """Check if an edge exists between two vertices."""
        for v1, v2, _ in self.edges:
            if (v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2):
                return True
        return False



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """Get the wall status between two vertices. Return False if the edge does not exist."""
        for v1, v2, wall in self.edges:
            if (v1, v2) == (vert1, vert2) or (v2, v1) == (vert1, vert2):
                return wall
        return False



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        """Return a list of all vertices connected to the given vertex."""
        neighbours = []
        if label in self.vertices:
            v_index = self.vertices.index(label)
            for edge in self.incidence_matrix:
                if edge[v_index] == 1:
                    for i, connection in enumerate(edge):
                        if connection == 1 and i != v_index:
                            neighbours.append(self.vertices[i])
        return neighbours
        