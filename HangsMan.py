import random

with open("palabras.txt", "r") as datos:
    
    lista_palabras = []
    
    for linea in datos:
        lista_palabras = ((linea.split(",")))
    
    cantidad_de_palabras = len(lista_palabras)
    posicion = random.randrange(0,cantidad_de_palabras)

    palabra_oculta = []

    """ Acá se guarda el largo de la palabra con "x" y muestra en consola las mismas """
    for x in lista_palabras[posicion]:
        palabra_oculta.append("x")
    for x in palabra_oculta:
        print(x, end = " ")

    
    print(" ")
    
    no_acierto = True
    posicion_letra = 0
    palabra = ""
    while no_acierto:
        letra = input("Inserte Letra:")

        for x in lista_palabras[posicion]:
            
            if letra == x:
                palabra_oculta[posicion_letra] = letra
            
            posicion_letra = posicion_letra + 1 

        for x in palabra_oculta:
            print(x, end = " ")   

        print(" ")

        if palabra != lista_palabras[posicion]:
            palabra = ""
            for x in palabra_oculta:
                palabra = palabra + x
                
        if palabra == lista_palabras[posicion]:
            no_acierto = False
            print("Ah adivinado la Letra :D")
             
        posicion_letra = 0 

    

    

