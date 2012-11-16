#Names:

from Color import *
from Location import *

class GameImpl:
  """GameImpl represents a game of HotGammon
  
  GameImpl provides following methods:
      newGame
      nextTurn
      getPlayerInTurn
      getNumberOfMovesLeft
      diceThrown
      diceValuesLeft
      getColor
      getCount
      _setBoard
      canOverBearOff
      noPiecesInOuterTable
      
    and takes in definitions for these methods to satisfy the requirements of different specifications:
      winner
      move"""
      
  def __init__(self):
      self.rolledValues = []

  def newGame(self):
      """Starts a new game- Creates new board with no player in turn"""
      
      self.turns = 0
      self.player = "NONE"
      self.board = {
	#Location : [Color,Number of pieces]
	"B1": ["RED",2],
	"B2": ["NONE",0],
	"B3": ["NONE",0],
	"B4": ["NONE",0],
	"B5": ["NONE",0],
	"B6": ["BLACK",5],
	"B7": ["NONE",0],
	"B8": ["BLACK",3],
	"B9": ["NONE",0],
	"B10":["NONE",0],
	"B11":["NONE",0],
	"B12":["RED",5],
	"R1": ["BLACK",2],
	"R2": ["NONE",0],
	"R3": ["NONE",0],
	"R4": ["NONE",0],
	"R5": ["NONE",0],
	"R6": ["RED",5],
	"R7": ["NONE",0],
	"R8": ["RED",5],
	"R9": ["NONE",0],
	"R10": ["NONE",0],
	"R11": ["NONE",0],
	"R12": ["BLACK",5],
	"B_BAR": ["NONE",0],
	"R_BAR": ["NONE",0],
	"B_BEAR_OFF": ["NONE",0],
	"R_BEAR_OFF": ["NONE",0]}

  def nextTurn(self):
    """Increments turn- Changes player and rolls dice"""
    
    #Roll Dice
    listRolls = [[1,2],[3,4],[5,6]]
    self.turns = self.turns + 1
    self.rolledValues = listRolls[(self.turns + 2)%3]    

	
    if self.player.getSign() == 0: #If there's no player in turn, black begins
	self.player = "BLACK"
    else:
	#Otherwise, switch players
	if self.player.__str__() == "BLACK":
	    self.player = "RED"
	    
	elif self.player.__str__() == "RED":
	    self.player = "BLACK"
	
  def getPlayerInTurn(self):
    """returns the color object representing the player in turn"""
    return self.player
    
  def getNumberOfMovesLeft(self):
    """Returns the number of moves from rolling you have left"""
    return len(self.rolledValues)	
    
  def diceThrown(self):	#Does not roll dice
    """Returns the values rolled from dice"""
    return self.rolledValues
    
  def diceValuesLeft(self):
    return self.rolledValues
    
  def getColor(self, location):
    """Returns the color of a given location"""
    return self.board[location][0].__str__()
    
  def getCount(self, location):
    """Returns the number of pieces on a given location"""
    return self.board[location][1]
    
  def _setBoard(self, boardDictionary):
    """Sets the board configuration according to boardDictionary"""
    self.board = boardDictionary
    
  def noPiecesInOuterTable(self,color):
    """Returns True if there are no locations owned by color in the outer table, otherwise returns false. Color should be a string 'RED' or 'BLACK'."""
    ans = True
    if color == "RED":
      for i in range(7,13): #If there is a Red piece in 6-13, ans = false
	ans = ans and self.board["R" + str(i)][0].__str__() != "RED"
      for i in range(1,13):
	ans = ans and self.board["B" + str(i)][0].__str__() != "RED"
      ans = ans and self.board["R_BAR"][0].__str__() != "RED"
      
    else: # color == "BLACK" (Should never be "NONE")
      for i in range(7,13):
	ans = ans and self.board["B" + str(i)][0].__str__() != "BLACK"
      for i in range(1,13):
	ans = ans and self.board["R" + str(i)][0].__str__() != "BLACK"
      ans = ans and self.board["B_BAR"][0].__str__() != "BLACK"
    return ans
    
  def canOverBearOff(self,color,locNum):
    """Returns True if there are no locations in the inner table owned by color further from bearing off , otherwise returns False. Color should be a string 'RED' or 'BLACK'."""
    checkingNums = range(6, locNum +1, -1)
    
    for target in checkingNums:
      targColor = self.board[color[0] + str(target)][0]
      if targColor.__str__() == color: #If there is a color there, there is a colored piece there. If that color is ours, we cannot overbear
	return False
    return True
      
  def nextTurn(self):
    """Increments turn- Changes player and rolls dice"""
    
    #Roll Dice
    listRolls = [[1,2],[3,4],[5,6]]
    self.turns = self.turns + 1
    self.rolledValues = listRolls[(self.turns + 2)%3]
    
  	
    if self.player.getSign() == 0: #If there's no player in turn, black begins
	self.player = "BLACK"
    else:
	#Otherwise, switch players
	if self.player.__str__() == "BLACK":
	    self.player = "RED"
	    
	elif self.player.__str__() == "RED":
	    self.player = "BLACK"
	
  def move(self, fromLocation, toLocation):
    """Checks if a move is legal and changes position of a checker"""
    
    #Checks for illegal- so far only if opponent's pieces in tolocation
    moverColor = self.getColor(fromLocation)
    dist = distance(fromLocation,toLocation)
    
    # The player in turn color and checker color must match to move
    if self.player.__str__() == moverColor.__str__():
    
    #If the destination is ours or empty or occupied by only one checker
      if self.getColor(toLocation) == "NONE" or self.getColor(toLocation) == moverColor or self.board[toLocation][1] == 1: 

	#Checks if we are moving forward
	if self.player.getColorFromNumerical(dist) == self.player.getSign() :
	  
	  #We can bear off if there are no pieces in the outer table and we are moving to the bear-off
	  bearingOff = self.noPiecesInOuterTable(self.player.__str__()) and toLocation == 	self.player.__str__()[0]+"_BEAR_OFF"
	  
	  #Stops us from bearing off if it's not legal
	  if (not bearingOff) and ("_BEAR_OFF" in toLocation):
	    return False
	  
	  #If distance we move is in the rolledValues or we can legally bear off
	  bearingRoll = max(self.rolledValues)
	  if abs(dist) in self.rolledValues or (bearingOff and bearingRoll > abs(dist) and self.canOverBearOff(self.player.__str__(), int(fromLocation[1:]))):
	    
	    # If moving onto a single opponent's piece
	    if self.board[toLocation][0].getSign() == -self.player.getSign() and self.board[toLocation][1] == 1:
	      
	      # Find the color of the opponent and put the checker on his bar.
	      if self.board[toLocation][0].__str__() ==  "BLACK":
		self.board["B_BAR"][0] = "BLACK"
		self.board["B_BAR"][1] = self.board["B_BAR"][1] + 1
	      else:
		self.board["R_BAR"][0] = "RED"
		self.board["R_BAR"][1] = self.board["R_BAR"][1] + 1
	      # Then remove the opponent's checker from this location.
	      # Movement can then treated as to a "NONE" location.
	      self.board[toLocation][0] = "NONE"
	      self.board[toLocation][1] = 0
	      
	    #Deals with piece movement
	    if bearingOff and not abs(dist) in self.rolledValues:#If we're over-bearing off, remove the larger value from the rolls
	      self.rolledValues.remove(bearingRoll)
	    else:#Otherwise, remove whatever our distance was
	      self.rolledValues.remove(abs(dist))	#Remove the value from pool
	      
	    self.board[fromLocation][1] = self.board[fromLocation][1] - 1
	    self.board[toLocation][1] = self.board[toLocation][1] + 1
	    self.board[toLocation][0] = self.player
	    
	    #If the last piece on a location moves, the color is going to be None
	    if self.board[fromLocation][1] == 0:
	      self.board[fromLocation][0] = "NONE"
	    return True   
    # If all conditions are not met no move is made and False returns
    return False
    
  def getPlayerInTurn(self):
    """returns the color object representing the player in turn"""
    return self.player
    
  def getNumberOfMovesLeft(self):
    """Returns the number of moves from rolling you have left"""
    return len(self.rolledValues)	
    
  def diceThrown(self):	#Does not roll dice
    """Returns the values rolled from dice"""
    return self.rolledValues
    
  def diceValuesLeft(self):
    return self.rolledValues
    
  def winner(self):
    """Checks to see if there is a winner"""
    
    #Red always wins after six turns
    if self.turns == 6:
      return "RED"
    else:
      return "NONE"
    
  def getColor(self, location):
    """Returns the color of a given location"""
    return self.board[location][0].__str__()
    
  def getCount(self, location):
    """Returns the number of pieces on a given location"""
    return self.board[location][1]
    
  def _setBoard(self, boardDictionary):
    """Sets the board configuration according to boardDictionary"""
    self.board = boardDictionary
    
  def noPiecesInOuterTable(self,color):
    """Returns True if there are no locations owned by color in the outer table, otherwise returns false. Color should be a string 'RED' or 'BLACK'."""
    ans = True
    if color == "RED":
      for i in range(7,13): #If there is a Red piece in 6-13, ans = false
	ans = ans and self.board["R" + str(i)][0].__str__() != "RED"
      for i in range(1,13):
	ans = ans and self.board["B" + str(i)][0].__str__() != "RED"
      ans = ans and self.board["R_BAR"][0].__str__() != "RED"
      
    else: # color == "BLACK" (Should never be "NONE")
      for i in range(7,13):
	ans = ans and self.board["B" + str(i)][0].__str__() != "BLACK"
      for i in range(1,13):
	ans = ans and self.board["R" + str(i)][0].__str__() != "BLACK"
      ans = ans and self.board["B_BAR"][0].__str__() != "BLACK"
    return ans
    
  def canOverBearOff(self,color,locNum):
    """Returns True if there are no locations in the inner table owned by color further from bearing off , otherwise returns False. Color should be a string 'RED' or 'BLACK'."""
    checkingNums = range(6, locNum +1, -1)
    
    for target in checkingNums:
      targColor = self.board[color[0] + str(target)][0]
      if targColor.__str__() == color: #If there is a color there, there is a colored piece there. If that color is ours, we cannot overbear
	return False
    return True
    
