inputFile = "../../inputs/day4/input.txt"




def parseCardLine(winHaveString): #prefix stripped string, return 2 int[] winNumbers, haveNumbers
  splitLine = winHaveString.split("|")
  # print("winHave", splitLine)
  winNumbers = [int(s) for s in splitLine[0].strip().split(" ") if len(s) > 0]
  haveNumbers = [int(s) for s in splitLine[1].strip().split(" ") if len(s) > 0]
  return winNumbers, haveNumbers

def calculateCardScore(winNumbers, haveNumbers):
  sharedNumbers = set(winNumbers).intersection(set(haveNumbers))
  if len(sharedNumbers) == 0:
    return 0
  else:
    return 2 ** (len(sharedNumbers)-1)

def calculatePileScoreSum(cardStrings):
  scoreSum = 0
  for cs in cardStrings:
    if len(cs) == 0:
      continue
    winHaveString = cs.split(":")[1]
    winNumbers, haveNumbers = parseCardLine(winHaveString)
    score = calculateCardScore(winNumbers, haveNumbers)
    scoreSum += score
  return scoreSum



if __name__ == "__main__":
  inputLines = open(inputFile).read().split("\n")
  sum = calculatePileScoreSum(inputLines)
  print("sum", sum)