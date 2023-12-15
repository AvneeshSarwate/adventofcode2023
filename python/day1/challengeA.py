
inputPath = '../../inputs/day1/input.txt'

def extractNumberFromLine(line):
  firstNum = -1
  lastNum = -1
  for i in range(len(line)):
    # print(f"{i} {line[i]} {line[i].isdigit()}")
    if line[i].isdigit():
      if firstNum == -1:
        # print(f"    first: {i} {line[i]} {line[i].isdigit()}")
        firstNum = int(line[i])
      lastNum = int(line[i])
  outputNum = firstNum * 10 + lastNum
  finalOut = 0 if firstNum < 0 else outputNum
  # print(f"line nums {firstNum} {lastNum} {outputNum} {outputNum == math.inf} {finalOut}")
  return finalOut

def extractNumberFromString(fileString):
  runningNum = 0
  for line in fileString.split("\n"):
    runningNum += extractNumberFromLine(line)
  return runningNum

if __name__ == "__main__":
  inputString = open(inputPath).read()
  numberSum = extractNumberFromString(inputString)
  print(f"sum: {numberSum}")

