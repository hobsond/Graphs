test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
from queue import Queue

def earliest_ancestor(ancestors, starting_node):
    child_Parent={}
    q = Queue()
    q.put(starting_node)
    for (i,j) in ancestors:
        if j not in child_Parent:
            child_Parent[j] = set()
            child_Parent[j].add(i)
            
        if i not in child_Parent[j]:
            child_Parent[j].add(i)
        if i not in child_Parent:
            child_Parent[i]=set()
            child_Parent[i]
        furthest = set()
        furthest = set()
        furthest = set()
        furthest = set()
    
        furthest = set()
    furthest=[]
    if len(child_Parent[starting_node]) ==0:
        return -1
    while q.qsize() > 0:
        current = q.get()
        parents=child_Parent[current]
        if len(parents) == 0:
            if current not in furthest:
                furthest.append(current)
        for i in parents:
            q.put(i)
    furthest.sort()
    return furthest[-1]
                
    

print(earliest_ancestor(test_ancestors,2))