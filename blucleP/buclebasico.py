print("\n Ejercicio 1. Basico")
for i in range(101):
    print(f"Numero actual :{i}")

print("\n Ejercicio 2. multiple")
for i in range(2,501, 2):
    print(i)
    
print("\n Ejercicio 3. Vanilla Ice")
for i in range(1,101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 ==0:
        print("Ice Ice")
    else:
        print(i)
        
print("\n Ejercicio 4. Numero gigante.")
suma_total = 0
for i in range(0, 500001, 2):
    suma_total += i
print(suma_total)

print("\n Ejercicio 5. de 3 en 3.")
for i in range(2024,0,-3):
    print(i)
    
print("\n Ejercicio 6. multiplo")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal +1):
    if i % multiplo == 0:
        print(i)