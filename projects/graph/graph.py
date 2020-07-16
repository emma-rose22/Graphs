"""
DFT
1. Starting node + target node
2. add [starting_node] to path and push to stack
3. pop last item from stack
4. check the last item in the path for instance if path ==[1, 2, 4, 6, 7],
check 7 and get its neighbors
5. add path[-1] to visited
5. get neighbors of path[-1]
6. add to your path, so for each neighbor create a path copy,
add neighbor to the end of the path
7. push the new path to the stack
8. for instance if neighbors of 7 are 10, 12, 13,
create [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13]
9. when path[-1] == target, stop and return path


BFS
1. do everything above but with a queue instead of a stack
"""


"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f'{self.vertices}'

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # using adjacency list
        # key is vertex_id, value is an empty set

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # go into dictionary
        # go to v1
        # add v2

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # go to vertex_id
        # print set

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        # insert starting node into queue
        # we don't want to visit the same node twice
        #   can do this with a set

        #while queueu isn't empyu
        #  deque from front of line
        #  if we haven't visited this node yet
        #      mark as visited
        #      get its neighbors, add to queue

        q = Queue()

        q.enqueue(starting_vertex)
        neighbors = []

        visited = set()

        while q.size() > 0:
            current_node = q.dequeue()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make a stack
        # push our starting vertex onto the stack
        # create a set to track if we have visited node

        #while stack isn't empty
            #current node = whatevr on top of stack
            #if we havent visited this before:
                #mark as visited
                # get its neighbors and add them to stack

        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #we have added visited so we don't forget where we have visited while looping
        #we don't need a stack because depth first will do that naturally

        #mark this vertex as visited
        #for each neighbor not visited
        #   recurse on neighbor

        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # path = Queue()
        # visited = set()

        # path.enqueue(starting_vertex)

        # while path.size() > 0:
        #     print('path:', path)
        #     print('visited:', visited)
        #     current = path.dequeue()
        #     visited.add(current)

        #     neighbors = self.get_neighbors(current)
        #     for i in neighbors:
        #         #path = path.copy()
        #         path.enqueue(i)
        #     if path.peek() == destination_vertex:
        #         return list(visited)

        #bfs needs queue
        q = Queue()
        visited = set()

        #add rhe path to the starting vertex

        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            #get current path out of queue
            current_path = q.dequeue()
            #get the current node out of the current path
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    #make a copy of the path for each neighbor before adding it 
                    #this is so we don't alter the original path for different nodes
                    path_copy = current_path[:] 
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)

        #while queue isnt empty
        #  dequeue node at front of line
        #  if it is the target, return it

        #  if not visited, mark as visited
        #  get neighbors
        #     for each neighbor, add to queue


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # DFT
        # 1. Starting node + target node
        # 2. add [starting_node] to path and push to stack
        # 3. pop last item from stack
        # 4. check the last item in the path for instance if path ==[1, 2, 4, 6, 7],
        # check 7 and get its neighbors
        # 5. add path[-1] to visited
        # 5. get neighbors of path[-1]
        # 6. add to your path, so for each neighbor create a path copy,
        # add neighbor to the end of the path
        # 7. push the new path to the stack
        # 8. for instance if neighbors of 7 are 10, 12, 13,
        # create [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13]
        # 9. when path[-1] == target, stop and return path

        #empty stack we add path to
        #remove entry if it has no children
        #if we have already visited a node, remove from stack

        s = Stack()
        visited = set()

        #add rhe path to the starting vertex

        path = [starting_vertex]
        s.push(path)

        while s.size() > 0:
            #get current path out of queue
            current_path = s.pop()
            #get the current node out of the current path
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    #make a copy of the path for each neighbor before adding it 
                    #this is so we don't alter the original path for different nodes
                    path_copy = current_path[:] 
                    path_copy.append(neighbor)

                    s.push(path_copy)

        #while queue isnt empty
        #  dequeue node at front of line
        #  if it is the target, return it

        #  if not visited, mark as visited
        #  get neighbors
        #     for each neighbor, add to queue

    def dfs_recursive(self, starting_vertex, destination_vertex, path= [], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        #we want to mark our node as visited
        # check if it is our target node

        # iterate over the neighbors of current
        #  check if visited
        #  if not recurse
        #   if recursion returns a path, return from here

        visited.add(starting_vertex)
        if len(path) == 0:
            path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path

        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
                if result is not None:
                    return result

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('Vertices:')
    print(graph.vertices)
    print()

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('BFT:')
    graph.bft(1)
    print()

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT:')
    graph.dft(1)
    print()
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS:')
    print(graph.bfs(1, 6))
    print()

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS:')
    print(graph.dfs(1, 6))
    print()
    # print(graph.dfs_recursive(1, 6))


    print('DFS Recursive:')
    print(graph.dfs_recursive(1, 6))


    print('the graph:', graph)