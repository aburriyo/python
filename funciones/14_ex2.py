#division segura 

#objetivo dividir entre 2 numeros y evitar o alertar 
#si el usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input("ingresa un numero:"))
        num2 = int(input("Ingresa otro numero:"))
        resultado = num1 / num2
        print("el resultado de la division es:", resultado)
    except ZeroDivisionError:
        print("Lo sentimos no se puede realizar esta división")
    except ValueError:
        print("Error. solo debes ingresar numeros") 
        
division_segura()