import graph
from dijsktra import Dijsktra_path
from dfs import DepthFirstSearch
from bfs import BreadthFirstSearch

if __name__ == '__main__':

    g = graph.Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    g2 = graph.Graph()

    g2.add_vertex('a')
    g2.add_vertex('b')
    g2.add_vertex('c')
    g2.add_vertex('d')
    g2.add_vertex('e')
    g2.add_vertex('f')
    g2.add_vertex('g')

    g2.add_edge('a', 'b', 1)
    g2.add_edge('a', 'c', 3)
    g2.add_edge('a', 'f', 10)
    g2.add_edge('b', 'c', 1)
    g2.add_edge('b', 'd', 7)
    g2.add_edge('b', 'e', 5)
    g2.add_edge('b', 'g', 2)
    g2.add_edge('c', 'd', 9)
    g2.add_edge('c', 'e', 3)
    g2.add_edge('d', 'e', 2)
    g2.add_edge('d', 'f', 1)
    g2.add_edge('d', 'g', 12)
    g2.add_edge('e', 'f', 2)
    
    #Dijsktra_path(g, g.vert_dict['a'])
    #print("---")
    #Dijsktra_path(g2, g2.vert_dict['a'])

    search = graph.Graph()

    search.add_vertex('a')
    search.add_vertex('b')
    search.add_vertex('c')
    search.add_vertex('d')
    search.add_vertex('e')
    search.add_vertex('f')
    search.add_vertex('g')
    search.add_vertex('h')

    search.add_edge('a', 'b')
    search.add_edge('a', 'd')
    search.add_edge('a', 'g')
    search.add_edge('b', 'e')
    search.add_edge('b', 'f')
    search.add_edge('c', 'f')
    search.add_edge('c', 'h')
    search.add_edge('d', 'f')
    search.add_edge('e', 'g')

    #DepthFirstSearch(search, search.vert_dict['a'])
    BreadthFirstSearch(search, search.vert_dict['a'])
