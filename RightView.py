import tkinter as tk
from Numpad import Numpad

class RightView:
  def __init__(self, window, controller):
    self._window = window
    self._controller = controller
    sv = tk.StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv: self.onInputChange(sv.get()))

    # Amount input
    self._amountInput = tk.Entry(self._window, textvariable=sv, width=24)
    self._amountInput.grid(row=0, column=0)

    ###########
    # Buttons #
    ###########

    # Backspace
    self._backspaceButton = tk.Button(self._window, text="backspace", command=lambda: self._amountInput.delete(len(self._amountInput.get())-1, tk.END))
    self._backspaceButton.grid(row=0, column=1)

    # Clear
    self._clearButton = tk.Button(self._window, text="wyczyść", command=lambda: self._amountInput.delete(0, tk.END))
    self._clearButton.grid(row=0, column=2)

    # Numpad START
    self._numpad = Numpad(self._window, self)
    # Numpad END
  
  def onInputChange(self, value):
    if value:
      self._controller.setArticlesToScan(int(value))
