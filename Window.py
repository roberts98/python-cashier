import tkinter as tk

class Window:
    def __init__(self):
        self._window = tk.Tk()
        # ustawianie parametrów okna
        self._window.title('Kasjer')
        self._window.iconbitmap('icon.ico')
        self._window.geometry('500x500')

    def start(self):
        self._window.mainloop()
