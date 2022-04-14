import random

def dibujar_monigote(numero_intentos):
    print("")

    if(numero_intentos == 6):
        print(" O")
        
    if (numero_intentos == 4):
        print("\\")
    elif (numero_intentos >= 4):
        print("\\", end = "")

    if (numero_intentos >=5):
        print(" /")
    
    if (numero_intentos >= 3):
        print(" |")

    if numero_intentos == 1 :
        print("/")
    else: 
        print("/", end = "")

    if (numero_intentos >= 2):
        print(" \\")
    

with open("palabras.txt", "r") as datos:
    
    lista_palabras = []
    
    for linea in datos:
        lista_palabras = ((linea.split(",")))
    
    cantidad_de_palabras = len(lista_palabras)
    posicion = random.randrange(0,cantidad_de_palabras)

    palabra_oculta = []

    """ Acá se guarda el largo de la palabra con "x" y muestra en consola las mismas """
    for x in lista_palabras[posicion]:
        palabra_oculta.append("X")
    for x in palabra_oculta:
        print(x, end = " ")

    
    print(" ")
    
    encontro_letra = False
    intentos = 0

    no_acierto = True
    posicion_letra = 0
    palabra = ""
    while no_acierto:
        letra = input("Inserte Letra:")

        for x in lista_palabras[posicion]:
            
            if letra == x:
                palabra_oculta[posicion_letra] = letra
                encontro_letra =  True

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
             
        if  not encontro_letra:
            intentos = intentos + 1 
            dibujar_monigote(intentos)
        else:
            encontro_letra = False

        if (intentos == 6):
            print("")
            print("Ah perdido :'( ")
            print("")
            break

        posicion_letra = 0 
        
    


