test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
from queue import Queue,LifoQueue

def ancestorGraph(ancestors):
    child_Parent={}
    
    for (i,j) in ancestors:
        if j not in child_Parent:
            child_Parent[j] = []
            child_Parent[j].append(i)
            
        if i not in child_Parent[j]:
            child_Parent[j].append(i)
        if i not in child_Parent:
            child_Parent[i]=[]
    return child_Parent

def earliest_ancestor(ancestors, starting_node,path=None,visited = None,choices=None):
    
    vert = ancestorGraph(ancestors)
    
    q = Queue()
    
    q.put(starting_node)
    
    if visited is None:
        visited = set()
    
    if path is None:
        path = [] + [starting_node]
    
    if choices is None:
        choices = {}
    if len(vert[starting_node]) == 0:
        path = path 
        choices[starting_node] = len(path) 
        
    visited.add(starting_node)
    
    for i in vert[starting_node]:
        if i not in visited:
            earliest_ancestor(ancestors,i,path + [i] ,visited,choices)
            
    t={}
    h=[]
    for (i,x) in choices.items():
        if i ==starting_node and x == 1:
            return -1
        if x not in t:
            t[x] = i
        if x < t[x]:
            t[x] = i
        h.append(t[x])
            
    
    
        
    return h[0]
        

    
    

print(earliest_ancestor(test_ancestors,8))