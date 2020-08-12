# make a Queue()
# INSTRUCTOR SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# # make a Graph()
# # represent a graph as a dictionary of vertices mapping labels to edges
# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         if vertex_id not in self.vertices:
#             self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("Vertex does not exist")


# def earliest_ancestor(ancestors, starting_node):

#     # build the graph
#     graph = Graph()
#     for item in ancestors:
#         graph.add_vertex(item[0])
#         graph.add_vertex(item[1])
#         graph.add_edge(item[1], item[0])

#     # Do a BFS storing the path
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_length = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         if(len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
#             earliest_ancestor = v
#             max_path_length = len(path)
#             for neighbor in graph.vertices[v]:
#                 path_copy = list(path)
#                 path_copy.append(neighbor)
#                 q.enqueue(path_copy)

#     return earliest_ancestor


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    queue = Queue()
    visited = set()
    longest_path_len = 1
    earliest_ancestor = -1
# loop through the given ancestors list
# create my graph dict {child: {parents}}
    for pairs in ancestors:
        graph[pairs[1]] = set()
    for pairs in ancestors:
        graph[pairs[1]].add(pairs[0])
    # print(graph)

# if the starting node is a not a key of graph, means no parent, return -1
    if starting_node not in graph:
        return -1

    queue.enqueue([starting_node])
# while the queue is not empty
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
    # if it's not in visited, mark as visited
    # get the neighbors
    # loop through neighbors,
    # construct new path by adding each neighbor to the end if neighbor is not none
    # last node is current node,
    # check if the length of current path is bigger than the longest path,
    # or (equal and current node is smaller than earliest ancestor)
    # assign current node to earliest ancestor
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph.get(current_node)
            if neighbors is not None:
                for neighbor in neighbors:
                    new_path = current_path + [neighbor]
                    queue.enqueue(new_path)
            # at the end of the path when there's no neighbors
            else:
                if len(current_path) > longest_path_len or (len(current_path) == longest_path_len and current_node < earliest_ancestor):
                    longest_path_len = len(current_path)
                    earliest_ancestor = current_node
    return earliest_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 6)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))
