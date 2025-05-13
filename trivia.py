# trivia_funciones.py

def obtener_preguntas():
    return [
        {
            "pregunta": "¿Qué función se utiliza para obtener la longitud de una lista en Python?",
            "opciones": ["a) size()", "b) length()", "c) len()", "d) count()"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué palabra clave se utiliza para manejar excepciones en Python?",
            "opciones": ["a) try", "b) catch", "c) throw", "d) except"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Cómo se define una función en Python?",
            "opciones": ["a) function nombre()", "b) def nombre():", "c) func nombre()", "d) define nombre()"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué operador se utiliza para la división entera en Python?",
            "opciones": ["a) /", "b) //", "c) %", "d) div"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué estructura se utiliza para almacenar pares clave-valor en Python?",
            "opciones": ["a) list", "b) tuple", "c) dict", "d) set"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué palabra clave se utiliza para crear una clase en Python?",
            "opciones": ["a) class", "b) def", "c) create", "d) object"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Qué método se utiliza para agregar un elemento a una lista en Python?",
            "opciones": ["a) append()", "b) add()", "c) insert()", "d) push()"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Qué operador lógico representa 'y' en Python?",
            "opciones": ["a) and", "b) or", "c) not", "d) &&"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Qué módulo se utiliza para generar números aleatorios en Python?",
            "opciones": ["a) random", "b) math", "c) os", "d) sys"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Qué función se utiliza para convertir un string en un entero en Python?",
            "opciones": ["a) int()", "b) str()", "c) float()", "d) parseInt()"],
            "respuesta": "a"
        }
    ]

def mostrar_pregunta(numero, pregunta_info):
    print(f"\nPregunta {numero}: {pregunta_info['pregunta']}")
    for opcion in pregunta_info["opciones"]:
        print(opcion)

def obtener_respuesta():
    while True:
        respuesta = input("Tu respuesta (a/b/c/d): ").lower()
        if respuesta in ["a", "b", "c", "d"]:
            return respuesta
        else:
            print("❗Respuesta inválida. Elegí entre a, b, c o d.")

def evaluar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario == respuesta_correcta:
        print("✅ ¡Correcto!\n")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta correcta era '{respuesta_correcta}'.\n")
        return False

def mostrar_resultado_final(puntaje, total):
    print(f"\n🧾 Tu puntaje final es: {puntaje} de {total}")

    if puntaje == total:
        print("🏆 ¡Excelente! Sos un crack de Python.")
    elif puntaje >= 3:
        print("👍 ¡Bien hecho! Vas por buen camino.")
    else:
        print("💡 A seguir practicando. ¡Vos podés!")

def jugar_trivia():
    print("🎮 Bienvenido al Juego de Trivia de Python 🎮")
    preguntas = obtener_preguntas()
    puntaje = 0

    for i, pregunta in enumerate(preguntas, 1):
        mostrar_pregunta(i, pregunta)
        respuesta = obtener_respuesta()
        if evaluar_respuesta(respuesta, pregunta["respuesta"]):
            puntaje += 1

    mostrar_resultado_final(puntaje, len(preguntas))

# Punto de entrada del programa
if __name__ == "__main__":
    jugar_trivia()
# Este código es un juego de trivia simple en Python. El jugador responde preguntas y recibe un puntaje al final.

