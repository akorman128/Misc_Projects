
# class for graph
class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

# makes graph
example_graph = SimpleGraph()
# what each node in graph is touching
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

# specialized container datatypes
import collections

class Queue:
    def __init__(self):
        # elements is a list container
        self.elements = collections.deque()

        # checks to see if deque empty. all nodes start in ftontier to begin w.
    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

        # remove + return element from left side of deque
    def get(self):
        return self.elements.popleft()


# takes graph object and starting point
def breadth_first_search_1(graph, start):
    # print out what we find
    frontier = Queue()
    # appends starting point of search
    frontier.put(start)
    # list of all nodes visited
    visited = {}
    # sets starting point to visited
    visited[start] = True

    # while frontier queue isn't empty, set current node to node from left side of deque (list)
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        # for each node in graph, find neighbor of the current node
        for next in graph.neighbors(current):
            # if we've been there, append to the frontier, set visited value to true
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breadth_first_search_1(example_graph, 'A')

#############################################

# grid class

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

# define if node is in graph
    def in_bounds(self, id):
        # takes x and y of node and sets to id
        (x, y) = id
        # checks if in bounds
        return 0 <= x < self.width and 0 <= y < self.height

        # checks if position is not a wall
    def passable(self, id):
        return id not in self.walls

        # finds neighboring nodes
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        # returns all  points in bounds
        results = filter(self.in_bounds, results)
        # returns all neighboring points passable
        results = filter(self.passable, results)
        return results


# function takes graph object and starting point
def breadth_first_search_2(graph, start):
    # frontier is a queue
    frontier = Queue()
    # sets starting point
    frontier.put(start)
    # directory of prior nodes
    came_from = {}
    came_from[start] = None

    # while frontier isn't empty
    while not frontier.empty():
        # gets current node
        current = frontier.get()
        for next in graph.neighbors(current):
            # if next node not yet visited
            if next not in came_from:
                # add to frontier
                frontier.put(next)
                came_from[next] = current

    return came_from

# make grid object
g = SquareGrid(30, 15)
# sets walls... would be a list of touples
g.walls = DEMO_GRAPH1

# calls fx
parents = breadth_first_search_2(g, (8, 7))
# draws gird
draw_grid(g, width = 2, point_to = parents, start = (8, 7))
