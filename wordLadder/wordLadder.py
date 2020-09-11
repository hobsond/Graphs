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
# print(word_set)
table = set()
letters = []

while len(letters)< 26:
    for i in word_set:
        for x in i:
            if x not in table and x.isalpha():
                table.add(x.lower())
                letters.append(x)
letters.sort()
# print(letters)

def get_neighbors(word:str):
    start= 0
    check = 0
    neighbor = []
    
    while start < len(word):
        if check == 25:
            check= 0
            start +=1
        if start > len(word) - 1:
            break
        x = list(word)
        x[start] = letters[check]
        y = ''.join(x)
        if y in word_set and y != word :
            neighbor.append(y)
        
        check += 1
        continue
    return neighbor


    
    
    
def find_word(begin_word,end_word):
    visited=set()
    q = Queue()
    q.enqueue([begin_word])
    fpath= []
    while q.size() > 0:
        path = q.dequeue()
        fpath.append(path)
        
        v = path[-1]
        if v == end_word:
            break
        if v not in visited:
            visited.add(v)
            
            for neighbor in get_neighbors(v):
                path_copy =  list(path)
                # print(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return fpath[-1]
print(find_word('bail','ants'))