#liza molina
#me duele mi ojito

respuesta = input ('¿Estas cansado? (sí / no):').strip().lower()

cansado = respuesta == 'sí'

if not cansado:
    print('!Es hora de programar')

else:
    print('Tómate un descanso, lo necesitas')