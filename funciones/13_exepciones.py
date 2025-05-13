#ejercicio 1 Convensión segura a número

#objetivo: Pedir un numero al usuario y evitar errores si escribe letras.

def pedir_numero ():
    try:
        numero = int(input("Escribe un número entero:"))
        print ("¡Gracias! Tu número es:", numero)
    except ValueError:
        print("Eso no es un numero valido. Intenta otra vez.")
        
pedir_numero()