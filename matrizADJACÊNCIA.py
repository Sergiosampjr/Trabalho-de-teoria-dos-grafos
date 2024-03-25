class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def compara_grafos(self, outro_grafo):
        if self.vertices != outro_grafo.vertices:
            return False

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] != outro_grafo.grafo[i][j]:
                    return False

        return True

# Definindo o primeiro grafo
g1 = Grafo(5)
g1.adiciona_aresta(1, 1)
g1.adiciona_aresta(2, 2)
g1.adiciona_aresta(3, 3)
g1.adiciona_aresta(4, 4)
g1.adiciona_aresta(5, 5)
'''
g1.adiciona_aresta(, )
g1.adiciona_aresta(4, 1)
g1.adiciona_aresta(4, 3)
g1.adiciona_aresta(5, 5)
'''
#g1.adiciona_aresta(1, 2)
#g1.adiciona_aresta(1, 3)
#g1.adiciona_aresta(1, 4)
#g1.adiciona_aresta(2, 1)
#g1.adiciona_aresta(2, 3)
#g1.adiciona_aresta(3, 1)
#g1.adiciona_aresta(3, 2)

# Definindo o segundo grafo
g2 = Grafo(5)
g2.adiciona_aresta(1, 1)
g2.adiciona_aresta(2, 2)
g2.adiciona_aresta(3, 3)
g2.adiciona_aresta(4, 4)
g2.adiciona_aresta(5, 5)
'''
g2.adiciona_aresta(3, 4)
g2.adiciona_aresta(4, 2)
g2.adiciona_aresta(4, 3)
'''
#g2.adiciona_aresta(3, 1)
#g2.adiciona_aresta(3, 2)
#g2.adiciona_aresta(1, 3)
#g2.adiciona_aresta(1, 2)
#g2.adiciona_aresta(2, 1)
#g2.adiciona_aresta(2, 3)
#g2.adiciona_aresta(4, 1)
#g2.adiciona_aresta(1, 4)

# Mostrando as matrizes de adjacência dos grafos
g1.mostra_matriz()
print()
g2.mostra_matriz()

# Verificando se os grafos são isomorfos
if g1.compara_grafos(g2):
    print("Os grafos são isomorfos.")
else:
    print("Os grafos não são isomorfos.")
