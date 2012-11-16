
#We use a dual-headed dictionary so we can do reverse-lookups easily
locations = {
	"B1": 24,
	"B2": 23,
	"B3": 22,
	"B4": 21,
	"B5": 20,
	"B6": 19,
	"B7": 18,
	"B8": 17,
	"B9": 16,
	"B10": 15,
	"B11": 14,
	"B12": 13,
	"R1": 1,
	"R2": 2,
	"R3": 3,
	"R4": 4,
	"R5": 5,
	"R6": 6,
	"R7": 7,
	"R8": 8,
	"R9": 9,
	"R10": 10,
	"R11": 11,
	"R12": 12,
	"B_BAR":0,
	"R_BAR":25,
	"B_BEAR_OFF": 26,
	"R_BEAR_OFF": 27,
	# Reverse look-up section
	24: "B1",
	23: "B2",
	22: "B3",
	21: "B4",
	20: "B5",
	19: "B6",
	18: "B7",
	17: "B8",
	16: "B9",
	15: "B10",
	14: "B11",
	13: "B12",
	1: "R1",
	2: "R2",
	3: "R3",
	4: "R4",
	5: "R5",
	6: "R6",
	7: "R7",
	8: "R8",
	9: "R9",
	10: "R10",
	11: "R11",
	12: "R12",
	0: "B_BAR",
	25: "R_BAR",
	26: "B_BEAR_OFF",
	27: "R_BEAR_OFF"}
	
def distance(locFrom, locTo):
    #Computes the distance between locFrom and locTo
    if locTo == "R_BEAR_OFF":
	return -	1*locations[locFrom]
    if locTo == "B_BEAR_OFF":
	return 25 - locations[locFrom]
    return locations[locTo] - locations[locFrom]

def findLocation(p, locFrom, dist):
    #Computes a new location given a starting location and a distance, direction depends on the color p of the player
    if locFrom == "B_BAR":
	toIndex = dist
    elif locFrom == "R_BAR":
	toIndex = 25 - dist
    else:
         if p == "RED":
             pSign = -1
         elif p == "BLACK":
             pSign = 1
         else:
             pSign = 0
	toIndex = locations[locFrom] + pSign * dist
	
    if toIndex <= 0:
	toIndex = locations["R_BEAR_OFF"]
    elif toIndex >= 25:
	toIndex = locations["B_BEAR_OFF"]
    else:
	toIndex = toIndex
    locTo = locations[toIndex]
    return locTo
	    
