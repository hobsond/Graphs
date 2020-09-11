test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
from queue import Queue,LifoQueue
import random
import math

def ancestorGraph(ancestors):
    child_Parent={}
    
    for (i,j) in ancestors:
        if j not in child_Parent:
            child_Parent[j] = []
            child_Parent[j].append(i)
            
        if i not in child_Parent[j] and len(child_Parent[j]) <2:
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
    # if vert[starting_node] == 0:
    choices[starting_node] = path
    # print(f"node {starting_node}        path:{len(path)}")
    
    visited.add(starting_node)
    try:
        for i in vert[starting_node]:
            
            if i not in visited:
                earliest_ancestor(ancestors,i,path + [i] ,visited,choices)
            
    except:
        return -1
    
    t={}
    h=[]
    for (i,x) in choices.items():
        # if len(x) == 1:
        #     return -1
        if len(x) not in t:
            t[len(x)] = i
        if i > t[len(x)]:
            t.pop(len(x))
            t[len(x)] = i
        h.append([t[len(x)],x])
            
    
    h.sort(key= lambda e:len(e[1]),reverse=True)
    
    if len(h[0][1]) is 1:
        return -1
    if h[1] and len(h[0][1]) ==len(h[1][1])   and h[0][0] > h[1][0]:
        return h[1][0]
    return h[0][0]



def rand():
    return random.randint(1,10000)
pr = []
for i in range (1,1000):
    x = rand()
    y = rand()
    pr.append((x,y))

# while True:
    

#     jj = input('check number : ')
#     if jj == "quit":
#         break

print(earliest_ancestor(test_ancestors,8))
# # print(ancestorGraph(pr)[12])