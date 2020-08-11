from queue import Queue,LifoQueue
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
   
    def dfs(self,start,target):
        q = Queue()
        q.put((start,[start]))
        while q.qsize() > 0:
            (v, path) = q.get()
            for i in self.vertices[v]:
                if i == target:
                    return path + [i]
                else:
                    q.put((i,path+[i]))
                    
    def bfs(self,start,target):
        q = LifoQueue()
        q.put((start,[start]))
        while q.qsize() > 0:
            (v, path) = q.get()
            for i in self.vertices[v]:
                if i == target:
                    return path + [i]
                else:
                    q.put((i,path+[i]))
    
                
                    
            

    def dfs_recursive(self, starting_vertex,target,visited=None,path=None):
        # sets the initialized to a set if it is the first instance 
        if visited is None:
            visited = set()
        # initializes a array if its the first recurssion
        if path is None:
            path = []
        # makes a copy of the path so that it can mutable, and add the current node to the array>>
        path = path +[starting_vertex]
        # adds the current node  to visited
        visited.add(starting_vertex)
        # if the current node is the target return the path
        if starting_vertex == target:
            return path
        # Gets the neighbors of the current node
        for i in self.getNeighbors(starting_vertex):
            # if the neighbor has not already been visited 
            if i  not in visited:
                # set a varaible for the recursive soloution so the 
                # path does not consistently rewrite itself 
                new_path = self.dfs_recursive(i,target,visited,path)
                # i
                if new_path is not None:
                    return new_path
        return None
        
        


g = Graph()

g.addVert("a")

g.addVert(1)
g.addVert(2)
g.addVert(3)
g.addVert(4)
g.addVert(5)
g.addVert(6)

g.addEnds(1,2)
g.addEnds(1,4)

g.addEnds(2,3)
g.addEnds(2,5)

g.addEnds(3,6)

g.addEnds(4,3)
# g.addEnds(4,6)

# g.dft_recursive('e')
print(g.dfs_recursive(1,5))

# g.bft('e')
# g.dft('e')