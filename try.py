class Graph:
    def __init__(self):
        self.vertices = {}
    def addVert(self,vId):
        self.vertices[vId] = set()
    def addEnds(self,v1,v2):
        self.vertices[v1].add(v2)
    def getNeighbors(self,vId):
        return self.vertices[vId]




g = Graph()

g.addVert("a")

g.addVert("b")
g.addVert("c")
g.addVert("d")
g.addVert("e")
g.addVert("f")

g.addEnds('a','d')
g.addEnds('a','b')
g.addEnds('a','c')

g.addEnds('c','d')
g.addEnds('c','a')

g.addEnds('d','e')
g.addEnds('d','f')

g.addEnds('e','c')
g.addEnds('f','b')


print(g.getNeighbors('c'))
