"""Objetivo Numero1: Aprender a usar Listas"""

paises=list() #forma numero 1
paises=[] #forma numero 2
paises=["Venezuela","Colombia","Brasil","España","Argentina","Italia"]

print("paises: ", paises)

print("Pais Numero 2: ",paises[2])

#ordenar paise3s con sort
paises.sort()
print("Piases: ", paises)

#Agregar pais 
paises.append("Uryguay")
print(f"Nuevo Pais agregado {paises}")

#Agregar un Pais con Posicion
paises.insert(2,"Australia")
print(f"paises: {paises}")

#Cosas Interesantes
print("el penultimo pais es: ",paises[-2])

#imprimer un rango de una lista 
print("primero tres paises: ",paises[0:3])

"""Objetivo 2: creacion de tuplas"""

continente=tuple()
continente=("Africa","Asia","Oceania","America","Antartida","Europa")

#Imprimri Tupla
print("Continentes", continente) #Imprimir Continente

print("lo imprime:",continente.count("Europa"),"vez") #Para saber cuantas veces se repite el valor

print("Africa aparace en la posicion:",continente.index("Africa"),"en la tupla") #Para saber en que posicion  esta el valor en la tuppla

print("la tupla contiene: ",len(continente),"espacios") #

print("el continente numero 2 es: ",continente[2])

"""Objetivo num 3: Sets"""

estados=set()
estados={}
estados={"Tachira","Merida","Trujillo","Zulia","Lara","Barinas"}

#imprimir un set

print("los estados de Venezuela son:",estados)
#Agregar
estados.add("Falcon")
print("Los estados de Venezuela son:",estados)

estados.add("Trujillo")
print("Los estados de Venezuela son:",estados)

#para buscar en valor en una tabla
print("Merida" in estados)

"""Objetivo 4: Diccionario"""
mundo=dict()
mundo={
    'nro_con':6,
    'nro_pai':195,
    'nro_per':8000000000,
    'continentes':["Africa","Asia","Oceania","America","Antartida","Europa"],
    "pais":{
        'Argentina':'Buenos Aires',
        'Colombia':'Bogota',
        'Ecuador':'Quito',
        'España':'Madrid',
        'Venezuela':'Caracas',
        }
}

print("Los datos de nuestro planeta:",mundo)

print("el planeta tierra tiene",mundo["nro_per"])

print("el planeta tierra tiene estos continentes:",mundo["continentes"])

print("nostros vivimos en este continente",mundo["continentes"][3])

print("los paises son",mundo["pais"])

print("la capital de Venezuela es :",mundo["pais"]["Venezuela"])

print("las llaves del diccionario son:",mundo.keys())

print("Los valores del diccionario son:",mundo.values())

print("ontiene el diccionario o none si no existe",mundo.get("nro-cont"))