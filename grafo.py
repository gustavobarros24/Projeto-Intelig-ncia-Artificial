import math
import networkx as nx  
import matplotlib.pyplot as plt  
from node import Node
from queue import Queue

class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para armazenar as heuristicas para cada nodo -< pesquisa informada
    

    def __str__(self): #grafo em string
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    #########################################################################################################
    #   encontrar nodo pelo nome
    #########################################################################################################

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None

    #########################################################################################################
    #   imprimir arestas
    #########################################################################################################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    #########################################################################################################
    #   adicionar aresta ao grafo 
    #########################################################################################################

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        
        # Test if nodes are in the graph.
        # If not, add them with the ID corresponding to the number of nodes in the graph.
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes)
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []

        # Add the edge.
        self.m_graph[node1].append((node2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
              self.m_graph[node2].append((node1, weight))

    #########################################################################################################
    #  adicionar arestas de nodo1 para todos os nodos na lista com custo respetivo
    #########################################################################################################

    def add_edges_from_list(self, node1, node2_list, weights_list):
        ## shortcut for adding multiple edges from one starting node to a list of end nodes.
        
        for i in range(len(node2_list)):
            self.add_edge(node1, node2_list[i], weights_list[i])
        
    def getNodes(self):
        return self.m_nodes

    #########################################################################################################
    #    devolver o custo de uma aresta                                                                      
    #########################################################################################################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    def get_neighbours(self, n):
        return self.m_graph[n]
        
    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()
    
    def getH(self, n):
        return self.m_h[n]
    
    def add_heuristica(self, n, estimate):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estimate

    def algDFS(self, start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.algDFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()
        return None

    def algBFS(self, start, end):
        visited = set()
        fila = Queue()
        custo = 0
        fila.put(start)
        visited.add(start)
        parent = dict()
        parent[start] = None
        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)
        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            custo = self.calcula_custo(path)
        return (path, custo)

    def algestrela(self, start, end):
        open_list = {start}
        closed_list = set([])
        g = {start: 0}
        parents = {start: start}
        
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n is None or g[v] + self.getH(v) < g[n] + self.getH(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return (reconst_path, self.calcula_custo(reconst_path))

            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight + self.getH(m)  # Add heuristic value to the cost
                else:
                    if g[m] > g[n] + weight + self.getH(m):
                        g[m] = g[n] + weight + self.getH(m)
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


    def greedy(self, start, end):
        open_list = set([start])
        closed_list = set([])
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
            if n == end:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return (reconst_path, self.calcula_custo(reconst_path))            
            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None