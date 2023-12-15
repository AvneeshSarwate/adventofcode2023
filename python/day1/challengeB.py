
inputPath = '../../inputs/day1/input.txt'

import re

digitRE = re.compile('[1-9]|one|two|three|four|five|six|seven|eight|nine')
wordMap = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}


def stringToNumber(digitStr):
  if digitStr.isdigit():
    return int(digitStr)
  else:
    return wordMap[digitStr]

def extractNumberFromLineManual(line):
  wordNames = set(wordMap.keys())
  firstSeen = False
  firstNum = -1
  lastNum = -1
  for i in range(len(line)):
    dig = line[i]
    w3 = line[i:i+3]
    w4 = line[i:i+4]
    w5 = line[i:i+5]
    numStr = ''

    if dig.isdigit():
      numStr = dig
    if w3 in wordNames:
      numStr = w3
    if w4 in wordNames:
      numStr = w4
    if w5 in wordNames:
      numStr = w5
    
    if len(numStr) == 0:
      continue

    if not firstSeen:
      firstNum = stringToNumber(numStr)
      firstSeen = True
    lastNum = stringToNumber(numStr)
  outNum = 0 if firstNum < 0 else firstNum * 10 + lastNum
  print(f"{line} {firstNum} {lastNum} {outNum}")
  return outNum


def extractNumberFromLineRegex(line):
  matches = digitRE.findall(line)
  # print(matches)
  if len(matches) == 0:
    print(line, matches, 0)
    return 0
  else:
    firstNum = stringToNumber(matches[0])
    lastNum = stringToNumber(matches[-1])
    outNum = firstNum * 10 + lastNum
    print(line, matches, f"{firstNum} {lastNum}", outNum)
    return outNum
  


def extractNumberFromLine(line):
  return extractNumberFromLineManual(line)

def extractNumberFromString(fileString):
  runningNum = 0
  for line in fileString.split("\n"):
    runningNum += extractNumberFromLine(line)
  return runningNum

if __name__ == "__main__":
  inputString = open(inputPath).read()
  numberSum = extractNumberFromString(inputString)
  print(f"sum: {numberSum}")

