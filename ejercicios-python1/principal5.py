"""
    @roberto n 
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellido": "Elizalde"}
diccionario2 = {"nombre": "Roberto", "apellido": "Narvaez"}

lista = [diccionario, diccionario2]

print("Imprimir diccionario")
for l in lista:
	midiccionario = l

	print("Mi nombre es: %s y mi apellido es: %s" \
		%(midiccionario["nombre"], midiccionario["apellido"]))