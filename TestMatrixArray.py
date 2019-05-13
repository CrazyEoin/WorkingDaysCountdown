import os, time

ListOfChar = ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-']

os.system("cls")

CharacterLoopNumber = 0
LoopMax = 10
LineLoopNumber = 0
LineLoopMax = 9

while LineLoopNumber < LineLoopMax:
    time.sleep(0.5)
    os.system("cls")
    CharacterLoopNumber = 0
    while CharacterLoopNumber < LoopMax:
        # print("Loop Number:", CharacterLoopNumber)
        # for char in ListOfChar:
        print(ListOfChar)
        if ((ListOfChar[CharacterLoopNumber+1]) & (CharacterLoopNumber < (LoopMax-1))) == 'X':
            ListOfChar[CharacterLoopNumber] = 'X'
        CharacterLoopNumber += 1

