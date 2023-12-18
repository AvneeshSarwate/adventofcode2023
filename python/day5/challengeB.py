import itertools
from itertools import chain

inputFile = "../../inputs/day5/input.txt"


def flatten_chain(ls):
 return list(chain.from_iterable(ls))

def createOutputRanges(inMin, inLen, rangeLine):
  end = rangeLine[0]
  start = rangeLine[1]
  width = rangeLine[2]

  # input is completely below map range
  if inMin+inLen < start:
    return [[inMin, inLen]]


  # input is completely above map range
  if start+width < inMin:
    return [[inMin, inLen]]

  # input is subset of map range
  if start <= inMin and inMin+inLen < start+width:
    return [[end, width]]

  # input is below + intersects map range
  if inMin < start and start <= inMin+inLen < start+width:
    intLow = start
    intHigh = inMin+inLen-1
    intersectRange = [intLow, intHigh-intLow]
    flatLow = inMin
    flatHigh = start-1
    flatRange = [flatLow, flatHigh-flatLow]
    return [intersectRange, flatRange]

  # input is above + intersects map range
  if start < inMin and inMin < start+width < inMin+inLen:
    intLow = inMin
    intHigh = start+width-1
    intersectRange = [intLow, intHigh-intLow]
    flatLow = start+width
    flatHigh = inMin+inLen-1
    flatRange = [flatLow, flatHigh-flatLow]
    return [intersectRange, flatRange]

  # input is superset of map range
  if inMin < start and start+width < inMin+inLen:
    lowRange = [inMin, start-inMin]
    intersectRange = [end, width]
    highRange = [start+width, (inMin+inLen) - (start+width)]
    return [lowRange, intersectRange, highRange]

def joinAllOutputRanges(inputRanges, rangeLines):
  outRanges = []
  for rl in rangeLines:
    for ir in inputRanges:
      ors = createOutputRanges(ir[0], ir[1], rl)
      outRanges.append(ors)
    
    return flatten_chain(outRanges)


def chainOutputRanges(inMin, inLen, mapRanges):
  stageRange = [[inMin, inLen]]

  for toFrom, stageMap in mapRanges:
    stageRange = joinAllOutputRanges(stageRange, stageMap)
  
  return stageRange
    

def parseMapDef(mapDefString): #returns: (srcStr,destStr), map
  mapDefLines = mapDefString.split("\n")
  mapTypeSplit = mapDefLines[0].split(" ")[0].split("-")
  rangeLines = [[int(n) for n in rl.split(" ")] for rl in mapDefLines[1:]]
  stageMap = rangeLines
  
  return (mapTypeSplit[0], mapTypeSplit[-1]), stageMap


def findMinFromOutputRange(outRange):
  return min(r[0] for r in outRange)

def parseInput(inputString):
  inputBlocks = inputString.split("\n\n")
  mapDefs = [parseMapDef(mds) for mds in inputBlocks[1:]]

  startSeeds = [int(s) for s in inputBlocks[0].split(": ")[1].split(" ")]
  startSeedRanges = []
  for i in range(len(startSeeds)/2):
    startSeedRanges.append([startSeeds[i*2], startSeeds[i*2+1]])

  return mapDefs, startSeedRanges

def findLowestLocation(inputString):
  mapDefs, startSeedRanges = parseInput(inputString)

  minLoc = float('inf')

  for ssr in startSeedRanges:
    outRanges = chainOutputRanges(ssr[0], ssr[1], mapDefs)
    minOut = findMinFromOutputRange(outRanges)
    if minOut < minLoc:
      minLoc = minOut
  
  return minLoc


if __name__ == "__main__":

  inputStr = open(inputFile).read()
  lowest = findLowestLocation(inputStr)

  print("lowest: ", lowest)