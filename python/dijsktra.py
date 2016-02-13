import math
def Dijsktra_path(graph, start):
    vertexMarker = {}
    for v in graph:
            if v.get_id() == start.get_id():
                vertexMarker[v.get_id()] = {'Weight': 0, 'Path': v.get_id(), 'Marked': True}
            else:
                vertexMarker[v.get_id()] = {'Weight': math.inf, 'Path': 0, 'Marked': False}

    currentNode = start
    while True:
        for w in currentNode.get_connections():
            if (currentNode.get_weight(w) + vertexMarker[currentNode.get_id()]['Weight']) < vertexMarker[w.get_id()]['Weight'] \
               and not vertexMarker[w.get_id()]['Marked']:
                vertexMarker[w.get_id()]['Weight'] = currentNode.get_weight(w) + vertexMarker[currentNode.get_id()]['Weight']
                vertexMarker[w.get_id()]['Path'] = currentNode.get_id()
        lowestNode = {'Weight': math.inf, 'Path': 0, 'Marked': False}
        nextKey = False
        for key, value in vertexMarker.items():
            if value['Weight'] <= lowestNode['Weight'] and not value['Marked']:
                lowestNode = value
                nextKey = key
        if nextKey:
            vertexMarker[nextKey]['Marked'] = True
            currentNode = graph.vert_dict[nextKey]
        else: break
    for key, value in vertexMarker.items():
        print (key, value)
