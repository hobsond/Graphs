from queue import Queue
from util import Stack
class Graph:
    def __init__(self):
        self.vertices = {}
    def addVert(self,vId):
        self.vertices[vId] = set()
    def addEnds(self,v1,v2):
        self.vertices[v1].add(v2)
    def getNeighbors(self,vId):
        return self.vertices[vId]
    
    def bft(self,start):
        q = Queue()
        q.put(start)
        visited=set()
        
        while q.qsize() >0:
            current = q.get()
            if current not in visited:
                visited.add(current)
                print(current)
                x = self.getNeighbors(current)
                for i in x:
                    q.put(i)
    def dft(self,start):
        stack = Stack()
        stack.push(start)
        visited = set()
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                x = self.getNeighbors(current)
                for i in x:
                    stack.push(i)
   
    def dfr(self,v,visited):
        visited.add(v)
        x = self.getNeighbors(v)
        
        print(v)
        for i in x:
            if i not in visited:
                self.dfr(i,visited)
            
            
            
                
        # print(v)
    def dft_recursive(self,start):
        
        visited =set()
        self.dfr(start,visited)




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


g.dft_recursive('e')
print()

# g.bft('e')
g.dft('e')