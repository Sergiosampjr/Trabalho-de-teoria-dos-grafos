import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity_graphs(matrix1, matrix2):
    # Converte as matrizes em vetores
    vector1 = np.array(matrix1).flatten()
    vector2 = np.array(matrix2).flatten()

    # Calcula o cosseno entre os vetores
    similarity = cosine_similarity([vector1], [vector2])[0][0]

    return similarity

# Exemplo de uso
matrix1 =[[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0]]
            #[[0, 1, 1, 0],
           #[1, 0, 0, 1],
           #[1, 0, 0, 1],
           #[0, 1, 1, 0]]

matrix2 = [[0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0]] 
            #[[0, 1, 0, 0],
           #[1, 0, 1, 1],
           #[0, 1, 0, 0],
           #[0, 1, 0, 0]]

similarity = cosine_similarity_graphs(matrix1, matrix2)
print("Similaridade de cosseno entre as matrizes:", similarity)

# Verifica se os grafos são considerados similares
if similarity >= 0.75:
    print("Os grafos são considerados similares.")
else:
    print("Os grafos não são considerados similares.")
    
    