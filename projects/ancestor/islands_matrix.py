# Islands Matrix Problem
# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:

#THIS IS NOT A MATRIX REPRESENTATION OF A GRAPH
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
#island_counter(islands) # returns 4

#nodes = the ones
#edge= if directly connected by n, s, e, w
#islands : connected componenets

#build our graph or jsut define getNeighbors

#we can iterate through and when we encounter a 1, 
#do get neighbors to get all the 1s it is touching
# they are added to a visited list

#Plan:
#iterate through matrix
#when we see 1, if not visited, run a traversal
#   increment our island counter
#    mark as visited 

def get_neighbors(node, matrix):
    neighbors = []
    #take a step n, s, e, w
    row, col = node
    #dont want to step out of the matrix
    stepNorth = stepSouth = stepWest = stepEast = False

    if row > 0:
        stepNorth = row - 1
    if row < len(matrix) - 1:
        stepSouth = row + 1
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    if col > 0:
        stepWest = col - 1

    if stepNorth and matrix[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))
    if stepSouth and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))
    if stepEast and matrix[row][stepEast] == 1:
        neighbors.append((row, stepEast))
    if stepWest and matrix[row][stepWest] == 1:
        neighbors.append((row, stepWest))

    return neighbors

def dft_recursive(node, visited, matrix):
    if node not in visited:
        # add to visited
        visited.add(node)
        # get neighbors
        neighbors = get_neighbors(node, matrix)
        # for each neighbor, recurse
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, matrix)

def island_counter(isles): 
    visited = set()
    number_islands = 0
    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)
            #check if visited and if it is a 1
            if node not in visited and isles[row][col] == 1:
                number_islands += 1
                dft_recursive(node, visited, isles)
    return number_islands

print(island_counter(islands))