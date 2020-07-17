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
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


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

#while making the path, add to path
#add only name to visited
#search for room with unvisited exits when stuck
#dft to get around, bfs to get out of a dead end
#get other notes

#do a depth first traversal 
#  while moving, save the steps
#  you encounter a room with no exits, or no unvisited rooms
#     breadth first search to an unvisited room


def dungeon_steps(starting_room):
    s = Stack()
    s.push([starting_room])
    visited = set()
    path = []

    while len(visited) < len(room_graph):
        #print('visited:', visited)
        current_r = s.pop()
        current_r = player.current_room

        if current_r.name not in visited:
            visited.add(current_r.name)
            #find an exit and move through it 
            exits = player.current_room.get_exits()
            #choose an exit to go through
            direction = random.sample(exits, 1)
            #add to path
            path += direction
            #move into one of the rooms
            player.travel(direction[0])
            s.push(player.current_room)
        else:
            #if we get into a dead end
            #we need to do a bfs for an unvisited room

            q = Queue()
            visited_search = set()
            current_search = current_r
            q.enqueue(current_search)

            found = False
            while q.size() > 0 and found == False:
                current = q.dequeue()
                if current.name not in visited_search and current.name in visited:
                    visited_search.add(current.name)
                    exits = current.get_exits()
                    direction = random.sample(exits, 1)
                    path += direction
                    player.travel(direction[0])
                    s.push(player.current_room.name)

                else:
                    found = True

    return path
    

traversal_path = dungeon_steps(player.current_room)
#print('dummy_path:', traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room

visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
# for i in visited_rooms:
#     print('room:', i.name)
#     print('description:', i.description)


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
