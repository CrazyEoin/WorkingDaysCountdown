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

        # for char in ListOfChar:
        print(ListOfChar)
        if CharacterLoopNumber < (LoopMax-1):
            if (ListOfChar[CharacterLoopNumber+1])  == 'X':
                ListOfChar[CharacterLoopNumber] = 'X'
        CharacterLoopNumber += 1
    print("Loop Number:", CharacterLoopNumber)

