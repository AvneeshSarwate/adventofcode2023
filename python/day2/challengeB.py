inputFile = '../../inputs/day2/input.txt'



def parseRoundString(roundStr):
  colorStrings = [s.strip() for s in roundStr.split(",")]
  # print("colorStrings", colorStrings)
  countDict = {"red": 0, "green": 0, "blue": 0}
  for cs in colorStrings:
    colorSplit = cs.split(" ")
    count = int(colorSplit[0])
    countDict[colorSplit[1]] = count
  return countDict

def parseRoundsLine(roundsLine):
  roundStrings = roundsLine.split(";")
  roundCounts = [parseRoundString(rs) for rs in roundStrings]
  return roundCounts

def gamePower(roundCounts):
  minR = max(*[rc["red"] for rc in roundCounts])
  minG = max(*[rc["green"] for rc in roundCounts])
  minB = max(*[rc["blue"] for rc in roundCounts])
  return minR * minG * minB

def parseGameLine(gameLine):
  gameSplit = gameLine.split(":")
  gameId = int(gameSplit[0].split(" ")[1])
  roundLine = gameSplit[1]
  return (gameId, roundLine)

def parseInput(inputStr, rCount, gCount, bCount):
  lines = inputStr.split("\n")
  runningPower = 0
  for line in lines:
    if len(line) == 0:
      continue
    gameId, roundLine = parseGameLine(line)
    power = gamePower(parseRoundsLine(roundLine))
    # print("power", power)
    runningPower += power
  return runningPower


if __name__ == "__main__":
  inputStr = open(inputFile).read()
  idSum = parseInput(inputStr, 12, 13, 14)
  print("sum: ", idSum)
