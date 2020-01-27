import sys


class Vertex (object):
    def __init__(self,name):
        self.name =name
        self.visited=False
        self.predecessor=None
        self.adjacenciesList=[]
        self.minDistance=sys.maxsize

    def __cmp__(self,otherVertex):
        return self.cmp(self.minDistance,otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority =self.minDistance
        otherPrioity=other.minDistance
        return selfPriority < otherPrioity


class Edge(object):
    def __init__(self,weght,startVertex,targetVertex):
        self.weigh =weght
        self.startvertex=startVertex
        self.targetVertex=targetVertex




