def jaccard_similarity(a, b):
    intersection = len(set(a).intersection(b))
    union = len(a) + len(b) - intersection
    return intersection / union

# Exemplo de uso
a = [1, 2, 3, 4, 5]
b = [4, 5, 3, 1, 2]
print(jaccard_similarity(a, b))
