"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited=set()
        
        while q.size() >0:
            current = q.dequeue()
            if current not in visited:
                visited.add(current)
                print(current)
                x = self.get_neighbors(current)
                for i in x:
                    q.enqueue(i)
            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                x = self.get_neighbors(current)
                for i in x:
                    stack.push(i)
                
    def dfr(self,v,visited):
        visited.add(v)
        x = self.get_neighbors(v)
        
        print(v)
        for i in x:
            if i not in visited:
                self.dfr(i,visited)
    
           
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited =set()
        self.dfr(starting_vertex,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass
        q = Stack()
        q.push((starting_vertex,[starting_vertex]))
        while q:
            (v, path) = q.pop()
            for i in self.vertices[v] :
                if i == destination_vertex:
                    return path + [i]
                else:
                    q.push((i,path+[i]))

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Queue()
        q.enqueue((starting_vertex,[starting_vertex]))
        while q.size() > 0:
            (v, path) = q.dequeue()
            for i in self.vertices[v]:
                if i == destination_vertex:
                    return path + [i]
                else:
                    q.enqueue((i,path+[i]))

    def dftr(self,v,path,target):
            if v == target:
                return path
                
            for i in self.vertices[v] :
                self.dftr(i,path+[i],target)
            return path
        
    def dfs_recursive(self, starting_vertex, destination_vertex,visited=None,path=None):
        
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
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
        if starting_vertex == destination_vertex:
            return path
        # Gets the neighbors of the current node
        for i in self.get_neighbors(starting_vertex):
            # if the neighbor has not already been visited 
            if i  not in visited:
                # set a varaible for the recursive soloution so the 
                # path does not consistently rewrite itself 
                new_path = self.dfs_recursive(i,destination_vertex,visited,path)
                # i
                if new_path is not None:
                    return new_path
        return None
        
        
        
            
                

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
