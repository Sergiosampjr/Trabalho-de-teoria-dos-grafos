def jaccard_similarity(matrix1, matrix2):
    # Transforma as matrizes de adjacência em conjuntos de pares de vértices conectados
    set1 = set((i, j) for i, row in enumerate(matrix1) for j, val in enumerate(row) if val != 0)
    set2 = set((i, j) for i, row in enumerate(matrix2) for j, val in enumerate(row) if val != 0)

    # O cálculo de Jaccard.
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection

    # Calcula a similaridade de Jaccard
    jaccard_similarity = intersection / union

    return jaccard_similarity

# Aplicação
matrix1 = [[0, 1, 1, 0, 0],
           [1, 0, 1, 1, 0],
           [1, 1, 0, 0, 1],
           [0, 1, 0, 0, 1],
           [0, 0, 1, 1, 0]]

matrix2 = [[0, 1, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 0, 0, 1],
           [0, 0, 1, 1, 0]]

print("Similaridade de Jaccard entre as matrizes:", jaccard_similarity(matrix1, matrix2))

