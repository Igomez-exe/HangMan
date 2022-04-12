import random

with open("palabras.txt", "r") as datos:
    
    valores = []
    
    for linea in datos:
        valores = ((linea.split(",")))
    
    cantidad_de_palabras = len(valores)
    posicion = random.randrange(0,cantidad_de_palabras)
    """print(valores[posicion])"""

    almacenar_x = []
    for x in valores[posicion]:
        almacenar_x.append("x")
    for x in almacenar_x:
        print(x, end = " ")

    
    print("")
    
    no_acertar = True
    algo = True
    posicion_letra = 0
    cadena = ""
    while no_acertar:
        letra = input("Inserte Letra:")

        for x in valores[posicion]:
            
            if letra == x:
                almacenar_x[posicion_letra] = letra
            
            posicion_letra = posicion_letra + 1 

        

        for x in almacenar_x:
            print(x, end = " ")    
        print(" ")

        
        if cadena != valores[posicion]:
            cadena = ""
            for x in almacenar_x:
                cadena = cadena + x
        """print(cadena)"""
        if cadena == valores[posicion]:
            no_acertar = False
            print("Ah adivinado la Letra :D")
             
        posicion_letra = 0 

    

    

