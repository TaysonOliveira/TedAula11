import numpy as np

matriz_A = np.random.randint(1, 101, size=(10, 10))

soma_total = np.sum(matriz_A)
print("A soma de todos os elementos da matriz é:", soma_total)

matriz_B = matriz_A * 3

print("A matriz B (A * 3) é:")
print(matriz_B)