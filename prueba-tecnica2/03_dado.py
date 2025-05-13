import random

total = random.randint(1,6)+ random.randint(1,6)

adivinanza =int(input("¿Cual es el total (2-12):?"))

while adivinanza != total:
    adivinanza =int(input("¿Cual es el total (2-12):?"))
    
print("Lo adivinaste!")


