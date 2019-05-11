import tkinter as tk

class LeftView:
  def __init__(self, window, controller):
    self._window = window
    self._controller = controller
    string = self._controller._currentArticle._name + ' ' + str(self._controller._currentArticleAmount)

    self._article = tk.Button(self._window, text=string, command=lambda: self._controller.scanArticle())
    self._article.grid(row=2, column=0, columnspan=10)
    self.newItem()
    self.articleInfo()

  def newItem(self):
    self._article.destroy()
    string = self._controller._currentArticle._name + ' ' + str(self._controller._currentArticleAmount)

    self._article = tk.Button(self._window, text=string, command=lambda: self._controller.scanArticle())
    self._article.grid(row=2, column=0)
    # pass

  def loseInfo(self):
    font = ('times', 20, 'bold')
    self._lose = tk.Label(self._window, text='Przegrales', bg='#abc', fg='white', font=font)
    self._lose.grid(row=3, column=0)

  def articleInfo(self):
    string = 'Skasowanych towarów ' + str(self._controller._scannedArticlesAmount)
    self._info = tk.Label(self._window, text=string)
    self._info.grid(row=4)

  def timeInfo(self, time):
    string = 'czas ' + str(time)
    self._time = tk.Label(self._window, text=string)
    self._time.grid(row=5)