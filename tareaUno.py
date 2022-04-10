import random

with open("palabras.txt", "r") as datos:
    valores = []
    
    for linea in datos:
        valores = ((linea.split(",")))
    
    print(valores)
    cantidad_de_palabras = len(valores)
    posicion = random.randrange(0,cantidad_de_palabras)
    print(posicion)
    print(valores[posicion])
    otros_valores = valores[posicion]

    for x in valores[posicion]:
        print("x",end = " ")
    
    print("")
    
    no_acertar = True
    while no_acertar:
        letra = input("Inserte Letra:")
        for x in valores[posicion]:
            print("x",end = " ")
            if letra in valores[posicion]:
                print(otros_valores)
            
        no_acertar = False
        print("sissiisi")


    