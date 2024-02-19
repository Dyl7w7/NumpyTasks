import numpy as np;
vector = np.array([1,2,3,4,5,6,7,8,9,0])

print(vector.size)
print(vector.ndim)
print(vector.dtype, "\n")

matriz = np.array(([2,3,4,1],[1,2,3,4],[1,2,3,4],[1,2,3,4]))
matriz1 = np.array([2,3,4,1])
matriz2 = np.array([1,2,3,4])

print(matriz)
print("Index de matrices")
print(matriz[0,2], "\n")
print("Tamaño de la matriz")
print(matriz.ndim, "\n")
print("Tamaño (x , y)")
print(matriz.shape, "\n")
print("Multiplicación entre matrices unidimencionales")
print(np.dot(matriz,matriz), "\n")
print("Multiplicación entre matrices polidimencionales")
print(np.dot(matriz1,matriz2), "\n")