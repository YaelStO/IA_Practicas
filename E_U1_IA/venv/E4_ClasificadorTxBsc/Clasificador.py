import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Datos de entrenamiento (Ejemplo: comentarios clasificados)
textos = [
    "Me encanta este producto, es increíble",  # Positivo
    "Es una porquería, no lo recomiendo",  # Negativo
    "Muy útil y funciona perfectamente",  # Positivo
    "No sirve para nada, pésima calidad",  # Negativo
    "Estoy muy feliz con esta compra",  # Positivo
    "Terrible, me arrepiento de comprarlo",  # Negativo
]

etiquetas = ["positivo", "negativo", "positivo", "negativo", "positivo", "negativo"]

# Convertir texto en números con TF-IDF y entrenar el modelo
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(textos, etiquetas)

# Probar el modelo con un texto nuevo
nuevo_texto = ["Este producto es no es bueno, lo odio"]
prediccion = modelo.predict(nuevo_texto)

print(f"Predicción: {prediccion[0]}")
