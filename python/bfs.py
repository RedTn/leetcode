from collections import deque
def BreadthFirstSearch(graph, start):
    queue = deque([start])
    visitedNodes = [start]

    while len(queue) > 0:
        currentNode = queue.popleft()
        for node in currentNode.get_connections():
            if node not in visitedNodes:
                queue.append(node)
                visitedNodes.append(node)
    
    for node in visitedNodes:
        print(node.get_id())
