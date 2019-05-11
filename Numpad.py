import tkinter as tk

class Numpad:
  def __init__(self, window, view):
    row = 0
    column = 3
    for i in range(10):
      tk.Button(window, text=i, command=lambda i = i: view._amountInput.insert(tk.END, i)).grid(row=row, column=column)
      if not i % 3 and i != 0:
        row += 1
      if column == 6:
        column = 3
      column += 1