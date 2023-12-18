inputFile = "../../input/day5/inputA.txt"



def getFromMap(map, key):
  if key in map:
    return map[key]
  else:
    return key

def fillMapFromLine(dest, start, rangeLen, map):
  for i in range(rangeLen):
    map[start+i] = dest+i

def parseMapDef(mapDefString): #returns: (srcStr,destStr), map
  mapDefLines = mapDefString.split("\n")
  mapTypeSplit = mapDefLines[0].split(" ")[0].split("-")
  rangeLines = [int(rl.split(" ")) for rl in mapDefLines[1:]]
  stageMap = {}
  for rl in rangeLines:
    fillMapFromLine(rl[0], rl[1], rl[2], stageMap)
  
  return (mapTypeSplit[0], mapTypeSplit[-1]), stageMap

def parseMaps(inputString):
  mapDefStrings = inputString.split("\n\n")
  mapDefs = [parseMapDef(mds) for mds in mapDefStrings]
  return mapDefs


def convertSeed(seed, mapChain):
  translatedId = seed
  
  for toFrom, stageMap in mapChain:
    translatedId = getFromMap(stageMap, translatedId)
  
  return translatedId

if __name__ == "__main__":
  x = 5