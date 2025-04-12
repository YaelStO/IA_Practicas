# Paso 1: Importar librerías
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Paso 2: Cargar los datos
iris = load_iris()
X = iris.data  # Características: largo/ancho de pétalo y sépalo
y = iris.target  # Clases: 0=setosa, 1=versicolor, 2=virginica

# Paso 3: Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Paso 4: Crear y entrenar el modelo probabilístico
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# Paso 5: Realizar predicciones
y_pred = modelo.predict(X_test)

# Paso 6: Ver precisión
print("Precisión:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# Paso 7: Mostrar probabilidades (confidence scores)
print("\nProbabilidades de predicción para las primeras 5 muestras:")
probs = modelo.predict_proba(X_test[:5])
print(np.round(probs, 3))  # Redondeamos para mejor visualización

# Paso 8 (opcional): Mostrar predicción final con probabilidad máxima
for i, prob in enumerate(probs):
    clase = iris.target_names[np.argmax(prob)]
    print(f"Muestra {i+1}: Predicción = {clase}, Confianza = {np.max(prob):.2f}")

