
inputFile = "../../inputs/day3/input.txt"



def createNumberStructures(inputGrid): #input is string[][], ouput (int[][], dict[int, int]
  numRows = len(inputGrid)
  numCols = len(inputGrid[0])
  numberIdGrid = [[-1 for i in range(numCols)] for j in range(numRows)]
  numberMap = {}
  nextNumberId = -1
  inNumber = False
  numberBuilder = []

  def flushParsedNumber():
    if len(numberBuilder) > 0:
      lastSeeenNumber = int("".join(numberBuilder))
      # print("    seen number", lastSeeenNumber)
      numberMap[nextNumberId] = lastSeeenNumber
      numberBuilder.clear()

  for j in range(numRows): #iterate over rows
    # print("parsing line", j, inputGrid[j])
    for i in range(numCols): # iterate a single row

      if not inNumber and inputGrid[j][i].isdigit(): #when you start seeing a new number, flush the last one
        if nextNumberId > -1:
          flushParsedNumber()
        nextNumberId += 1

      inNumber = inputGrid[j][i].isdigit()

      if inNumber:
        numberIdGrid[j][i] = nextNumberId
        numberBuilder.append(inputGrid[j][i])
  
    flushParsedNumber() #flush the last seen number
    inNumber = False

  return numberIdGrid, numberMap


def coordInBounds(inputGrid, rowj, coli):
  numRows = len(inputGrid)
  numCols = len(inputGrid[0])
  return 0 <= rowj < numRows and 0 <= coli < numCols

def checkPositionForGearValue(inputGrid, numIdGrid, numIdMap, rowj, coli):
  isInBounds = coordInBounds(inputGrid, rowj, coli)

  if not isInBounds:
    return 0
  
  isGear = inputGrid[rowj][coli] == "*"

  if not isGear:
    return 0
  
  adjacentNumberIds = set()
  for j in range(-1, 2):
    for i in range(-1, 2):
      row = rowj+j
      col = coli+i
      if not coordInBounds(inputGrid, row, col):
        continue
      # print("    ", row, col)
      numId = numIdGrid[row][col]
      if numId > -1:
        adjacentNumberIds.add(numId)
  # print("ids", rowj, coli, adjacentNumberIds)
  if len(adjacentNumberIds) == 2:
    num1 = numIdMap[list(adjacentNumberIds)[0]]
    num2 = numIdMap[list(adjacentNumberIds)[1]]
    # print("gear", num1, num2)
    return num1 * num2
  else:
    return 0



def sumGridGears(inputGrid):
  numberIdGrid, numberMap = createNumberStructures(inputGrid)

  numRows = len(inputGrid)
  numCols = len(inputGrid[0])

  gearSum = 0

  for j in range(numRows): #iterate over rows
    for i in range(numCols): # iterate a single row
      gearSum += checkPositionForGearValue(inputGrid, numberIdGrid, numberMap, j, i)



  return gearSum





if __name__ == "__main__":
  inputString = open(inputFile).read()
  sel = 100
  inputGrid = inputString.split("\n")
  joinedSlice = "\n".join(inputGrid)
  print(joinedSlice)
  print('\n')
  open("sliced_data.txt", "w").write(joinedSlice)
  # inputGrid = [line.split() for line in inputLines]
  # print(inputGrid)
  outputSum = sumGridGears(inputGrid)

  print("sum", outputSum)