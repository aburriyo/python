#liza molina
#07-04-2025
# fui a ver minecraf

print('BANCO DEL 4°B')

adivinanzas= 0
intentos = 0
 

while adivinanzas != 6 and intentos > 5:
    adivinanzas = int(input('Adivina el numero:'))
    intentos +=1
if adivinanzas !=6:
    print('Te quedaste sin intentos')
else:
    print('Adivinaste')

