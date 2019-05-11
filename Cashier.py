import random
import time
from Article import WeightArticle, PieceArticle, WeightArticlelsList, PieceArticlesList

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

    self.generateArticlesList()
    self.generateSingleArticle()

  def setView(self, view):
    self._view = view

  def setArticlesToScan(self, value):
    self._articlesToScan = value

  def generateArticlesList(self):
    self._articlesAmount = random.randint(10, 20)
    for i in range(0, self._articlesAmount):
      # if i < self._articlesAmount / 2:
      # self._articlesList.append(WeightArticle(PieceArticlesList[random.randint(0, 9)]))
      # else:
      self._articlesList.append(PieceArticle(WeightArticlelsList[random.randint(0, 9)]))

  def generateSingleArticle(self):
    if self._lastArticleId < self._articlesAmount:
      self._currentArticle = self._articlesList[self._lastArticleId]
      self._currentArticleAmount = self.generateRandomArticleAmount()
      self._currentAticleOriginalAmount = self._currentArticleAmount
      self._lastArticleId += 1
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

  def scanArticle(self):
    self._currentArticle.setArrivalTime(time.time())
    if (self._currentArticle._isPieceArticle):
      self._currentArticleAmount -= self._articlesToScan
      self._scannedArticlesAmount += self._articlesToScan
      self._view.rightView._amountInput.delete(0, 'end')
      self._view.rightView._amountInput.insert(0, 1)
      self._view.leftView.newItem()
      if self._currentArticleAmount == 0:
        self._currentArticle.setDeleteTime(time.time())
        self._view.leftView.newItem()
        self.generateSingleArticle()
        self._view.leftView.newItem()
      elif self._currentArticleAmount < 0:
        return self.lose()
    else:
      self._currentArticle.setWeight(random.randint(5, 200)) 
      self._scannedArticlesAmount += 1
      self.generateSingleArticle()
      self._currentArticle.setDeleteTime(time.time())
    print(self._scannedArticlesAmount)
    self._view.leftView.articleInfo()

  def lose(self):
    print('Loser')
    self._view.leftView.timeInfo(time.time() - self._time)

