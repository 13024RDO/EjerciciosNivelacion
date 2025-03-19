import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje(event):
    # Muestra el mensaje cuando presionas Enter
    messagebox.showinfo("Mensaje", caja.get())

def cambiar_color():
    global indice_color
    colores = [
        ("white", "black"),  
        ("black", "white"),  
        ("lightblue", "red")  
    ]
    
    caja.config(bg=colores[indice_color][0], fg=colores[indice_color][1])
    
    # Incrementar el índice para el siguiente color
    indice_color = (indice_color + 1) % len(colores)


# Crea ventana
ventana = tk.Tk()
ventana.title("Ejercicio Caja de Texto")
ventana.geometry("300x150")  # Tamaño de la ventana
ventana.config(bg="lightgray")

# Crear encabezado con Label
encabezado = tk.Label(ventana, text="Caja de Texto", font=("Arial", 16, "bold"))
encabezado.pack(pady=10)  # Colocamos el encabezado con un margen

# Crea Caja de texto
caja = tk.Entry(ventana, font=("Arial", 12), width=25)
caja.pack(pady=20)
caja.bind("<Return>", mostrar_mensaje)  # Detecta cuando se presiona Enter

# Crea Botón para cambiar colores
indice_color = 0
tk.Button(ventana, text="Cambiar Color caja de texto", command=cambiar_color).pack()

ventana.mainloop()
