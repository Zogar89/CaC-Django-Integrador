# Ejercicios integradores para revisar en la clase 7

# 1. Escribir una función que calcule el máximo común divisor entre dos números.

import math  # Importar el módulo math
a = math.gcd(72, 60)  # Usar la función gcd()
print(a)  # Imprimir el resultado

# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

a = math.lcm(72, 60) # Usar la función lcm()
print(a) # Imprimir el resultado

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena): # Definir la función contar_palabras
    palabras = cadena.split() # Separar la cadena en una lista de palabras
    contador = {} # Crear un diccionario vacío
    for palabra in palabras: # Recorrer la lista de palabras
        frecuencia = contador.get(palabra, 0) # Obtener la frecuencia actual o cero
        frecuencia += 1 # Sumar uno a la frecuencia
        contador[palabra] = frecuencia # Asignar la nueva frecuencia como valor
    return contador # Devolver el diccionario

Muchachos='''En Argentina nací
Tierra del Diego y Lionel
De los pibes de Malvinas
Que jamás olvidaré
No te lo puedo explicar
Porque no vas a entender
Las finales que perdimos
Cuantos años la lloré
Pero eso se terminó
Porque en el Maracaná
La final con los brazucas
La volvió a ganar papá
Muchachos
Ahora nos volvimos a ilusionar
Quiero ganar la tercera
Quiero ser campeón mundial
Y al Diego
Desde el cielo lo podemos ver
Con Don Diego y La Tota
Alentándolo a Lionel
Muchachos
Ahora nos volvimos a ilusionar
Quiero ganar la tercera
Quiero ser campeón mundial
Y al Diego
Desde el cielo lo podemos ver
Con Don Diego y La Tota
Alentándolo a Lionel, y ser campeones otra vez, y ser campeones otra vez'''

resultado = contar_palabras(Muchachos) # Llamar a la función con una cadena
print(resultado) # Imprimir el resultado

#4 Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def obtener_palabra_mas_repetida(diccionario): # Definir la función obtener_palabra_mas_repetida
    palabra_mas_repetida = "" # Crear una variable para almacenar la palabra más repetida
    frecuencia_mas_repetida = 0 # Crear una variable para almacenar su frecuencia
    for palabra, frecuencia in diccionario.items(): # Recorrer el diccionario
        if frecuencia > frecuencia_mas_repetida: # Comparar las frecuencias
            palabra_mas_repetida = palabra # Actualizar la palabra más repetida
            frecuencia_mas_repetida = frecuencia # Actualizar su frecuencia
    resultado = (palabra_mas_repetida, frecuencia_mas_repetida) # Crear una tupla con los resultados
    return resultado # Devolver la tupla

resultado = obtener_palabra_mas_repetida(resultado)
print(resultado) # Imprimir el resultado
