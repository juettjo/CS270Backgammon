class Color:
  """Color represents a color of a player or checker
  Use: Color(<string>)
  
  Color provides following methods
      getSign
      """
  def __init__(self,color):
    self.RED, self.NONE, self.BLACK = -1, 0, 1
    if color == "RED":
      self.sign = -1
    elif color == "NONE":
      self.sign = 0
    else: #BLACK
      self.sign = 1
    
  def getSign(self):
    """returns the numerical value of the current color-
	Red = -1
	None = 0
	Black = 1"""
    return self.sign
    
  def getColorFromNumerical(self,value):
    if value < 0:
      return self.RED
    if value > 0:
      return self.BLACK
    return self.NONE
    
  def __str__(self):
    if self.sign == self.RED:
      return "RED"
    if self.sign == self.BLACK:
      return "BLACK"
    return "NONE"