import numpy as np

# Definir los conceptos (nodos)
conceptos = ["Perro", "Mamífero", "Animal", "Cuatro patas", "Ladrido"]

# Crear una matriz de adyacencia (5x5) inicializada en 0
matriz_adyacencia = np.zeros((len(conceptos), len(conceptos)), dtype=int)

# Definir las relaciones usando índices
relaciones = {
    ("Perro", "Mamífero"): 1,   # Perro es un Mamífero
    ("Mamífero", "Animal"): 1,  # Mamífero es un Animal
    ("Perro", "Cuatro patas"): 1,  # Perro tiene Cuatro patas
    ("Perro", "Ladrido"): 1  # Perro emite Ladrido
}

# Llenar la matriz de adyacencia
for (concepto1, concepto2), valor in relaciones.items():
    i, j = conceptos.index(concepto1), conceptos.index(concepto2)
    matriz_adyacencia[i, j] = valor

# Función para mostrar relaciones de un nodo específico
def mostrar_relaciones(concepto):
    if concepto in conceptos:
        index = conceptos.index(concepto)
        relaciones = [conceptos[i] for i in range(len(conceptos)) if matriz_adyacencia[index, i] == 1]
        print(f"Relaciones de '{concepto}': {', '.join(relaciones)}")
    else:
        print("Concepto no encontrado.")

# Mostrar la matriz de adyacencia
print("Matriz de Adyacencia:")
print(matriz_adyacencia)

# Mostrar relaciones de "Perro"
mostrar_relaciones("Perro")
