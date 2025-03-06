import nltk
from nltk.sem.logic import Expression
# Inicializar el analizador
read_expr = Expression.fromstring
# Definir las constantes para Josue, Israel y Juan
yael = read_expr('yael')
ariel = read_expr('ariel')
juan = read_expr('juan')
#Definir los predicados con las constantes
amigos_yael_ariel = read_expr('amigos (yael, ariel)')
amigos_yael_juan = read_expr('no_son_amigos (yael, juan)')
no_amigos_juan_ariel = read_expr('tienen_la_misma_edad(juan, ariel)')
trabajan_juntos_yael_ariel = read_expr('trabajan (yael, ariel)')
# Crear un conjunto de fórmulas
formulas = [
amigos_yael_ariel,
amigos_yael_juan,
no_amigos_juan_ariel,
trabajan_juntos_yael_ariel
 ]
# Imprimir las fórmulas
for formula in formulas:
    print(f"{formula} : {formula}")