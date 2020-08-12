# make a Queue()

# make a Graph()


def earliest_ancestor(ancestors, starting_node):

    # build the graph
    graph = Graph()
    for item in ancestors:
        graph.add_vertex(item[0])
        graph.add_vertex(item[1])
        graph.add_edge(item[1], item[0])

    # Do a BFS storing the path
    q = Queue()
    q.enqueue([starting_node])
    max_path_lenth = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if(len(path) >= max_path_lenth and v < earliest_ancestor) or (len(path) > max_path_lenth):
            earliest_ancestor = v
            max_path_lenth = len(path)
            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return earliest_ancestor
