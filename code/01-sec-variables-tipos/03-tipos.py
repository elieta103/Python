"""
Tipos de datos
"""

nada = None
cadena = "Hola soy Eliel Herrera"
entero = 99
flotante = 4.2
booleano = False
lista = [1,2,2,3]
listaString = [1, "a", 3]
tuplaNoCambia = ("master", "en", "python")
diccionario ={"id": "1A",
              "nombre": "Juan",
              "depto": "TI"}
rango = range(9)
dato_byte = b"Probando"

#Tipo
print("-------- Inicio tipo de datos ----------")
print(f"{nada} {type(nada)}")
print(f"{cadena} {type(cadena)}")
print(f"{entero} {type(entero)}")
print(f"{flotante} {type(flotante)}")
print(f"{booleano} {type(booleano)}")
print(f"{lista} {type(lista)}")
print(f"{listaString} {type(listaString)}")
print(f"{tuplaNoCambia} {type(tuplaNoCambia)}")
print(f"{diccionario} {type(diccionario)}")
print(f"{rango} {type(rango)}")
print(f"{dato_byte} {type(dato_byte)}")

print("-------- Fin tipo de datos ----------")