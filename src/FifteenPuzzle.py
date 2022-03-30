# buat array sepanjang 16, 1 nya null
class FifteenPuzzle:
  # Posisi kosong ditandai dengan angka 0
  puzzle = [0 for i in range(16)]
  kurang = [0 for i in range(16)]
  nullPosition = 0

  # Konstruktor yang menerima puzzlenya seperti apa, kemudian mencari posisi 0 dan menginisiasi array kurang
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.nullPosition = puzzle.index(0)
    for i in range(16):
      self.hitungKurang(i)
  
  # Untuk print puzzle
  def __str__(self):
    print("")
    for i in range(16):
      print(self.puzzle[i], end=" ")
      if (i+1) % 4 == 0:
        print("")
    print(f"Null Position: {self.nullPosition}") # jangan lupa hapus
    return ""
  
  def printInfo(self):
    print("KURANG(i):")
    for i in range(1, len(self.kurang)):
      print(f"{i}\t: {self.kurang[i]}")
    print(f"Total KURANG(i) + X: {self.totalKurang()}")

  # Untuk mengecek apakah ubin kosong ada di indeks ganjil atau genap, return 1 jika ganjil
  def cekUbinKosong(self):
    # Jika ubin kosong ada di indeks ganjil, maka return 1
    if self.nullPosition % 2 == 1:
      if 0 <= self.nullPosition <= 3 or 8 <= self.nullPosition <= 11:
        return 1
      else:
        return 0
    else:
      if 4 <= self.nullPosition <= 7 or 12 <= self.nullPosition <= 15:
        return 1
      else:
        return 0

  # Fungsi mereturn jumlah kurang(i) + x
  def totalKurang(self):
    sum = 0
    for i in range(16):
      sum += self.kurang[i]
    sum += self.cekUbinKosong()
    return sum

  # Untuk mengecek apakah puzzle dapat diselesaikan
  def isPuzzleSolvable(self):
    sum = self.totalKurang()
    if sum % 2 == 0:
      return True
    else:
      return False
  
  # Menghitung kurang(Number) dari puzzle
  def hitungKurang(self, Number):
    if Number == 0:
      self.kurang[0] = 15 - self.nullPosition
    else:
      # Buat status apakah Number telah ditemukan di puzzle
      foundNumber = False
      for i in range(16):
        # Ubah status jika Number telah ditemukan
        if self.puzzle[i] == Number:
          foundNumber = True
        # Jika status = True, cek apakah puzzle[i] < Number, jika iya, kurang[idxKurang] += 1
        if foundNumber:
          if self.puzzle[i] < Number and self.puzzle[i] != 0:
            self.kurang[Number] += 1

  # Menghitung ada berapa ubin yang tidak sesuai tempat jika dibandingkan dengan goal state (g(node) kalo di ppt)
  def g(self):
    sum = 0
    for i in range(16):
      if self.puzzle[i] != 0:
        if self.puzzle[i] != i + 1:
          sum += 1
    return sum

  # Method untuk menggerakkan up, down, left, right
  def moveUp(self):
    if 0 <= self.nullPosition <= 3:
      print("Tidak bisa gerak ke atas")
    else:
      self.puzzle[self.nullPosition], self.puzzle[self.nullPosition - 4] = self.puzzle[self.nullPosition - 4], self.puzzle[self.nullPosition]
      self.nullPosition -= 4
      for i in range(16):
        self.hitungKurang(i)
  
  def moveDown(self):
    if 12 <= self.nullPosition <= 15:
      print("Tidak bisa gerak ke bawah")
    else:
      self.puzzle[self.nullPosition], self.puzzle[self.nullPosition + 4] = self.puzzle[self.nullPosition + 4], self.puzzle[self.nullPosition]
      self.nullPosition += 4
      for i in range(16):
        self.hitungKurang(i)
  
  def moveLeft(self):
    if self.nullPosition % 4 == 0:
      print("Tidak bisa gerak ke kiri")
    else:
      self.puzzle[self.nullPosition], self.puzzle[self.nullPosition - 1] = self.puzzle[self.nullPosition - 1], self.puzzle[self.nullPosition]
      self.nullPosition -= 1
      for i in range(16):
        self.hitungKurang(i)
  
  def moveRight(self):
    if self.nullPosition % 4 == 3:
      print("Tidak bisa gerak ke kanan")
    else:
      self.puzzle[self.nullPosition], self.puzzle[self.nullPosition + 1] = self.puzzle[self.nullPosition + 1], self.puzzle[self.nullPosition]
      self.nullPosition += 1
      for i in range(16):
        self.hitungKurang(i)
    
  # Method untuk menggerakkan puzzle sesuai enum move
  def move(self, move):
    if move == 0:
      self.moveUp()
    elif move == 1:
      self.moveDown()
    elif move == 2:
      self.moveLeft()
    elif move == 3:
      self.moveRight()
  
  # Method untuk mengecek apakah puzzle bisa gerak ke atas, bawah, kiri, atau kanan. 0 untuk atas, 1 untuk bawah
  # 2 untuk kiri, 3 untuk kanan
  def cekLegalMove(self):
    # Return array dari move yang legal, dalam bentuk enumerasi
    cond1 = 0 <= self.nullPosition <= 3
    cond2 = 12 <= self.nullPosition <= 15
    cond3 = self.nullPosition % 4 == 0
    cond4 = self.nullPosition % 4 == 3
    if cond1:
      if cond3:
        return [1, 3]
      elif cond4:
        return [1, 2]
      else:
        return [1, 2, 3]
    elif cond2:
      if cond3:
        return [0, 3]
      elif cond4:
        return [0, 2]
      else:
        return [0, 2, 3]
    else:
      if cond3:
        return [0, 1, 3]
      elif cond4:
        return [0, 1, 2]
      else:
        return [0, 1, 2, 3]
   
''' TODO: - '''