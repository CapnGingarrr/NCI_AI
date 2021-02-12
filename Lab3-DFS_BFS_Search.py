# Build graph

graph = {'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']), 'C': set(['A', 'F']), 'D': set(['B', 'G', 'H']),
         'E': set(['B', 'F']), 'F':set(['C', 'E']), 'G': set(['D']), 'H': set(['D'])}


# Question 1, 3, 5

# Q1
# Create DFS function and visited set

# Keep track of visited nodes


# Function
def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

# Traverse starting at A
visited = dfs([], graph, 'A')
print(visited)

# Q3 - Find node H and print path

# Function
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

dfs_paths(graph, 'A', 'H')

# Q5 - Find node 'H' and print all other paths
def dfs_all_paths(graph, start, goal):
    wstep, forstep = 0,0
    stack = [(start, [start])]
    while stack:
        wstep+=1
        #print("{}:{} before (vertex, path) = stack.pop():{}".format(wstep, forstep, stack))
        (vertex, path) = stack.pop()
        #print("{}:{} after (vertex, path) = stack.pop(): {}".format(wstep, forstep, stack))
        forstep=0
        for next in graph[vertex] - set(path):
            forstep+=1
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                print("{}:{} after stack.append((next, path + [next])):{}".format(wstep, forstep, stack))

list(dfs_all_paths(graph, 'A', 'H'))

# Q2 - BFS function traverse graph

def bfs(visited, graph, node):
    # Initialising visited and queue objects
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Q4 - Find node 'H'

def bfs_path(graph, start, goal):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

path = bfs_path(graph, 'A', 'H')
print(path)

# Q6 - BFS All paths to node
def bfs_all_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_all_paths(graph, 'A', 'H'))




