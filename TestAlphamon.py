import unittest
from GameImpl import *
from Color import Color

class TestAlphamon(unittest.TestCase):
  
  def setUp(self):
    self.game = AlphaMon()
    self.game.newGame()
        
  def test_shouldHaveNoPlayerInTurnAfterNewGame(self):
    self.assertEquals("NONE", self.game.getPlayerInTurn().__str__())
    
  def test_shouldHaveBlackPlayerInTurnAfterNewGame(self):
    self.game.nextTurn()
    self.assertEquals("BLACK", self.game.getPlayerInTurn().__str__())
    
  def test_firstRollGivesOneAndTwo(self):    
    self.game.nextTurn()
    self.assertEquals(self.game.diceThrown(),[1,2])
  
  def test_secondRollGivesThreeAndFour(self):    
    self.game.nextTurn()
    self.game.nextTurn()
    self.assertEquals(self.game.diceThrown(),[3,4])  
  
  def test_thirdRollGivesFiveAndSix(self):    
    self.game.nextTurn()
    self.game.nextTurn()
    self.game.nextTurn()
    self.assertEquals(self.game.diceThrown(),[5,6])
  
  def test_fourthRollGivesOneAndTwo(self):    
    self.game.nextTurn()
    self.game.nextTurn()
    self.game.nextTurn()
    self.game.nextTurn()
    self.assertEquals(self.game.diceThrown(),[1,2])
    
  def test_shouldHaveTwoMovesAfterRolling(self):    
    self.game.nextTurn()
    rolls = self.game.diceValuesLeft()
    self.assertEquals(len(rolls), 2)
    
  def test_shouldUseMethodToGiveBackTwoMovesLeftAfterRolling(self):    
    self.game.nextTurn()
    self.assertEquals(self.game.getNumberOfMovesLeft(),2)
    
  def test_shouldHaveOneMoveLeftAfterMoving(self):   
    self.game.nextTurn()
    self.game.move("B1","B2")
    self.assertEquals(self.game.getNumberOfMovesLeft(),1)

  ###################################################################
  # Testing starting board configuration

  # Each test case checks the color and number of checkers
  # at a given location.

  # Test Black side

  def test_shouldGetRedAnd2FromB1(self):    
    self.assertEquals(self.game.getColor("B1"),"RED")
    self.assertEquals(self.game.getCount("B1"),2)
    
  def test_shouldGetNoneAnd0FromB2(self):    
    self.assertEquals(self.game.getColor("B2"),"NONE")
    self.assertEquals(self.game.getCount("B2"),0)
    
  def test_shouldGetNoneAnd0FromB3(self):    
    self.assertEquals(self.game.getColor("B3"),"NONE")
    self.assertEquals(self.game.getCount("B3"),0)
    
  def test_shouldGetNoneAnd0FromB4(self):    
    self.assertEquals(self.game.getColor("B4"),"NONE")
    self.assertEquals(self.game.getCount("B4"),0)
    
  def test_shouldGetNoneAnd0FromB5(self):    
    self.assertEquals(self.game.getColor("B5"),"NONE")
    self.assertEquals(self.game.getCount("B5"),0)
    
  def test_shouldGetBlackAnd5FromB6(self):    
    self.assertEquals(self.game.getColor("B6"),"BLACK")
    self.assertEquals(self.game.getCount("B6"),5)
    
  def test_shouldGetNoneAnd0FromB7(self):    
    self.assertEquals(self.game.getColor("B7"),"NONE")
    self.assertEquals(self.game.getCount("B7"),0)
    
  def test_shouldGetBlackAnd3FromB8(self):    
    self.assertEquals(self.game.getColor("B8"),"BLACK")
    self.assertEquals(self.game.getCount("B8"),3)
    
  def test_shouldGetNoneAnd0FromB9(self):    
    self.assertEquals(self.game.getColor("B9"),"NONE")
    self.assertEquals(self.game.getCount("B9"),0)
    
  def test_shouldGetNoneAnd0FromB10(self):    
    self.assertEquals(self.game.getColor("B10"),"NONE")
    self.assertEquals(self.game.getCount("B10"),0)
    
  def test_shouldGetNoneAnd0FromB11(self):    
    self.assertEquals(self.game.getColor("B11"),"NONE")
    self.assertEquals(self.game.getCount("B11"),0)
    
  def test_shouldGetRedAnd5FromB12(self):    
    self.assertEquals(self.game.getColor("B12"),"RED")
    self.assertEquals(self.game.getCount("B12"),5)
    
