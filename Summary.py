import tkinter as tk

class Summary:
  def __init__(self, controller):
    self._window = tk.Tk()
    self._controller = controller
    # ustawianie parametrów okna
    self._window.title('Kasjer')
    self._window.iconbitmap('icon.ico')
    self._window.geometry('200x200')

  def start(self):
    self._window.mainloop()

  def loseInfo(self):
    font = ('times', 20, 'bold')
    self._lose = tk.Label(self._window, text='Koniec gry', bg='#abc', fg='white', font=font)
    self._lose.grid(row=3, column=0)

  def articleInfo(self):
    string = 'Skasowanych towarów ' + str(self._controller._scannedArticlesAmount)
    self._info = tk.Label(self._window, text=string)
    self._info.grid(row=4)

  def timeInfo(self, time):
    string = 'Sredni czas ' + str(time)
    self._time = tk.Label(self._window, text=string)
    self._time.grid(row=5)
