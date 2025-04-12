import numpy as np

# Definimos los datos de entrenamiento (características) y sus etiquetas (clases)
# Características: [vertebrado, sangre_caliente, pelo, plumas, escamas]
X_train = np.array([
    [1, 1, 1, 0, 0],  # Mamífero (Ej: Gato)
    [1, 1, 0, 1, 0],  # Ave (Ej: Águila)
    [1, 0, 0, 0, 1],  # Reptil (Ej: Serpiente)
    [0, 0, 0, 0, 1],  # Pez (Ej: Tiburón)
    [0, 0, 0, 0, 0]   # Insecto (Ej: Hormiga)
])

# Etiquetas correspondientes
y_train = np.array(["Mamífero", "Ave", "Reptil", "Pez", "Insecto"])

# Función para clasificar un nuevo animal usando k-NN (k=1)
def clasificar_animal(nuevo_animal):
    # Calculamos la distancia euclidiana entre el nuevo animal y los datos de entre
    # 
    # 
    # 
    # namiento
    distancias = np.linalg.norm(X_train - nuevo_animal, axis=1)
    
    # Encontramos la posición del menor valor (el vecino más cercano)

    
    indice_min = np.argmin(distancias)
    
    # Devolvemos la etiqueta del animal más cercano
    return y_train[indice_min]

# ---- Pruebas ----
nuevo_animal_1 = np.array([1, 1, 1, 0, 0])  # Similar a un mamífero
nuevo_animal_2 = np.array([1, 1, 0, 1, 0])  # Similar a un ave

print("Clasificación:", clasificar_animal(nuevo_animal_1))  # Debería ser Mamífero
print("Clasificación:", clasificar_animal(nuevo_animal_2))  # Debería ser Ave

