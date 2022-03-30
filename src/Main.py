import FifteenPuzzle as fp
from util import *
from queue import PriorityQueue
import os

# Tanya pengguna ingin input puzzle darimana
print("~~~SELAMAT DATANG DI SOLVER 15PUZZLE~~~")
print("Anda ingin input puzzle darimana?")
print("1. Input puzzle dari file")
print("2. Input puzzle secara acak")
genPuzzle = int(input("Masukkan angka pilihan Anda: "))
while genPuzzle < 1 or genPuzzle > 2:
    print("Pilihan tidak tersedia, silahkan masukkan angka 1 atau 2")
    genPuzzle = int(input("Masukkan angka pilihan Anda: "))

if genPuzzle == 1:
    fileName = input("Masukkan nama file Anda (tanpa .txt): ")
    dirAwal = os.getcwd()
    arrOfDir = dirAwal.split("\\")
    if arrOfDir[-1] == "src":
        dirAwal = os.path.dirname(dirAwal)
    dirAwal += "\\input\\"
    stateAwal = txtToArray(dirAwal + fileName + ".txt")
else:
    stateAwal = randPuzzle()

# Buat objek puzzle
puzzle = fp.FifteenPuzzle(stateAwal)

# Cek apakah puzzle solvable
if not puzzle.isPuzzleSolvable():
    print("PUZZLE TIDAK DAPAT DISELESAIKAN")
    print(puzzle)
    puzzle.printInfo()
else:
    # Buat prioqueue simpul hidup
    simpulHidup = PriorityQueue()
    print(puzzle)
    puzzle.printInfo()
    simpulHidup.put((puzzle.g(), [puzzle, "up"]))
    simpulHidup.put((6, [puzzle, "up"]))
    simpulHidup.put((4, [puzzle, "up"]))

    # print(puzzle.cekLegalMove())
    while not simpulHidup.empty():
        puzzle = simpulHidup.get()
        print(f"Priority-nya adalah {puzzle[0]}")
        print(puzzle[1][0])

# print(p)
# print(f"Ada {p.g()} ubin yang tidak sesuai tempat")
# p.moveLeft()
# p.moveDown()
# print(p)
# print(f"Ada {p.g()} ubin yang tidak sesuai tempat")