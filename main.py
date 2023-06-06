class Graph:
    def __init__(self):
        """
        Inicializa um objeto Graph com um dicionário vazio para armazenar os nós e suas adjacências.
        """
        self.graph = {}

    def add_edge(self, source, destination):
        """
        Adiciona uma aresta direcionada do nó de origem para o nó de destino no grafo.

        Args:
            source: O nó de origem da aresta.
            destination: O nó de destino da aresta.
        """
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    def dfs(self, start):
        """
        Realiza uma busca em profundidade (DFS) no grafo a partir do nó inicial dado.

        Args:
            start: O nó inicial da busca em profundidade.
        """
        visited = set()
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        """
        Função auxiliar recursiva para realizar a busca em profundidade (DFS) no grafo.

        Args:
            node: O nó atual sendo visitado.
            visited: Um conjunto que armazena os nós visitados.

        """
        visited.add(node)
        print(node)

        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs_helper(neighbor, visited)

    def bfs(self, start):
        """
        Realiza uma busca em largura (BFS) no grafo a partir do nó inicial dado.

        Args:
            start: O nó inicial da busca em largura.
        """
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node)

                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
    
    def calcVertexCover(self):
        """
        Calcula a cobertura de vértices do grafo.
        """
        # Inicializa a cobertura de vértices
        vertexCover = set()
        copy = self.graph.copy()

        # Enquanto houverem arestas no grafo
        while copy:
            # Escolhe uma aresta qualquer
            # edge = next(iter(copy))
            # print(copy)
            edge = copy.popitem()

            if not edge[1]:
                continue

            # Adiciona os vértices da aresta na cobertura
            # vertexCover.add(edge)
            # print(edge)
            vertexCover.add(edge[0] + edge[1][0])
            # for i in edge[1]:
            #     vertexCover.add(edge[0] + i)
            #vertexCover.add(edge[1])

            # Remove todas as arestas que contém os vértices da aresta escolhida
            # copy = {k: v for k, v in copy.items() if edge[0] not in v and edge[1] not in v}
            # copy = {k: v for k, v in copy.items() if edge not in v}
            # copy.pop(edge[0])
            # print(edge[0])
            self._removeEdgesFromNode(copy, edge[0])
            # self.removeEdges(copy, edge[1])

        return vertexCover

    def _removeEdgesFromNode(self, g, node):
        """
        Remove todas as arestas que contém o nó dado.

        Args:
            node: O nó que será removido das arestas.
        """
        if node in g:
            g.pop(node)
        for key, value in g.items():
            if node in value:
                value.remove(node)


# Exemplo de uso
g = Graph()
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(4, 2)

g.add_edge("a", "b")
g.add_edge("a", "c")
g.add_edge("b", "c")
g.add_edge("c", "d")
g.add_edge("d", "b")
g.add_edge("d", "e")
g.add_edge("e", "d")
g.add_edge("e", "a")
g.add_edge("e", "f")

# print("DFS:")
# g.dfs(1)

# print("BFS:")
# g.bfs(1)

print(g.calcVertexCover())
