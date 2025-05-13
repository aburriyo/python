#Repetir hasta que lo hagan bien 
#podemos usar un bucle junto con try 

def pedir_numero_repetido():
    while True:
        try:
            numero =int(input("Escribe un numero entero:"))
            print("!Gracias Tu numero es:", numero)
            break
        except ValueError:
            print("Eso no es un numero valida.")

pedir_numero_repetido()
            
