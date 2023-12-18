inputFile = "../../inputs/day4/input.txt"

import collections


def parseCardLine(winHaveString): #prefix stripped string, return 2 int[] winNumbers, haveNumbers
  splitLine = winHaveString.split("|")
  # print("winHave", splitLine)
  winNumbers = [int(s) for s in splitLine[0].strip().split(" ") if len(s) > 0]
  haveNumbers = [int(s) for s in splitLine[1].strip().split(" ") if len(s) > 0]
  return winNumbers, haveNumbers

def calculateMatchedNumbers(winNumbers, haveNumbers):
  sharedNumbers = set(winNumbers).intersection(set(haveNumbers))
  return len(sharedNumbers)

def calculateCardMatchCounts(cardStrings):
  matchCountMap = {}
  for cs in cardStrings:
    if len(cs) == 0:
      continue
    cardSplit = cs.split(":")
    cardId = int(cardSplit[0].split(" ")[-1])
    winHaveString = cardSplit[1]
    winNumbers, haveNumbers = parseCardLine(winHaveString)
    matchLen = calculateMatchedNumbers(winNumbers, haveNumbers)
    matchCountMap[cardId] = matchLen

  return matchCountMap

def calculateCardRelations(matchCountMap):
  cardRelations = {}
  for k, matchLen in matchCountMap.items():
    adjacents = [k+i+1 for i in range(matchLen)]
    cardRelations[k] = adjacents
  return cardRelations

def calculateInverseCardRelations(cardRelations):
  invCardRelations = collections.defaultdict(lambda: [])
  for k, adjacents in cardRelations.items():
    for a in adjacents:
      invCardRelations[a].append(k)
  return invCardRelations


def calculatePathCounts(invCardRelations, numCards):
  nodesInOrder = list(invCardRelations.keys())
  nodesInOrder.sort()
  numPathsToNode = collections.defaultdict(lambda: 1)
  for k in range(1, numCards+1):
    sources = invCardRelations[k]
    if len(sources) == 0:
      # print(k, sources, numPathsToNode)
      numPathsToNode[k] = 1
    else:
      # print(k, sources, numPathsToNode)
      numPathsToNode[k] = sum([numPathsToNode[i] for i in sources]) + 1
  return numPathsToNode



def pipelineCalculations(inputLines):
  matchCountMap = calculateCardMatchCounts(inputLines)
  # print(matchCountMap)
  # print()
  cardRelations = calculateCardRelations(matchCountMap)
  # print(cardRelations)
  # print()
  invCardRelations = calculateInverseCardRelations(cardRelations)
  # print(invCardRelations)
  # print()
  numPathsToNode = calculatePathCounts(invCardRelations, len(matchCountMap))  
  # print(numPathsToNode)
  # print()

  return sum(numPathsToNode.values())



if __name__ == "__main__":
  inputLines = open(inputFile).read().split("\n")
  sum = pipelineCalculations(inputLines)
  print("sum", sum)