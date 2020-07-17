from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 'n']


#suggestion is to make a starting graph that shows where exits are
# but you only know what you can see from your position
# so you can see that you can move this way, but not the ID of that room
#yes we are traversing, but we need to input directions, the path of how
# to step from room to room
# we want step by step instructions 
# and if we can, minimize those steps 

#So run a traversal in order to build the graph
#read me suggests a random traversal
# at a dead end, we want to find the nearest unexplored exit

#translate to graph terminology
# node : rooms
# edges : exits
# 

# IN ENGLISH
#we start at the first node
#look around and see what exits there are
#go down the path of an exit until reaching a dead end
#back track until we can go out an exit we haven't been down before
#do this until all the rooms are visited

#he said the trick will be figuring out how to get our two traversal types to play together...

# PSUEDO CODE
# we start at the first node
# look around to see what exits there are 
#    do a depth first traversal of the map
#        generate a nested dictionary that contains all the exits in all the rooms
#        this can kind of act as a get neighbors function as we are moving through
#go down the path of an exit until reaching a dead end
#    this is where we will do a breadth first traversal 
#    as we go from room to room, the cardinal values that had a ? will be replaced with a room name
#     this is also where the traversal path is populated
#    if we get to dead end:
#        travel back a room and add that to the traversal path
#        if it has cardinal directions that haven't been visited
#             do a breadth first traversal from there

def make_room_dict(starter_room):
    #make this get neighbors?
    the_room = {}
    room_directions = {}
    for direction in starter_room.get_exits():
        room_directions[direction] = '?'
    the_room[starter_room.name] = room_directions
    return the_room

print('what', player.current_room.name)

def graph_all_rooms(starter_room):
    #this is a DFT
    #the master graph
    all_rooms = {}
    s = Stack()
    #add in the first room 
    s.push(starter_room)
    visited = set()

    while s.size() > 0:
        current_node = s.pop()
        print('current node:', current_node)
        if current_node not in visited:
            visited.add(current_node)
            #add room's directions and room to all_rooms
            all_rooms[current_node.name] = make_room_dict(current_node)
            print('added room:', all_rooms[current_node.name])
            #for each of the available directions in that room
            for direction_list in all_rooms[current_node.name].values():
                for direction in direction_list.keys():
                    print('direction:', direction)
                    #if we can travel there 
                    player.travel(direction)
                    #print('player room:', player.current_room)
                    #add that room to the stack of rooms to visit
                    s.push(player.travel(direction))
    return all_rooms

#print('trying to move:', player.travel('n'))

print('first graph:', graph_all_rooms(player.current_room))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room

visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
for i in visited_rooms:
    print('room:', i.name)


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
