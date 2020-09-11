from room import Room
from player import Player
from world import World

from queue import Queue,LifoQueue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt" 


# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms() 

check = 0   
start=0
myMap = {}

while True:
    if check == len(world.room_grid[0]) :
        check = 0
        start += 1
    grid = world.room_grid
    
    x = grid[start][check]
    
    if x is not  None:
        myMap[x.name] = [(i,x.get_room_in_direction(i)) for i in x.get_exits()]
    check += 1
    
    if start == len(world.room_grid) -1 :
        break
    
    continue
player = Player(world.starting_room)
# print(myMap)



# Fill this out with directions to walk
traversal_path = []
namePath = []
visited = set()
q = LifoQueue()
q.put([player.current_room])
keyReverse= {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}
deadEnd = set()
def Traverse():
    # deadEnd.add(world.starting_room)
    while len(visited) < len(world.rooms):
        # Grab the the lattest path from the stack
        path = q.get()
        # current is the the last room node added to the lattest path
        current = path[-1]
        if q.qsize() ==0 and current is not world.starting_room:
            deadEnd.add(current.name)
            # print('added')
        #  add the current room to the visited 
        
        if current.name not in visited:
            
            visited.add(current)
        elif current.name in visited:
            continue
        
        namePath.append(path)
        # namePath.append(current)
        print(current.name)
        
      
        exits = myMap[current.name]
        
        if len(exits) == 1 :
            # print('dead end')
            # print(current.name)
            deadEnd.add(current.name)
        choice = random.choice(exits)
        while choice[1] == current or choice in deadEnd or choice in visited:
            choice = random.choice(exits)
            
        # print('hello')    
        # if choice not in deadEnd and choice not in visited:
        cpy_path = list(path)
        cpy_path.append(choice[1])
        q.put(cpy_path)
        traversal_path.append(choice[0])
        
        # for i in exits:
        #     if i[1].name not in visited and i[1].name not in deadEnd:
        #         path_copy = list(path)
        #         path_copy.append(i[1])
        #         namePath[-1] += path_copy
        #         q.put(path_copy)
        
        continue
        
    print(traversal_path)
    print(len(traversal_path))
    print(len(world.rooms))
            
Traverse()
         

# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

