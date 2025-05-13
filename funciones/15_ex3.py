#mostrar un elemento de una lista por su posición, manejando si la 
#posición no existe

def mostrar_elemento():
    frutas = ["manzana","banana", "naranja", "palta"]
    try:
        indice =int(input("elige una posición (0 a 3):"))
        print("fruta elegida:", frutas[indice])
    except IndexError:
        print("Esta posición no existe en la lista")
    except ValueError:
        print("Debes ingresar número")
        
mostrar_elemento()
        