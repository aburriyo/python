import random

pregunta = input('Pregunta:')

numero_aletorio = random.randint(1,9)

if numero_aletorio ==1:
    respuesta = 'si, definitivamente' 

elif numero_aletorio ==2:
    respuesta = 'con toda certeza'

elif numero_aletorio ==3:
    respuesta = 'sin duda alguna'

elif numero_aletorio ==4:
    respuesta = 'respuesta confusa, intente nuevamente'

elif numero_aletorio ==5:
    respuesta = 'pregunta mas tarde'

elif numero_aletorio ==6:
    respuesta = 'mejor no decirlo ahora'

elif numero_aletorio ==7:
    respuesta = 'mis fuentes dicen no'

elif numero_aletorio ==8:
    respuesta = 'la perspectiva no es muy buena'

elif numero_aletorio ==9:
    respuesta = 'muy dudo'

else:
    respuesta= 'error'


print('bola 8: '+ respuesta)
