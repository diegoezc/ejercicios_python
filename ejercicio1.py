#Objetivo1: Crear comentarios
# este es mi primer ejercicio comentario de una sola linea
"""este es un comentario de multiples linas"""

nro_con=6 #Continentes
nro_pai=195 #Paises
nro_est=23 #Estados de Venezuela
nro_ciu=100 #Nuemero de ciudades
nro_zon=1 #Zona Horaria

#Declarando variables Reales
pro_vid=71.1 #promedio de vida
tas_cam=29.21 #tasa de Cambio
por_imp=16.00

#Declarando Cadenas

nom_pai="Venezuela"
cap_pai='Caracas'
des_pai="""Venezuela es un pais de la costanosrte de America del Sur con diversas atracciones naturales.
tiene Montañas, Desiertos, selvas; y Llanuras"""

#Declarando Buleanos

num_bei=True
num_fut=False

#Datos importntes

num_hab, cti_pai, fec_ind = 30000000, "+58",1811

"""Objetivo N3: funciones BASICAS
- print para imprimir
-input para pedir datos a usuario
-float para convertir un string a real
"""
print ("hola Mundo")

"""Objetivo 4: Inferencia de datos"""

print ("en Sur america se encuenta %s cuya capital es %s y tiene %d estados"%(nom_pai,cap_pai,nro_est))

print ("El promedio de vida en {} es de {} años" .format(nom_pai,pro_vid))

print(f" El numero de habitantes de {nom_pai} es de {num_hab} millones")

print(f"LA tasa de cambio para {nom_pai} es de {tas_cam}")

#funcion input para pedir datos

print ("Ingrese la tasa de cambio de hoy: ")
tas_cam=input()
print(f"la tasa de cambio para {nom_pai} es de {tas_cam}")

print("Ingrese el precio del diplomado en dolares")
pre_dip=input()
print(f"Desea factura legas? S/N")
fac_leg=input().upper()

pre_vef=float(tas_cam)*float(pre_dip)

if fac_leg=="S":
    iva_vef=pre_vef*(por_imp/100)#Porcentaje de Impuesto
    bas_imp=pre_vef-iva_vef #Impuesto Imponible
    print(f""" 
    El precio del diplomado tiene un precio en Bs de: {pre_vef}
    La base Imponible es de :{bas_imp}
    El impuesto a pagar es de:{iva_vef}""")
else:
    print(f" El precio del diplomado en Bs es de: {pre_vef}")

