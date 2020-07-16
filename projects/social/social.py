import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        ## use num users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        ## we could make a list with all possible friendships 
        friendships = []
        #for all users in the range of users we just made
        for user in range(1, self.last_id + 1):
            #for friend in range of current user and the number of users we asked for 
            for friend in range(user + 1, num_users + 1):
                #create a tuple of each user and a random friend
                friendship = (user, friend)
                friendships.append(friendship)
        
        #shuffle the list 
        self.fisher_yates_shuffle(friendships)
        #take as many friends as we need
        total_friendships = num_users * avg_friendships
        #divided by two because bidirectional
        random_friendships = friendships[:total_friendships//2]

        # add randomized friendships paired down for the number of friends we asked for
        # to the class friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_time_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        ## use num users
        for user in range(num_users):
            self.add_user(user)

        #as long as we havent made all the friendships we need
        # pick 2 random numbers between 1 and last id
        # try to create that friendship
        # if we can, increment friendships

        target_num_friendships = (num_users * avg_friendships) // 2
        friendships_created = 0

        while friendships_created < target_num_friendships:
            #pick two random nums between 1 and last id
            friend_one = random.randint(1, num_users)
            friend_two = random.randint(1, num_users)
            #will return false if friendship exists or we try to be friends with ourselves
            friendship_successful = self.add_friendship(friend_one, friend_two)
            if friendship_successful:
                friendships_created += 2


    def get_neighbors(self, friend):
        return self.friendships[friend]
    
    def bfs(self, starting_vertex, destination_vertex):
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


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # return visited
        # 1. Describe the problem using graphs terminology
        #     What are your nodes?
                #user id
        #     when are nodes connected?
                #when they are friends
        #     What are your connected components?
                #the users

        # 2. Build your graph, or at least write get_neighbors() function
        #     Figure out how to get the nodes with which the node has an edge (how to connect nodes)
                # currently each friend is in a dictionary, w/ a dictionary of their friends

        # 3. Choose your algorithm and apply it 
            #we should do a breadth first traversal because we want the shortest path

        #do a bft of everyone in the user's extended friend group
        #go through all the users that contain target as friends
        #get all of their friends
        #   this is the get neighbors part
        #put them together, prioritizing shortest connection to target
        '''
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
        '''
        visited = {}  # Note that this is a dictionary, not a set
        for friend in self.friendships[user_id]:
            if friend not in visited:
                visited[friend] = self.bfs(user_id, friend)
            #print('first iter:', visited)
            for second_degree in self.friendships[friend]:
                visited[second_degree] = self.bfs(user_id, second_degree)
        return visited

        #lesson version:
        # Plan, use BTF, use dictionary for visited

        #imports a queue

        #while q isdsn't empty
        #  deque the current path
        #  grab the last vertex from the path

        #  if it hasn't been visited
        #     add to dictionary 
        #     then enqueue paths to each of our neighbors 


    def get_all_social_paths2(self, user_id):
        #used bft because we still do need to go through every item
        #though we are using it a bit like a search here
        visited = {}
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            #get current path 
            current_path = q.dequeue()

            #get last vertex
            current_user = current_path[-1]

            #if it hasnt ben visited 
            if current_user not in visited:
                visited[current_user] = current_path

                friends = self.friendships[current_user]

                #enqueue paths to each neighbors
                for friend in friends:
                    path_to_friend = current_path + [friend]

                    q.enqueue(path_to_friend)

        return visited




if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('the graph:', sg.friendships)
    #connections = sg.get_all_social_paths(1)
    #print('friends of friend:', connections)
    connections = sg.get_all_social_paths2(1)
    print('extended network:', connections)


    #percent of total users in extended social network

    #how many people we know // how many people there are

    # print(f'{(len(connections) - 1) / 10 *100}%')

    # #what is the average degree of seperation between a user and the network?

    # # average length of a path to each user
    # #traverse a users extended connections, gather lengths, sum

    # total_length = 0

    # for friend in connections:
    #     total_length += len(connections[friend])

    # print(total_length / len(connections))
