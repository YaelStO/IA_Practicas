import numpy as np

# Definir los conceptos (nodos)
conceptos = ["Perro", "Mamífero", "Animal", "Cuatro patas", "Ladrido"]

# Crear una matriz de adyacencia (5x5) inicializada en 0
matriz_adyacencia = np.zeros((len(conceptos), len(conceptos)), dtype=int)

# Definir las relaciones usando índices
relaciones = {
    ("Perro", "Mamífero"): 1,
    ("Mamífero", "Animal"): 1,
    ("Perro", "Cuatro patas"): 1,
    ("Perro", "Ladrido"): 1
}

# Llenar la matriz de adyacencia
for (concepto1, concepto2), valor in relaciones.items():
    i, j = conceptos.index(concepto1), conceptos.index(concepto2)
    matriz_adyacencia[i, j] = valor

# Mostrar la matriz de adyacencia
print("Matriz de Adyacencia:")
print(matriz_adyacencia)