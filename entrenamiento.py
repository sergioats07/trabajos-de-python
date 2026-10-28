# Lista de ejemplo provista en el ejercicio
lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]

# Diccionario vacío para guardar los resultados
diccionario = {}

# Recorremos cada número de la lista
for numero in lista:
    # .get(numero, 0) busca el número; si no existe, devuelve 0 y le sumamos 1
    diccionario[numero] = diccionario.get(numero, 0) + 1

print(diccionario)