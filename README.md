# SOLVER 15PUZZLE

> Sebuah program yang menyelesaikan permainan 15 Puzzle dengan algoritma branch and bound

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Direktori](#direktori)
- [_Environment_ dan _Requirements_](#environment-dan-requirements)
- [Cara _Run_ program](#cara-run-program)
- [Author](#author)

## Deskripsi
15 Puzzle adalah sebuah permainan yang mengacak susunan angka dari 1 hingga 15 pada sebuah ubin berukuran 4 x 4. State dari permainan 15 puzzle didasari oleh letak ubin kosong dalam puzzle ukuran 4 x 4 tersebut. Dalam permainan ini, terdapat empat gerakan untuk ubin kosong, yaitu atas, bawah, kiri, dan kanan. Tujuan dari permainan ini adalah menyusun puzzle menjadi susunan akhir seperti berikut
```
 ───────────────
| 1 | 2 | 3 | 4 |
 ───────────────
| 5 | 6 | 7 | 8 |
 ───────────────
| 9 |10 |11 |12 |
 ───────────────
|13 |14 |15 |   |
 ───────────────
 
```

## Direktori
```
|──src                              [Berisi source code dari program]
|   |──Main.py
|   |──FifteenPuzzle.py
|   |──util.py
|──doc
|   |──Tucil3_13520049.pdf          [Laporan Tugas Kecil 3 Stima]
|──test
|   |──puzzle1.txt
|   |──puzzle2.txt
|   |──puzzle3.txt
|   |──puzzle4.txt
|   |──puzzle5.txt
|──README.md
```

## Environment dan Requirements
```
Environment:
-Python 3.9
-Windows 10
```

## Cara Run Program
1. Download repository ini atau lakukan clone repository
2. Buka terminal pada folder repository ini, kemudian ganti direktori ke src dengan cara `cd src`
3. Jika Anda menggunakan windows, run `main.py` dengan perintah `py main.py`
4. Pilih dataset yang Anda inginkan.
5. Pilih kolom dari dataset yang Anda inginkan.
6. Jika ingin menyimpan gambar, input nama file gambar.
7. Gambar akan disimpan pada folder `src`.

## Author
Aditya Prawira Nugroho - 13520049