# Test Red side
    
  def test_shouldGetBlackAnd2FromR1(self):    
    self.assertEquals(self.game.getColor("R1"),"BLACK")
    self.assertEquals(self.game.getCount("R1"),2)
    
  def test_shouldGetNoneAnd0FromR2(self):    
    self.assertEquals(self.game.getColor("R2"),"NONE")
    self.assertEquals(self.game.getCount("R2"),0)
    
  def test_shouldGetNoneAnd0FromR3(self):    
    self.assertEquals(self.game.getColor("R3"),"NONE")
    self.assertEquals(self.game.getCount("R3"),0)
    
  def test_shouldGetNoneAnd0FromR4(self):   
    self.assertEquals(self.game.getColor("R4"),"NONE")
    self.assertEquals(self.game.getCount("R4"),0)
    
  def test_shouldGetNoneAnd0FromR5(self):    
    self.assertEquals(self.game.getColor("R5"),"NONE")
    self.assertEquals(self.game.getCount("R5"),0)
    
  def test_shouldGetRedAnd5FromR6(self):   
    self.assertEquals(self.game.getColor("R6"),"RED")
    self.assertEquals(self.game.getCount("R6"),5)
    
  def test_shouldGetNoneAnd0FromR7(self):    
    self.assertEquals(self.game.getColor("R7"),"NONE")
    self.assertEquals(self.game.getCount("R7"),0)
    
  def test_shouldGetRedAnd3FromR8(self):   
    self.assertEquals(self.game.getColor("R8"),"RED")
    self.assertEquals(self.game.getCount("R8"),3)
    
  def test_shouldGetNoneAndFromR9(self):   
    self.assertEquals(self.game.getColor("R9"),"NONE")
    self.assertEquals(self.game.getCount("R9"),0)
    
  def test_shouldGetNoneAnd0FromR10(self):   
    self.assertEquals(self.game.getColor("R10"),"NONE")
    self.assertEquals(self.game.getCount("R10"),0)
    
  def test_shouldGetNoneAnd0FromR11(self):    
    self.assertEquals(self.game.getColor("R11"),"NONE")
    self.assertEquals(self.game.getCount("R11"),0)
    
  def test_shouldGetBlackAnd5FromR12(self):   
    self.assertEquals(self.game.getColor("R12"),"BLACK")
    self.assertEquals(self.game.getCount("R12"),5)
    
###########################################################
    
  def test_redShouldWinAfter6Turns(self):     
     self.game.nextTurn()
     self.game.nextTurn()
     self.game.nextTurn()
     self.game.nextTurn()
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertTrue(self.game.winner())
    
  def test_shouldAllowMoveFromRedToRed(self):   
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertTrue(self.game.move("R6", "R8"))
    
  def test_shouldAllowMoveFromRedToEmpty(self):  
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertTrue(self.game.move("R6", "R7"))
    
  def test_shouldNotAllowMoveFromRedToBlack(self):   
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertFalse(self.game.move("R6", "B6"))
    
  def test_shouldNotAllowRedToMoveOnBlacksTurn(self):
     self.game.nextTurn()
     self.assertFalse(self.game.move("R6", "R7"))
    
  def test_shouldNotAllowRedToMoveBlackPieces(self):
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertFalse(self.game.move("B6", "B7"))
    
  def test_boardConfigurationShouldChangeOnMove(self):
     self.game.nextTurn()
     self.game.nextTurn()
     self.assertEquals(self.game.getCount("R6"),5)
     self.assertEquals(self.game.getCount("R7"),0)
     self.assertTrue(self.game.move("R6", "R7"))
     self.assertEquals(self.game.getCount("R6"),4)
     self.assertEquals(self.game.getCount("R7"),1)
    
    
    
    