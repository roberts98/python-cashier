import tkinter as tk
from RightView import RightView
from LeftView import LeftView
from Summary import Summary

class Window:
    def __init__(self, controller):
        self._window = tk.Tk()
        self._controller = controller
        # ustawianie parametrów okna
        self._window.title('Kasjer')
        self._window.iconbitmap('icon.ico')
        self._window.geometry('1000x550')
        bg = tk.PhotoImage(file='bg.gif')
        background_label = tk.Label(self._window, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = bg

        self.rightView = RightView(self._window, controller)

        self.leftView = LeftView(self._window, controller)

        self.summary = Summary(controller)


    def start(self):
        self._window.mainloop()

    def destroy(self):
        self._window.destroy()
        self.summary.start()
