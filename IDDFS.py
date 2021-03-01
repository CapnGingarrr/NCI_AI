tree = {'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G', 'H'],
        'E': ['I'],
        'F': [],
        'G': [],
        'H': [],
        'I': []
        }


# # # # # # # # # # # # # # # # #
# Iterative Depth First Search #
# # # # # # # # # # # # # # # # #
def iddfs(tree, start, maxdepth):
    level = 0
    path = []
    visited = set()  # visited nodes
    stack = [(start, 0)]  # frontier (stack last in first out) additionally stores depth of node (tuple)

    # Iterate until frontier/stack is empty
    while stack:
        print(f'Frontier before removing: {stack}')
        # pop last item from frontier/stack
        vertex, vlevel = stack.pop()

        if vlevel > maxdepth:
            continue

        path.append(vertex)
        print(f'Node removed: {vertex}')
        print(f'Node level: {vlevel}')
        print(f'Frontier after removing last node: {stack}')

        # if current node not in visited set
        if vertex not in visited:
            # Add current node to visited
            visited.add(vertex)

            # Add current nodes unvisited children to frontier/stack and increase vlevel
            for child in tree[vertex]:
                stack.append((child, vlevel + 1))

        print(f'Frontier after adding current node children: {stack}\n')

    return path


path = iddfs(tree, 'A', 2)
print('IDDFS route:', path)

# # # # # # # # # # # # # # #
# IDFS Return Path to Goal #
# # # # # # # # # # # # # # #

def iddfs(tree, start, maxdepth, goalnode):
    level = 0
    path = []

    visited = set()  # visited set
    stack = [(start, 0)]  # frontier [stack last in first out]  additionally it stores depth of the node
    # (data structure tuple)

    while stack:  # iterate until frontier (stack) is empty
        print(f'Frontier before removing: {stack}')

        vertex, vlevel = stack.pop()  # pop last in item from frontier / stack

        if vlevel > maxdepth:
            continue

        path.append(vertex)
        print(f'Node removed: {vertex}')
        print(f'Node level: {vlevel}')
        print(f'Frontier after removing the last node: {stack}')

        if vertex == goalnode:
            print(f"Goal Node {goalnode} found")
            break

        if vertex not in visited:  # the current node is not in visited set
            visited.add(vertex)  # add current node to visited set

            for child in tree[vertex]:  # add current node's unvisited childrens to frontier / stack
                if child not in visited:
                    stack.append((child, vlevel + 1))  # increase level by 1

        print(f'Frontier after adding current node\'s childs: {stack}\n')

    return path  # return visited nodes


path = iddfs(tree, 'A', 2, 'E')
print("iddfs route", path)
