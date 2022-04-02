import FifteenPuzzle as fp
from util import *
from queue import PriorityQueue
import os
from itertools import count
import time

# Tanya pengguna ingin input puzzle darimana
print("~~~SELAMAT DATANG DI SOLVER 15PUZZLE~~~")
print("Anda ingin input puzzle darimana?")
print("1. Input puzzle dari file")
print("2. Input puzzle secara acak")
genPuzzle = input("Masukkan angka pilihan Anda: ")
while genPuzzle != "1" and genPuzzle != "2":
    print("Pilihan tidak tersedia, silahkan masukkan angka 1 atau 2")
    genPuzzle = input("Masukkan angka pilihan Anda: ")

# Jika pengguna memilih 1
if genPuzzle == "1":
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
root = fp.FifteenPuzzle(stateAwal)

# Inisiasi variabel
# Kedalaman tree didapat dari length list of prev moves
listOfSimpulEkspan = {}
found = False
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
jumlahSimpulYangDibangkitkan = 0
unique = 0

# Mulai waktu dari sini
startTime = time.time()

# Cek apakah puzzle solvable
if not root.isPuzzleSolvable():
    print("15PUZZLE TIDAK DAPAT DISELESAIKAN")
    print(root)
    root.printInfo()
    endTime = time.time()
    print("Lama eksekusi program adalah: " + str(endTime - startTime) + " detik")
else:
    # Buat prioqueue simpul hidup
    # Isi dari queue adalah (priority, [puzzle, [list of prev moves]])
    simpulHidup = PriorityQueue()
    print(root)
    root.printInfo()
    # Insert akar ke listOfSimpulEkspan dan simpul hidup
    simpulHidup.put((1, unique, [root, []]))
    listOfSimpulEkspan[(*root.puzzle,)] = True

    # Cek apakah root sudah solusi
    if root.isEqualtoArray(solution):
        endTime = time.time()
        print(root)
        print(f"Jumlah simpul yang dibangkitkan: {jumlahSimpulYangDibangkitkan}")
        print("Lama eksekusi program adalah: " + str(endTime - startTime) + " detik")
    else:
        simpulEkspan = simpulHidup.get()
        # tambahkan simpul hidup yang mungkin dari root
        legalMoves = simpulEkspan[2][0].getLegalMove()
        for move in legalMoves:
            # Buat simpul baru
            simpulBaru = fp.FifteenPuzzle(simpulEkspan[2][0].puzzle.copy())
            simpulBaru.move(move)
            # Masukkan simpul baru ke simpul hidup
            cost = len(simpulEkspan[2][1]) + 1 + simpulBaru.g()
            listOfPrevMoves = simpulEkspan[2][1] + [move]
            simpulHidup.put((cost, unique - 1, [simpulBaru, listOfPrevMoves]))
            unique -= 1
            jumlahSimpulYangDibangkitkan += 1
            listOfSimpulEkspan[(*simpulBaru.puzzle,)] = True
        while not found and not simpulHidup.empty():
            simpulEkspan = simpulHidup.get()
            if simpulEkspan[2][0].isEqualtoArray(solution):
                found = True
                endTime = time.time()
                # print langkah langkah simpul
                print("LANGKAH PENYELESAIAN:")
                i = 1
                for move in simpulEkspan[2][1]:
                    print("Langkah ke-" + str(i) + ":")
                    root.move(move)
                    print(root)
                    i += 1
                print(f"Jumlah simpul yang dibangkitkan: {jumlahSimpulYangDibangkitkan}")
                print("Lama eksekusi program adalah: " + str(endTime - startTime) + " detik")
            else:
                # Bangkitkan anaknya
                legalMoves = simpulEkspan[2][0].getLegalMove()
                for move in legalMoves:
                    # Cek apakah move kebalikan dari move sebelumnya
                    if not move == simpulEkspan[2][0].getOppositeMove(simpulEkspan[2][1][-1]):
                        # Buat simpul baru
                        simpulBaru = fp.FifteenPuzzle(simpulEkspan[2][0].puzzle.copy())
                        simpulBaru.move(move)
                        if not (*simpulBaru.puzzle,) in listOfSimpulEkspan:
                            # Masukkan simpul baru ke simpul hidup
                            cost = len(simpulEkspan[2][1]) + 1 + simpulBaru.g()
                            listOfPrevMoves = simpulEkspan[2][1] + [move]
                            simpulHidup.put((cost, unique - 1, [simpulBaru, listOfPrevMoves]))
                            unique -= 1
                            jumlahSimpulYangDibangkitkan += 1
                            listOfSimpulEkspan[(*simpulBaru.puzzle,)] = True

