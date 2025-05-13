import tkinter as tk
import random
import time
import threading

# Lista de alumnos
alumnos = [
    "Acevedo Peña Daniel Isaias",
    "Aguirre Parra Cristian Patricio",
    "Alzamora Zorricueta Tomás Justino",
    "Arredondo Contreras Emilia Paz",
    "Cabezas Aliaga Miguel Angel Matías",
    "Cáceres Durán Sofía Carolina",
    "Cayo Cuevas Yanira Belén",
    "Cid Sepulveda Dailyn",
    "Concha Venegas Constanza Belén",
    "Fuentes Manibet Cristofer Alejandro",
    "Fuentes Peña Lissett Constanza",
    "García Guevara Karla Hellen",
    "Gatica Méndez Alonso Gabriel",
    "Gutiérrez Tenorio Tomás Alfredo",
    "Guerrero Hernández Elías Abraham",
    "❌ Jara Belmar Aileen Yarithza",
    "Jara Delgadillo Fernando",
    "Jerez Ríos Dayana Arlette",
    "Medina Pernia Juan Diego",
    "Molinet Navarrete Giovanni Eduardo",
    "Morales Aguilar Brandon Ignacio",
    "Moreno Zapata Vicente Adolfo",
    "Pizarro García Benjamín Ignacio",
    "Poblete Donoso Benjamín Rodrigo",
    "Repol Monje Victoria Estefanía",
    "Rivera Millán Amaro León",
    "Rojas Navarro Jade Alexandra",
    "Rojas Palma Diego Benjamín",
    "Rosales Gallegos Mathias Joaquín",
    "Rubilar Soto Bastián Alexander",
    "Saldaña González Davis Alejandro",
    "Silva Cruz Renato Antonio",
    "Soto Morales Gustavo Alonso",
    "Tapia Concha Pablo Alejandro Andrés",
    "Terán González Tahía Anaís",
    "Toledo Manríquez Madeline Jazmín",
    "Torres Suazo Constanza Noemí",
    "Uribe  Zambrano Alexander Nicolás",
    "Valdez Cifuentes Eyner Alberto",
    "Vargas Fuentes Loreto Ines",
    "Vargas Molina Fabián Ignacio"
]

# Función que simula la ruleta
def girar_ruleta():
    def run():
        boton.config(state="disabled")
        for i in range(30):  # Número de vueltas (más = más lento al final)
            nombre = random.choice(alumnos)
            label_nombre.config(text=nombre)
            ventana.update()
            time.sleep(0.05 + i * 0.01)  # Va frenando
        boton.config(state="normal")

    threading.Thread(target=run).start()  # Para no congelar la interfaz

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ruleta de Alumnos 🎡")
ventana.geometry("600x200")
ventana.resizable(False, False)

# Texto
label_titulo = tk.Label(ventana, text="Haz clic para girar la ruleta", font=("Helvetica", 16))
label_titulo.pack(pady=10)

label_nombre = tk.Label(ventana, text="🎯", font=("Helvetica", 18, "bold"), fg="blue")
label_nombre.pack(pady=10)

boton = tk.Button(ventana, text="GIRAR 🎲", font=("Helvetica", 14), command=girar_ruleta)
boton.pack(pady=10)

# Iniciar la app
ventana.mainloop()
    