class AlphaMon(GameImpl):
  """An implementation of a HotGammon Game meeting the AlphaMon specifications."""
  def move(self, fromLocation, toLocation):
    """Checks if a move is legal and changes position of a checker"""
    
    self.rolledValues = self.rolledValues[:-1]	#Decrements number of moves
    
    #Checks for illegal- so far only if opponent's pieces in tolocation
    moverColor = self.getColor(fromLocation)
    
    # The player in turn color and checker color must match to move
    if self.player.__str__() == moverColor.__str__():

    #If the destination is ours or empty
      if self.getColor(toLocation) == "NONE" or self.getColor(toLocation) == moverColor:
	self.board[fromLocation][1] = self.board[fromLocation][1] - 1
	self.board[toLocation][1] = self.board[toLocation][1] + 1
	#If the last piece on a location moves, the color is going to be None
	if self.board[fromLocation][1] == 0:
	  self.board[fromLocation][0] = "NONE"
	return True   
    # If all conditions are not met no move is made and False returns
    return False
    
  def winner(self):
    """Checks to see if there is a winner"""
    
    #Red always wins after six turns
    if self.turns == 6:
      return "RED"
    else:
      return "NONE"
  
class BetaMon(GameImpl):
  """An implementation of a HotGammon Game meeting the BetaMon specifications."""
  def move(self, fromLocation, toLocation):
    """Checks if a move is legal and changes position of a checker"""
    
    #Checks for illegal- so far only if opponent's pieces in tolocation
    moverColor = self.getColor(fromLocation)
    dist = distance(fromLocation,toLocation)
    
    # The player in turn color and checker color must match to move
    if self.player.__str__() == moverColor.__str__():
    
    #If the destination is ours or empty or occupied by only one checker
      if self.getColor(toLocation) == "NONE" or self.getColor(toLocation) == moverColor or self.board[toLocation][1] == 1: 

	#Checks if we are moving forward
	if self.player.getColorFromNumerical(dist) == self.player.getSign() :
	  
	  #We can bear off if there are no pieces in the outer table and we are moving to the bear-off
	  bearingOff = self.noPiecesInOuterTable(self.player.__str__()) and toLocation == 	self.player.__str__()[0]+"_BEAR_OFF"
	  
	  #Stops us from bearing off if it's not legal
	  if (not bearingOff) and ("_BEAR_OFF" in toLocation):
	    return False
	  
	  #If distance we move is in the rolledValues or we can legally bear off
	  bearingRoll = max(self.rolledValues)
	  if abs(dist) in self.rolledValues or (bearingOff and bearingRoll > abs(dist) and self.canOverBearOff(self.player.__str__(), int(fromLocation[1:]))):
	    
	    # If moving onto a single opponent's piece
	    if self.board[toLocation][0].getSign() == -self.player.getSign() and self.board[toLocation][1] == 1:
	      
	      # Find the color of the opponent and put the checker on his bar.
	      if self.board[toLocation][0].__str__() ==  "BLACK":
		self.board["B_BAR"][0] = "BLACK"
		self.board["B_BAR"][1] = self.board["B_BAR"][1] + 1
	      else:
		self.board["R_BAR"][0] = "RED"
		self.board["R_BAR"][1] = self.board["R_BAR"][1] + 1
	      # Then remove the opponent's checker from this location.
	      # Movement can then treated as to a "NONE" location.
	      self.board[toLocation][0] = "NONE"
	      self.board[toLocation][1] = 0
	      
	    #Deals with piece movement
	    if bearingOff and not abs(dist) in self.rolledValues:#If we're over-bearing off, remove the larger value from the rolls
	      self.rolledValues.remove(bearingRoll)
	    else:#Otherwise, remove whatever our distance was
	      self.rolledValues.remove(abs(dist))	#Remove the value from pool
	      
	    self.board[fromLocation][1] = self.board[fromLocation][1] - 1
	    self.board[toLocation][1] = self.board[toLocation][1] + 1
	    self.board[toLocation][0] = self.player
	    
	    #If the last piece on a location moves, the color is going to be None
	    if self.board[fromLocation][1] == 0:
	      self.board[fromLocation][0] = "NONE"
	    return True   
    # If all conditions are not met no move is made and False returns
    return False
    
    def winner(self):
      """Checks to see if there is a winner"""
      
      #Red always wins after six turns
      if self.turns == 6:
	return "RED"
      else:
	return "NONE"
      
