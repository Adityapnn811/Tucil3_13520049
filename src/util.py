import random

def txtToArray(fileName):
    # Reads a text file and returns an array of number
    arrayOfNum = []
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(" ")
            for char in line:
                if char != '\n' and char != ' ':
                    arrayOfNum.append(int(char))
    return arrayOfNum

def randPuzzle():
    # Returns a random puzzle
    puzzle = []
    while len(puzzle) < 16:
        num = random.randint(0,15)
        if num not in puzzle:
            puzzle.append(num)
    return puzzle

def hasPuzzleGotChecked(puzzle, listOfSimpulEkspan):
    # Returns True if the puzzle is in list of Simpul Ekspan
    for puzzle2 in listOfSimpulEkspan:
        if puzzle.isEqual(puzzle2):
            return True
    return False