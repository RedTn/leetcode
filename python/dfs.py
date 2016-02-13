def DepthFirstSearch(graph, start):
    visitedNodes = [start]
    stack = [start]

    while len(stack) > 0:
        currentNode = stack[-1]
        anyResults = False
        for node in currentNode.get_connections():
            if node not in visitedNodes:
                anyResults = True
                stack.append(node)
                visitedNodes.append(node)
                break
        if not anyResults:
            stack.pop()

    for node in visitedNodes:
        print(node.get_id())
    
