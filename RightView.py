import tkinter as tk
from Numpad import Numpad

class RightView:
  def __init__(self, window, controller):
    self._window = window
    self._controller = controller
    sv = tk.StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv: self.onInputChange(sv.get()))

    font = ('times', 14, 'bold')
    self._amountInput = tk.Entry(self._window, textvariable=sv, width=24, font=font, fg='black', bd=10, justify='center')
    self._amountInput.grid(row=0, column=4)

    self._backspaceButton = tk.Button(self._window, text='backspace', pady=10, padx=10, command=lambda: self._amountInput.delete(len(self._amountInput.get())-1, tk.END))
    self._backspaceButton.grid(row=0, column=5)

    self._clearButton = tk.Button(self._window, text='wyczyść', pady=10, padx=10, command=lambda: self._amountInput.delete(0, tk.END))
    self._clearButton.grid(row=0, column=6)
    
    self._weighButton = tk.Button(self._window, text='zważ', pady=10, padx=10, command=controller.weighArticle)
    self._weighButton.grid(row=0, column=7)

    self._numpad = Numpad(self._window, self)
  
  def onInputChange(self, value):
    if value:
      self._controller.setArticlesToScan(int(value))
