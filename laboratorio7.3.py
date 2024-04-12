import serial
import tkinter as tk

# Crear la instancia de Serial
puerto_serie = serial.Serial('COM3', 9600)

def leer_potenciometro():
    valor = puerto_serie.readline().decode().strip()  # Leer valor del puerto serie
    if valor and valor.isdigit():  # Verificar si hay algún valor recibido y si es un número válido
        valor_potenciometro.set(int(valor))  # Actualizar la variable asociada al valor del potenciómetro
        actualizar_grafica()  # Actualizar la gráfica
        contador_valor.config(text="Valor del potenciómetro: " + valor)  # Actualizar contador
    root.after(10, leer_potenciometro)  # Llamar recursivamente a la función después de 10ms

def actualizar_grafica():
    canvas.delete("todo")  # Eliminar gráfica anterior
    valor = valor_potenciometro.get()  # Obtener valor del potenciómetro
    
    # Crear árbol binario con 5 círculos a la izquierda de la barra
    x_base = 150
    y_base = 100
    radio = 20
    for i in range(5):
        x = x_base + i * 50
        y = y_base + i * 50
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="green", tags="todo")

    # Crear barra en el lado derecho
    ancho_barra = 30
    altura_barra = valor / 1023 * 300  # Escalar valor del potenciómetro para que quepa en el lienzo
    canvas.create_rectangle(750 - ancho_barra, 50 + (300 - altura_barra), 750, 350, fill="blue", tags="todo")  # Crear nueva gráfica

# Función para manejar el evento del botón "InOrden"
def in_orden():
    print("Recorrido InOrden")

# Función para manejar el evento del botón "PostOrden"
def post_orden():
    print("Recorrido PostOrden")

# Función para manejar el evento del botón "PreOrden"
def pre_orden():
    print("Recorrido PreOrden")

# Crear ventana principal de tkinter
root = tk.Tk()
root.title("Lectura de Potenciómetro")

# Variable para almacenar el valor del potenciómetro
valor_potenciometro = tk.IntVar()

# Configurar lienzo para la gráfica
canvas = tk.Canvas(root, width=1000, height=600, bg="white")
canvas.pack()

# Crear título
titulo = tk.Label(root, text="Laboratorio 3 de Arduino Programación III", font=("Arial", 18, "bold"))
titulo.place(relx=0.25, rely=0.05, anchor="center")

# Crear label para mostrar el valor del potenciómetro
contador_valor = tk.Label(root, text="Valor del potenciómetro: ", font=("Arial", 16))
contador_valor.place(relx=0.75, rely=0.05, anchor="center")

# Crear contador label
contador = tk.Label(root, text="", font=("Arial", 16))
contador.place(relx=0.75, rely=0.15, anchor="center")

# Crear botones
boton_in_orden = tk.Button(root, text="InOrden", command=in_orden, font=("Arial", 14))
boton_in_orden.place(relx=0.3, rely=0.9, anchor="center")

boton_post_orden = tk.Button(root, text="PostOrden", command=post_orden, font=("Arial", 14))
boton_post_orden.place(relx=0.5, rely=0.9, anchor="center")

boton_pre_orden = tk.Button(root, text="PreOrden", command=pre_orden, font=("Arial", 14))
boton_pre_orden.place(relx=0.7, rely=0.9, anchor="center")

# Llamar a la función para leer el potenciómetro
leer_potenciometro()

# Ejecutar el bucle principal de tkinter
root.mainloop()

# Cerrar el puerto serie al finalizar
puerto_serie.close()
