class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
word_set=set()
with open('words.txt') as f :
    for word in f:
        word_set.add(word.strip().lower())
letters=set()
def letterList():
    for i in word_set:
        for j in i:
            if j.lower() not in letters and j.isalpha() :
                letters.add(j.lower())
    x = []
    for i in letters:
        x.append(i)
    return x
def get_neighbors(word):
    h = letterList()
    h.sort()
    neighbors = []
    for i in range(len(word)):
        for j in h:
            x = word.replace(word[i],j)
            if x in word_set:
                neighbors = neighbors + [x]
    return neighbors
    
def find_word(begin_word,end_word):
    visited=set()
    q = Queue()
    q.enqueue(begin_word)
    
    while q.size() > 0:
        path = q.dequeue()
        
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v== end_word:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy =  list(path)
                print(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
# print(get_neighbors('bail'))
# print(get_neighbors('tail'))
print(find_word('sail','tail'))