import tkinter as tk

class Numpad:
  def __init__(self, window, view):
    row = 0
    column = 8
    for i in range(10):
      tk.Button(window, text=i, pady=10, padx=10, command=lambda i = i: view._amountInput.insert(tk.END, i)).grid(row=row, column=column)
      if not i % 3 and i != 0:
        row += 1
      if column == 11:
        column = 8
      column += 1
