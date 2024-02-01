#Task 1.1 and 1.2
CPattern = Pattern("C", "CCC*CCCC*") 
self.__AllowedPatterns.append(CPattern)
self.__AllowedSymbols.append("C")

#Task 2.1 and 2.2
validate = True
for i in range(3):
  for j in range(3):
    if not self.__GetCell(StartRow - i, StartColumn + j).CheckSymbolAllowed(PatternString):
      valiate = False
      break

#Task 3.1 and 3.2
if Row >= 1 and Row <= self.__GridSize and Column >= 1 and Column <= self.__GridSize:

#Task 4.1 and 4.2 and 4.3 and 4.4
QPattern = Pattern("Q", "QQ**Q**QQ", random.randint(1,3))
self.__PatternCount = AmountAllowed
def OutputPatternCount(self):
      print("You have ", self.__PatternCount," patterns left to place of the symbol ", self.__Symbol)
if self.__PatternCount != 0:
          self.__PatternCount = self.__PatternCount - 1
          self.OutputPatternCount()
          return True
        else:
          return False
