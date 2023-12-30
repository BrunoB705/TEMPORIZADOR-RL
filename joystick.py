import pygame
from threading import Thread
import tkinter as tk
from pantalla import mostrar_ventana
from pantalla import borrar_ventana

continuar_joystick = True

def iniciar_aplicacion():
    root = tk.Tk()
    root.title("TIMER RL")
    root.geometry("100x100")

    pygame.init()
    pygame.joystick.init()
        
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick_thread = Thread(target=joystick_monitor, args=(root,))
    joystick_thread.start()

    root.protocol("WM_DELETE_WINDOW", lambda: cerrar_programa(root))
    root.attributes("-topmost", True)
    root.mainloop()

def cerrar_programa(root):
    global continuar_joystick
    continuar_joystick = False
    root.destroy()

def joystick_monitor(root):
    while continuar_joystick:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # BOTON A
                    # print("Boto A presionado") DESCOMENTAR PARA VER EN CONSOLA
                    borrar_ventana(root)
                    root.after(1, mostrar_ventana, root)

    # SI EL WHILE FINALIZA ENTONCES SE APAGAN LOS MODULOS DE PYGAME Y DEL PYGAME.JOYSTICK
    pygame.joystick.quit()
    pygame.quit()
if __name__ == "__main__":
    iniciar_aplicacion()
