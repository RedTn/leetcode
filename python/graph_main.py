import graph
from dijsktra import Dijsktra_path

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
    
    Dijsktra_path(g, g.vert_dict['a'])
    print("---")
    Dijsktra_path(g2, g2.vert_dict['a'])
