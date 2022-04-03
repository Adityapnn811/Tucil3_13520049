import random

def txtToArray(fileName):
    # Reads a text file and returns an array of number
    # Inisiasi array
    arrayOfNum = []
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # Pisah string berdasarkan spasi
            line = line.split(" ")
            for char in line:
                # Append ke array dalam bentuk integer
                if char != '\n' and char != ' ':
                    arrayOfNum.append(int(char))
    return arrayOfNum

def randPuzzle():
    # Returns a random puzzle
    puzzle = []
    while len(puzzle) < 16:
        # Generate angka random 0 hingga 15
        num = random.randint(0,15)
        # Jika angka belum ada di puzzle, append
        if num not in puzzle:
            puzzle.append(num)
    return puzzle
