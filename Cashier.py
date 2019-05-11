import random
import time
from Article import WeightArticle, PieceArticle, WeightArticlesList, PieceArticlesList
from threading import Timer

class Cashier:
  def __init__(self):
    self._articlesList = []
    self._articlesAmount = 0
    self._currentArticle = None
    self._currentArticleAmount = 0
    self._lastArticleId = 0
    self._scannedArticlesAmount = 0
    self._articlesToScan = 0
    self._time = time.time()
    self._isReadyForWeigh = False

    self.generateArticlesList()
    self.generateSingleArticle()

  def setView(self, view):
    self._view = view

  def setArticlesToScan(self, value):
    self._articlesToScan = value

  def generateArticlesList(self):
    self._articlesAmount = random.randint(10, 20)
    for i in range(0, self._articlesAmount):
      if i < self._articlesAmount / 2:
        self._articlesList.append(WeightArticle(WeightArticlesList[random.randint(0, 9)]))
      else:
        self._articlesList.append(PieceArticle(PieceArticlesList[random.randint(0, 9)]))

  def generateSingleArticle(self):
    self._isReadyForWeigh = False
    if self._lastArticleId < self._articlesAmount:
      self._currentArticle = self._articlesList[self._lastArticleId]
      self._lastArticleId += 1
      if self._currentArticle._isPieceArticle:
        self._currentArticleAmount = self.generateRandomArticleAmount()
      else:
        self._currentArticleAmount = '?kg'
    else:
      self.lose()

  def resetCurrentArticle(self):
    self._currentArticle = None
    self._currentArticleAmount = 0

  def generateRandomArticleAmount(self):
    if random.randint(0, 1) % 2:
      return random.randint(1, 50)
    else:
      return 1

  def onArticleClick(self):
    if self._currentArticle._isPieceArticle:
      self.pieceArticle()
    else:
      self._isReadyForWeigh = True

  def pieceArticle(self):
    self._currentArticle.setArrivalTime(time.time())
    self._currentArticleAmount -= self._articlesToScan
    self._scannedArticlesAmount += self._articlesToScan
    self._view.rightView._amountInput.delete(0, 'end')
    self._view.rightView._amountInput.insert(0, 1)
    self.refresh()
    if self._currentArticleAmount == 0:
      self._currentArticle.setDeleteTime(time.time())
      self.refresh()
      self.generateSingleArticle()
      self.refresh()
    elif self._currentArticleAmount < 0:
      return self.lose()
    self._view.leftView.articleInfo()

  def weighArticle(self):
    if self._currentArticle._isPieceArticle:
      self.lose()
    if self._isReadyForWeigh:
      self._currentArticleAmount = (random.randint(5, 200)) / 100
      self._scannedArticlesAmount += 1
      self._currentArticle.setDeleteTime(time.time())
      self._view.leftView.articleInfo()

      r = Timer(0, self.refresh)
      s = Timer(1.0, self.genAndRefresh)
      r.start()
      s.start() 

  def lose(self):
    print('Loser')
    self._view.leftView.loseInfo()
    self._view.leftView.timeInfo(time.time() - self._time)

  def refresh(self):
    self._view.leftView.newItem()
    
  def genAndRefresh(self):
    self.generateSingleArticle()
    self._view.leftView.newItem()
