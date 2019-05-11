import tkinter as tk

class LeftView:
  def __init__(self, window, controller):
    self._window = window
    print (controller._currentArticle._name)