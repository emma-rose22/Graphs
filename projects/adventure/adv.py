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
    #past_directions = Stack()
    opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

    while len(visited) < len(room_graph):
        directions = []
        #add current room to visited
        visited.add(player.current_room)
        #find an exit and move through it 
        exits = player.current_room.get_exits()
        #what if I checked if the room was visited before 
        #making it one of the random choices
        for i in exits:
            if player.current_room.get_room_in_direction(i) not in visited:
                directions.append(i)

        #choose an exit to go through
        #not choosing visited rooms means maybe directions are empty
        if len(directions) > 0:
            direction = random.sample(directions, 1)
            #add to path
            path.append(direction[0])
            #move into one of the rooms
            player.travel(direction[0])
            #trying add direction instead of name
            s.push(direction[0])
 
        else:
            #instead of using bfs,
            #what if I turn around and go the opposite way
            #this only works if I store room directions instead of 
            #the names

            #using path doesnt work, creates endless loop
            turn_around = s.pop()
            player.travel(opposites[turn_around])
            path.append(opposites[turn_around])


    return path

#tried changing search type 
#tried using  get_room_in_direction to check an exit before moving there
#tried not using seperate visited for bfs    
#try turning around instead of bfs

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
