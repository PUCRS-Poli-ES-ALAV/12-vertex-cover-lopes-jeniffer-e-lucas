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
    
    def CVA(g):
        c = None
        e = g * e

        while (e != None):



# Exemplo de uso
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

print("DFS:")
g.dfs(1)

print("BFS:")
g.bfs(1)
