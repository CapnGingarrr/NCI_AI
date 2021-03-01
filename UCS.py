wtree = {'A': [('B', 1), ('C', 4)],
         'B': [('D', 2), ('E', 2)],
         'C': [('F', 11)],
         'D': [('G', 2), ('H', 2)],
         'E': [('I', 4)],
         'F': [('x2', 3)],
         'G': [],
         'H': [('x1', 3)],
         'I': [],
         'x1': [],
         'x2': []
         }


def minindex(queue):
    minindex = 0
    cmin = queue[0][1]

    print(queue)
    for i, tup in enumerate(queue):
        # print ("cmin", cmin)
        # print ("cur", tup[1])
        if tup[1] < cmin:
            cmin = tup[1]
            minindex = i

    return minindex


def ucs(tree, start, goalnodes):
    path = []
    visited, queue = set(), [(start, 0)]  # visited set and frontier [priority queue]
    while queue:  # iterate until frontier (queue) is empty
        print(f'frontier before removing: {queue}')

        lindex = minindex(queue)

        print(f"index of node with low cost {lindex}")

        vertex, cost = queue.pop(lindex)  # pop item with lowest cost
        path.append(vertex)

        print(f'node removed: {vertex}')
        print(f'frontier after removing the last node: {queue}')

        if vertex in goalnodes:
            print(f"Goal Node {vertex} found")
            break

        if vertex not in visited:  # the current node is not in visited set
            visited.add(vertex)  # add current node to visited set

            for child, costchild in tree[vertex]:  # add current node's unvisited childrens to frontier / stack
                if child not in visited:
                    queue.append((child, costchild + cost))

        print(f'frontier after adding current node\'s childs: {queue}\n')

    return path  # return visited nodes


S = 'A'
Goalnodes = ['x1', 'x2']
path = ucs(wtree, 'A', Goalnodes)
print(f'uniform cost search path from {S} to X', path)
