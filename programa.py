#programa para genera un numero entero en pyton 
import random
#La funcion input () captura datos desde el teclado 
# como si fuera una cadena de texto(string)
a= input("limite inferior")
b= input("limite superior")

#convertir a y b a enteros 
a= int(a)
b= int(b)
respuesta= random.randint (a,b)
print (respuesta)

