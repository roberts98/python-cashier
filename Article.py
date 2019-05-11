class Article:
  def __init__(self):
    self._arrivalTime = 0
    self._deleteTime = 0

  def setArrivalTime(self, time):
    self._arrivalTime = time

  def setDeleteTime(self, time):
    self._deleteTime = time

class WeightArticle(Article):
  def __init__(self, name):
    super(WeightArticle, self).__init__()
    self._isPieceArticle = False
    self._name = name
    self._weight = 0

  def setWeight(self, weight):
    self._weight = weight

class PieceArticle(Article):
  def __init__(self, name):
    super(PieceArticle, self).__init__()
    self._isPieceArticle = True
    self._name = name

PieceArticlesList = ['Baton', 'Chipsy', 'Chleb', 'Bulki', 'Woda', 'Pepsi', 'Sok', 'Sól', 'Cukier', 'Mąka']
WeightArticlesList = ['Ziemniaki', 'Pomidory', 'Arbuzy', 'Banany', 'Jabłka', 'Gruszki', 'Cebula', 'Czosnek', 'Rabarbar', 'Smoczy Owoc']
