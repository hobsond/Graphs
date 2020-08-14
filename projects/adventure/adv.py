from room import Room
from player import Player
from world import World

from queue import Queue
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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
myMap ={}
myMap[player.current_room.id]= {"n":"?","s":"?","e":"?","w":"?",}
q= Queue()
q.put(player.current_room)
rooMChoices = {}
keyReverse= {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}

while len(myMap) !=  len(world.rooms):
    currentRoom = q.get()
    print(f" _______this is my current room {currentRoom.name}")
    
    currentExits = currentRoom.get_exits()
    if len(currentExits)== 0:
        while len(currentExits) is not 0:
            j=traversal_path.pop()
            h = keyReverse[j]
            player.travel(h)
            currentExits= player.current_room.get_exits()
    
    choice = random.choice(currentExits)
    print(f"this is my next random  choice     {choice}")
    nextRoom = currentRoom.get_room_in_direction(choice)
    print(f"this is the room in that direction {nextRoom.id}")
    # print(f"this is my map so far in that direction {myMap[currentRoom.id][choice]}")
    if nextRoom.id not in myMap:
        myMap[nextRoom.id] = {'n':"?",'s':"?",'e':"?",'w':"?",}
    print(f'this is the map for the next room {myMap[nextRoom.id]}')
    
    if myMap[currentRoom.id][choice] == '?':
        myMap[currentRoom.id][choice] = nextRoom.id
        h = keyReverse[choice]
        print(f"this is the map oposite {h}")
        myMap[nextRoom.id][h] = currentRoom.id
        print(f"this is the map for the next room {myMap[nextRoom.id][h]}")
    else:
        
        
        print('ive been that way before')
        j = []
        for i in nextRoom.get_exits():
            if myMap[nextRoom.id][i] =="?":
                j.append(i)
        print(j)
    currentRoom.connect_rooms(choice,nextRoom)
    traversal_path.append(choice)
    q.put(nextRoom)
    player.travel(choice)
print(myMap)

    
    
    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
