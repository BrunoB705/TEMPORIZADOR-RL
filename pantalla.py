import tkinter as tk
import time

def mostrar_ventana(root):
    inicio = time.time()
    def actualizar_cronometro(widget):
        tiempo_transcurrido = time.time() - inicio
        # widget.config(text=f"Tiempo restante: {tiempo_transcurrido:.2f}") TENGO ESTA OPCION O LA DE ABAJO ELEGIR UNA
        widget.config(text=f"{tiempo_transcurrido:.2f}",font=("Arial",25))
        if tiempo_transcurrido < 1.3:
            widget.after(100, lambda: actualizar_cronometro(lTimer))
        else:
            widget.destroy()
    lTimer = tk.Label(root)
    lTimer.pack(pady=20)
    
    actualizar_cronometro(lTimer)

def borrar_ventana(root):
    for widget in root.winfo_children():
        widget.destroy()
