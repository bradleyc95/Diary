class DiaryEntry:
    
    def __init__(self, entryNum, date):
        self.entryNum = entryNum
        self.date = date
        self.text = " "

    def printEntry(self):
        print("Entry", str(self.entryNum) + ":", self.date, "\n\n" + self.text)
    
    def writeEntry(self):
        print(self.text)
        newText = str(input("Please add to entry..."))
        self.text = self.text + " " + newText

'''def writeEntry(DiaryEntry):
    print(DiaryEntry.text)
    newText = str(input("Please add to entry..."))
    DiaryEntry.text = DiaryEntry.text + " " + newText'''

e1 = DiaryEntry(1, "3/24/2022")

e1.text = "Today I woke up at 10:30am and took my dog on a walk to the coffee shop."

e1.writeEntry()
e1.printEntry()
