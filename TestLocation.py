import unittest
from Location import *
from Color import *

class TestLocation(unittest.TestCase):
    
    def test_shouldHaveProperNames(self):
        print locations["B1"]
	self.assertEquals( "B1", locations[locations["B1"]])
	self.assertEquals( "B5", locations[locations["B5"]])
	self.assertEquals( "R12", locations[locations["R12"]])
	self.assertEquals( "R4", locations[locations["R4"]])
	self.assertEquals( "B_BEAR_OFF", locations[locations["B_BEAR_OFF"]])
	self.assertEquals( "R_BEAR_OFF", locations[locations["R_BEAR_OFF"]])
	self.assertEquals( "R_BAR", locations[locations["R_BAR"]])
	self.assertEquals( "B_BAR", locations[locations["B_BAR"]])
	
    def test_shouldCalculateDistanceCorrectly(self):
	self.assertEquals(1, distance("B2", "B1"))
	self.assertEquals(-1, distance("B1", "B2"))
	self.assertEquals(-1, distance("R2", "R1"))
	self.assertEquals(1, distance("R1", "R2"))
	self.assertEquals(6, distance("B8", "B2"))
	self.assertEquals(3, distance("R10", "B12"))
	self.assertEquals(-5, distance("B11", "R9"))
	
    def test_shouldCalculateBarDistanceCorrectly(self):
	self.assertEquals(-3, distance("R_BAR", "B3"))
	self.assertEquals(4, distance("B_BAR", "R4"))

    def test_shouldCalculateBearOffDistanceCorrectly(self):
	self.assertEquals(4, distance("B4", "B_BEAR_OFF"))
	self.assertEquals(-6, distance("R6", "R_BEAR_OFF"))
	
    def test_shouldFindProperLocationBasedOnDistance(self):
	self.assertEquals("B6", findLocation(Color("RED"), "B2", 4))
	self.assertEquals("B2", findLocation(Color("BLACK"), "B6", 4))
	self.assertEquals("B_BEAR_OFF", findLocation(Color("BLACK"), "B2",4))
	self.assertEquals("B_BEAR_OFF", findLocation(Color("BLACK"), "B2", 6))
	self.assertEquals("R_BEAR_OFF", findLocation(Color("RED"), "R2", 6))
	self.assertEquals("R3", findLocation(Color("BLACK"), "B_BAR", 3))
	self.assertEquals("B6", findLocation(Color("RED"), "R_BAR", 6))
	self.assertEquals("B10", findLocation(Color("BLACK"), "R10", 5))
	self.assertEquals("R10", findLocation(Color("RED"), "B10", 5))

    def test_shouldIterateThrough28Locations(self):
	count = 0
	for l in locations:
	    if type("string") == type(l):
	      	count = count + 1
		self.assertTrue( l != None)
	self.assertEquals(28, count)
	
	
