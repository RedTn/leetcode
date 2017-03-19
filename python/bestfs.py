import math.inf
def BestFirstSearch(graph, start):
    startPath = {"Weight": 0, "Node": start}
    exploredNodes = [start]
    frontierNodes = []
    currentBestCost = 0
    currentNode = start
    
    bestPath = {"Weight": math.inf, "Node": 0}
    for frontier in currentNode.get_connections():
        if currentNode.get_weight(frontier) < bestPath:
            bestPath["Weight"] = currentNode.get_weight(frontier)
            bestPath["Node"] = frontier
        frontierNodes.append(frontier)
    currentNode = bestPath["Node"]
    exploredNodes.append[bestPath["Node"]]
