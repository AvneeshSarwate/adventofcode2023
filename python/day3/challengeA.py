
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

def checkPositionForNumberIds(inputGrid, numIdGrid, rowj, coli): # return list of number ids adacent to this cell (none if no symbol) - only actual ids
  isInBounds = coordInBounds(inputGrid, rowj, coli)

  if not isInBounds:
    return []
  
  isSymbol = not inputGrid[rowj][coli].isdigit() and inputGrid[rowj][coli] != '.'

  if not isSymbol:
    return []
  

  # print("symbol", inputGrid[rowj][coli], rowj, coli)

  adjacentNumberIds = []
  for j in range(-1, 2):
    for i in range(-1, 2):
      row = rowj+j
      col = coli+i
      if not coordInBounds(inputGrid, row, col):
        continue
      # print("    ", row, col)
      numId = numIdGrid[row][col]
      if numId > -1:
        adjacentNumberIds.append(numId)
        # print("    ", row, col, numId)
  # print("    ", rowj, coli, adjacentNumberIds)
  return adjacentNumberIds


def sumGridNumbers(inputGrid):
  numberIdGrid, numberMap = createNumberStructures(inputGrid)

  numRows = len(inputGrid)
  numCols = len(inputGrid[0])

  numberSet = set()
  numberIdSet = set()

  for j in range(numRows): #iterate over rows
    for i in range(numCols): # iterate a single row
      numIds = checkPositionForNumberIds(inputGrid, numberIdGrid, j, i)
      numbers = [numberMap[numId] for numId in numIds]
      numberSet.update(numbers)
      numberIdSet.update(numIds)
  
  # ids = "abcdefghijklmnopqrstuvwxyz1234567890"
  # def charPrint(e, o):
  #   outVal = "_" if e < 0 or e not in numberIdSet else ids[e]
  #   outVal = o if not o.isdigit() and o != "." else outVal
  #   return outVal
  # for j in range(len(numberIdGrid)):
  #   gl = numberIdGrid[j]
  #   print("".join([charPrint(gl[i], inputGrid[j][i]) for i in range(len(gl))]))

  # print()

  dupeSum = 0
  for k in numberIdSet:
    # print(ids[k], numberMap[k])
    dupeSum += numberMap[k]
  
  # print("numberMap", numberMap)
  # print("numberMapSize", len(numberMap))

  # print("numNumbers", len(numberIdSet))
  # print("numberSet", numberSet)
  # print("dupeSum", dupeSum)


  return dupeSum





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
  outputSum = sumGridNumbers(inputGrid)

  print("sum", outputSum)