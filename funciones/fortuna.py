
import random

opciones = [
    'No persigas la felicidad, créala.'
    'Todas las cosas son difíciles antes de ser fáciles.'
    'El pájaro madrugador consigue el gusano, pero el segundo ratón se lleva el queso.'
    'Alguien en tu vida necesita una carta de tu parte.'
    'No solo pienses. ¡Actúa!'
    'Tu corazón se acelerará.'
    'La fortuna que buscas está en otra galleta.'
    '¡Ayuda! ¡Estoy prisionero en una panadería china!'
]

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])

fortuna()
fortuna()
fortuna()