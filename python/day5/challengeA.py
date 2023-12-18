inputFile = "../../inputs/day5/input.txt"



def getFromMap(mapRangeLines, key):
  outId = -1
  for rl in mapRangeLines:
    outId = checkIfKeyInRangeLine(key, rl)
    if outId > -1:
      return outId
  
  return key

def checkIfKeyInRangeLine(key, rangeLine): #returns -1 if not in range
  end = rangeLine[0]
  start = rangeLine[1]
  width = rangeLine[2]
  if start <= key < start + width:
    # print("        in range", end, start, width, "in", key, "out", end + (key-start))
    return end + (key-start)
  else: 
    return -1

def parseMapDef(mapDefString): #returns: (srcStr,destStr), map
  mapDefLines = mapDefString.split("\n")
  mapTypeSplit = mapDefLines[0].split(" ")[0].split("-")
  rangeLines = [[int(n) for n in rl.split(" ")] for rl in mapDefLines[1:]]
  stageMap = rangeLines
  
  return (mapTypeSplit[0], mapTypeSplit[-1]), stageMap

def parseInput(inputString):
  inputBlocks = inputString.split("\n\n")
  mapDefs = [parseMapDef(mds) for mds in inputBlocks[1:]]

  startSeeds = [int(s) for s in inputBlocks[0].split(": ")[1].split(" ")]

  return mapDefs, startSeeds


def convertSeed(seed, mapDefs):
  translatedId = seed
  
  for toFrom, stageMap in mapDefs:
    translatedId = getFromMap(stageMap, translatedId)
    # print("    ", toFrom[1], translatedId, "\n")
  
  return translatedId

def findLowestSeedMap(inputString):
  mapDefs, startSeeds = parseInput(inputString)
  lowestLoc = float("inf")
  for seed in startSeeds:
    # print("convertingSeed ", seed)
    loc = convertSeed(seed, mapDefs)
    if loc < lowestLoc:
      lowestLoc = loc
  
  return lowestLoc


if __name__ == "__main__":

  inputStr = open(inputFile).read()
  lowest = findLowestSeedMap(inputStr)

  print("lowest: ", lowest)