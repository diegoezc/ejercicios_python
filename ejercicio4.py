"""Objetivo 4: Aprender a usar funciones

#Objetico 1 funcion simple

def bienvenido():
    print("¡Bienvenid@! a mi red social")

bienvenido()

#Objetivo 2 Funbcion con parametros fijos

def calcular_precio_bs(tc,pd):
    pre_bol=float(tc)*float(pd)
    return pre_bol

print("Por favor ingresa la tasa de cambio")
tas_cam=input()

print("Por favor ingrese el precio en USD")
pre_dol=input()

pre_bs=calcular_precio_bs(tas_cam,pre_dol)

print("el valor en bs es de :",pre_bs)"""

def mostrar_paises_clasificados(confederacion, *paises):
    for pai in paises:
        print ("Pais clasificado al mundial:",pai,"de",confederacion)

mostrar_paises_clasificados("America del Sur","Brasil","Argentina","Ecuador","Uruguay")
mostrar_paises_clasificados("Europa","Serbia","Dinamarca","España","Paises bajos","Suiza","Coracia")
