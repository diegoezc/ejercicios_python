"""clase 3: aprender a usar
1. ciclos for in
2.while"""
#objetivo 1: while

paises=['Venezuela','Colombia','Brasil','España','Argentina','Italia']

nro_pai=len(paises)
print(f"El número de países es {nro_pai}")

con=0
while con<nro_pai:
    print("impimiendo el pais numero",con,paises[0])
    con=con+1
else:
    print('Ya no hay más elementos en la lista')

#objetivo numero 2: cilco for

paises=['Venezuela','Colombia','Brasil','España','Argentina','Italia']

con=0

for nom_pai in paises:
    print("los paises de mi lista son:",nom_pai)

#ejercicio

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

for val_mun in mundo.values():
    print("los valores del diccionario son", val_mun)

    