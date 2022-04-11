import random

with open("palabras.txt", "r") as datos:
    valores = []
    
    for linea in datos:
        valores = ((linea.split(",")))
    
    print(valores)
    cantidad_de_palabras = len(valores)
    posicion = random.randrange(0,cantidad_de_palabras)
    print(valores[posicion])
    otros_valores = valores[posicion]

    almacenar_x = []
    for x in valores[posicion]:
        almacenar_x.append("x")
    for x in almacenar_x:
        print(x, end = " ")

    
    print("")
    
    no_acertar = True
    posicion_letra = 0
    while no_acertar:
        letra = input("Inserte Letra:")
        for x in valores[posicion]:
            
            if letra == x:
                almacenar_x[posicion_letra] = letra
            
            posicion_letra = posicion_letra + 1 
            
            
        no_acertar = False


    for x in almacenar_x:
        print(x, end = " ")