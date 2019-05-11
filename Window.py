import tkinter as tk
from RightView import RightView
from LeftView import LeftView

class Window:
    def __init__(self, controller):
        self._window = tk.Tk()
        self._controller = controller
        # ustawianie parametrów okna
        self._window.title('Kasjer')
        self._window.iconbitmap('icon.ico')
        self._window.geometry('500x500')

        self._window.bind('<Key>', lambda event: controller.keyPressed(event.char))

        self.rightView = RightView(self._window, controller)

        self.leftView = LeftView(self._window, controller)


    def start(self):
        self._window.mainloop()
