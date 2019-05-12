import tkinter as tk

class LeftView:
  def __init__(self, window, controller):
    self._window = window
    self._controller = controller
    self.newItem()

    self._nextClient = tk.Button(window, text="nastepny klient", pady=10, padx=10, command=lambda: controller.start())
    self._nextClient.grid(row=2, column=0)

  def newItem(self):
    if hasattr(self, '_article'):
      self._article.destroy()
    if self._controller._currentArticle:
      string = self._controller._currentArticle._name + ' ' + str(self._controller._currentArticleAmount)

      self._article = tk.Button(self._window, text=string, pady=10, padx=10, command=lambda: self._controller.onArticleClick())
      self._article.grid(row=2, column=0)
    # pass

  def bigAlert(self, text):
    self._alert = tk.Label(self._window, text=text, font=('times', 25))
    self._alert.grid(row=8, column=4)

  def removeAlert(self):
    self._alert.destroy()