class GammaMon(GameImpl):
  """An implementation of a HotGammon Game meeting the GammaMon specifications."""
  def move(self, fromLocation, toLocation):
    """Checks if a move is legal and changes position of a checker"""
    
    self.rolledValues = self.rolledValues[:-1]	#Decrements number of moves
    
    #Checks for illegal- so far only if opponent's pieces in tolocation
    moverColor = self.getColor(fromLocation)
    
    # The player in turn color and checker color must match to move
    if self.player.__str__() == moverColor.__str__():
      # We should either not be bearing off or be able to bear off.
      if (not "_BEAR_OFF" in toLocation) or self.noPiecesInOuterTable(self.player.__str__()):
	#If the destination is ours or empty
	if self.getColor(toLocation) == "NONE" or self.getColor(toLocation) == moverColor:
	  self.board[fromLocation][1] = self.board[fromLocation][1] - 1
	  self.board[toLocation][1] = self.board[toLocation][1] + 1
	  
	  #If the last piece on a location moves, the color is going to be None
	  if self.board[fromLocation][1] == 0:
	     self.board[fromLocation][0] = "NONE"
	  return True   
    # If all conditions are not met no move is made and False returns
    return False
    
  def winner(self):
    """Checks to see if there is a winner"""
    
      #Checks each player BEAR_OFF for all 15 pieces of their color
    spaces = iter(self.board)
    noBlacks = True
    noReds = True
    for space in spaces:
      if self.board[space][0].__str__() == "BLACK" and space != "B_BEAR_OFF":
	noBlacks = False	
      if self.board[space][0].__str__() == "RED" and space != "R_BEAR_OFF":
	noReds = False	
    if noBlacks:
      return "BLACK"
    elif noReds:
      return "RED"
    return "NONE"