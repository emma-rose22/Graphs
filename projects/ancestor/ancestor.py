from util import Stack

# 1. Describe the problem using graphs terminology
#     What are your nodes?
#     when are nodes connected?
#     What are your connected components?

# 2. Build your graph, or at least write get_neighbors() function
#     Figure out how to get the nodes with which the node has an edge (how to connect nodes)

# 3. Choose your algorithm and apply it 


'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9

1. My nodes are my nodes. My nodes are connected when there is a parent child relationship
2. make a nearest neighbors function
3. I think that depth first traversal is going to be the best fit here.
If I turn the visual upsidown, I can travel down the list until there are no more parents.
And then return those parents. 
'''


def earliest_ancestor(ancestors, starting_node):
    #we could store the input as a key value pair in a dictionary
    # create a stack to store our searches in 
    #while the stack is greater than 0
        # search dict values for input
        #if key is target:
        # add key to ancestors list 
        # add to stack to search for parents
    
    cache = {}
    all_ancestors = []
    s = Stack()

    s.push(starting_node)

    for node in ancestors:
        node_key, node_value = node
        if node_key not in cache:
            cache[node_key] = []
            cache[node_key].append(node_value)
        else:
            cache[node_key].append(node_value)

    while s.size() > 0:
        current = s.pop()
        for node in cache:
            if current in cache[node]:
                s.push(node)
                all_ancestors.append(node)
                
    print('cache:', cache)
    if len(all_ancestors) > 0:
        print('all', all_ancestors)
        return all_ancestors[-1]
    else:
        return -1

    print('cache:', cache)
    # print('keys:', cache.keys())
    # print('values:', cache.values())

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 6))

graph = Graph()
def build_graph(ancestors):
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

def earliest_ancestor2(ancestors, starting_node):
    #nodes -> people
    #edges -> when child has a parent

    #either bfs or dfs would work here 

    graph = build_graph(ancestors)

    s = Stack()
    visited = set()

    s.push([starting_node])

    longest_path = []

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]
        
        if len(path) > len(longest_path):
            longest_path = path

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)